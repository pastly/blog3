---
title: "Creating Private V3 Onion Services"
date: 2019-01-19
slug: 2019-01-19-creating-private-v3-onion-services"
type: post
draft: false
toc: true
categories:
  - default
tags:
  - onion-service
  - tutorial
  - tor
---

*This post first appeared on my old blog in January 2019. It is preserved, but
maybe not updated, here.*

---

[v2-post]: {{< ref "creating-private-onion-services" >}}

This post is about v3 onion services with 56 characters in their name. For the
old post for creating private v2 onion services, see [here][v2-post].

In that old post I talked about some of the great features of Tor onion
services. The features still apply with the new onion services: they are still
end-to-end encrypted, they still assure you that it is impossible for anyone to
modify your traffic, etc.

Regular v3 onions fix the issue that v2 onions had where a malicious HSDir
could snoop and learn about onion services that the owner literally never
advertised. This is great, you no longer have to make your onion service
regular authorization in order to avoid malicious HSDirs. If you never tell
anyone your v3 onion address, no one will ever know it exists.

Regardless of whether you're okay with people knowing your v3 onion address or not,
what if you still wanted to require people to know a secret key in order to
be allowed to connect to your v3 onion service? You can do that now.

<!--
Some quick facts:

- HSDirs cannot snoop and learn addresses for v3 onion services (you get this
  for free with v3 onions even if you don't do anything in this post)
- All authorized users connect to the same onion address
- There is not a limit on the number of authorized users there can be
  (**TODO**: fact check this)
-->

Here's how you set this up.

Alice is the client. Bob runs an onion service and wants to allow Alice to
connect to it. Everyone has Tor 0.3.5.7 or newer.

# 0. Know how to set up an onion service

If you don't know how to set up a regular onion service,
[go figure that out now](https://www.torproject.org/docs/tor-hidden-service.html.en).
Don't come back until you can connect to it successfully.

Note that all the file and directory paths used her make sense for me, but may
not make sense for you on your computer. Only copy/paste things intelligently.

I will assume the onion address is y34f3abl2bou6subajlosasumupsli2oq7chfo3oqfqznuedqhzfr5yd.onion

# 1. Generate a key for Alice

Someone needs to generate a key for Alice to use. I don't think it really
matters if Bob generates it for her instead. I will assume it is Alice.  I
would like to see Tor produce something themselves (perhaps inside little-t
tor, perhaps a script shipped with its source code, etc.) but for now you have
to figure out how to do it yourself.

I wrote a
[simple python3 script](https://github.com/pastly/python-snippits/blob/master/src/tor/x25519-gen.py)
to generate an x25519 key pair. It requires [PyNaCl](https://pynacl.readthedocs.io/en/stable/).

Record the base32-encoded key pair somewhere. You'll need it soon. Here's some example output.

    public:  MEE25GRMPHS7NKNV3B7MHB6Y46FVGBALIC2OZUOD47CGYQMKQ56A
    private: NQ2IJRNRZWPKVJNGWV7N6KJFUS235N27IP5NZ7UAXMXWUMILNLJA


# 2. Bob tells his Tor about the public key for Alice

Assume Bob already has this torrc snippet.

**/etc/tor/torrc**

    HiddenServiceDir /var/lib/tor/foo_v3_onion/
    HiddenServicePort 5248

He should have an `authorized_clients` directory inside `foo_v3_onion/`. If it
doesn't already exist, he should figure out what is wrong because Tor should
have made it for him.

Inside `authorized_clients/`, Bob should make a file ending in `.auth`; for
example, `alice.auth`. Inside that file, he should put the following content.

    descriptor:x25519:<base32-encoded-public-key>

Using an example public key ...

**/var/lib/tor/foo\_v3\_onion/authorized\_clients/alice.auth**

    descriptor:x25519:MEE25GRMPHS7NKNV3B7MHB6Y46FVGBALIC2OZUOD47CGYQMKQ56A

Bob should then restart his Tor.

If Bob wants to add more users, he can repeat this process with additional
files in this directory.

# 3. Alice tells her Tor about her private key

First she should check that her torrc has a `ClientOnionAuthDir` option set.
These paths will be significantly different based on if she is configuring her
system's background Tor daemon or if she is configuring Tor Browser. (**T**)
means an example system Tor daemon path and (**TB**) means an example Tor
Browser path. Remember, yours may still be different.

(**T**) **/etc/tor/torrc**

    ClientOnionAuthDir /var/lib/tor/onion_auth

(**TB**) **[Tor Browser folder]/Browser/TorBrowser/Data/Tor/torrc**

    # In case this path ends up not making sense on your system ...
    # The directory I'm aiming for onion_auth to be in is the same
    # directory that contains the torrc
    ClientOnionAuthDir TorBrowser/Data/Tor/onion_auth

After restarting Tor, if this directory doesn't exist, Alice should make it with
0700 permissions.

Inside this directory, she then should add a file ending in `.auth_private`;
for example, `bob.auth_private`.  Inside that file, she should add the following content.

    <onion-address>:descriptor:x25519:<base32-encoded-private-key>

Using an example onion address and private key ...

(**T**) **/var/lib/tor/onion\_auth/bob.auth\_private**

    y34f3abl2bou6subajlosasumupsli2oq7chfo3oqfqznuedqhzfr5yd:descriptor:x25519:NQ2IJRNRZWPKVJNGWV7N6KJFUS235N27IP5NZ7UAXMXWUMILNLJA

(**TB**) **[Tor Browser folder]/Browser/TorBrowser/Data/Tor/onion\_auth/bob.auth\_private**

    y34f3abl2bou6subajlosasumupsli2oq7chfo3oqfqznuedqhzfr5yd:descriptor:x25519:NQ2IJRNRZWPKVJNGWV7N6KJFUS235N27IP5NZ7UAXMXWUMILNLJA

Alice should then restart her Tor.

If Alice needs keys for more onion addresses, she can repeat this process with
additional files in this directory.

Notes:

- The `.onion` suffix in the address is removed in those `.auth_private` files.
- I haven't actually tried this on Tor Browser, I'm merely relaying what
  [a brave Redditor managed to figure out](https://reddit.com/r/TOR/comments/anu1f7/how_to_set_up_version_3_hidden_service_with/efzcdd9/?context=100).
- Tor Browser doesn't expect you to edit its torrc, so if you change Tor
  settings graphically in Tor Browser, you may find it has generated a new
  torrc without your changes.

# 4. Done

If everyone's Tor processes are running without error, then setup should be
complete. Alice should be able to connect, but no one else should be able to.

Bob can authorize up to [about
350 clients per onion service](https://trac.torproject.org/projects/tor/ticket/29134).
