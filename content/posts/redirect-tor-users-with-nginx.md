---
title: "Redirect Tor Users to Your Onion Service with Nginx"
date: 2016-09-07
slug: 2016-09-07-redirect-tor-users-with-nginx
type: posts
draft: false
categories:
  - default
tags:
  - tutorial
  - nginx
  - tor
  - onion-service
---

*This post first appeared on my old blog in September 2016. It is preserved,
but maybe not updated, here.*

*Furthermore, this blog post is largely irrelevant bad practice since the implementation of
[Onion-Location](https://community.torproject.org/onion-services/advanced/onion-location/)
and onion Alt-Svc headers. If interested about the latter, ask me to write a tutorial.*

---

If you host a web onion service that is also available on the clearnet, then
your guests may appreciate it if they can type your clearnet address and
automatically get redirected to your onion address. This is nice if

- your or your users don't want to remember the onion address; or
- you want to share only the clearnet address but want to offer Tor users the
  extra protection that comes with using the onion service. They may not even
  realize you're helping them!

**Warnings:**

- If you choose to *not* encourage your users to bookmark your onion
  address and force them to rely on your clearnet domain name, they will be
  vulnerable to DNS spoofing/poisoning attacks. 
- Technically, traffic coming from an IP address that is home to a Tor exit node
  is not necessarily Tor traffic. You _could_ be automatically and unavoidably
  redirecting someone to a domain they cannot reach.
- If a user isn't using Tor in a sane way (like not using Tor Browser), it's
  possible that by redirecting them to the onion address you're forcing them to
  leak their interest in your website via a DNS query.

As of December 2017, I no longer automatically redirect people on my websites
and do not recommend that anyone else does so.

So with that being said, here's the best way I found to do it.

If you are good with Linux and nginx already, just look
[here](https://github.com/placeholdr/nginx-tor-redirect). This is more for those
that aren't experts already! All I've done is explain what to do with the code
snippets found in that repo.

# 1. Auto generate a list of Tor Exit IP addresses

You will want to put the following code in a script, make the script executable,
and run it automatically periodically.

    IPADDR="$(curl -s https://check.torproject.org/exit-addresses | \
            grep ExitAddress | \
            awk '{print "\t" $2 " 1;"}' | \
            sort -u)"
    cat > /etc/nginx/conf.d/nginx-tor-geo.conf <<EOF
    geo \$torUsers {
        default 0;
    $IPADDR
    }
    EOF

You may want to replace `/etc/nginx/conf.d/nginx-tor-geo.conf` depending on your
Linux distro. 

What this script does is

1. Grab a list of exits and their IPs from the Tor Project
2. Grab only the IP from that list
3. Put the list of IPs in the `/etc/nginx/conf.d/nginx-tor-geo.conf` file with
   some other necessary lines

Put the above code in some script, say `/path/to/my/script.sh`. Then make it
executable by you with `chmod u+x /path/to/my/script.sh`. Then, the easiest way
to get it to run automatically is to use cron. For example, to have cron rerun
this script on the 21st minute of every hour, run the command `crontab -e` and
add the following line.

    21 * * * * /path/to/my/script.sh

Then exit the text editor.

Once the `/etc/nginx/conf.d/nginx-tor-geo.conf` file exists, you can move on.

# 2. Tell nginx about all the Tor exit IPs

This will go a little different based on your Linux distro. In fact, for Debian
(and *likely* Debian-based distros like Ubuntu), you don't even have to do
anything for this step. 

Nginx will likely have an `nginx.conf` file, probably `/etc/nginx/nginx.conf`.
In it, find the `http {}` block. If you already have the following line in the
`http {}` block and you used the same `nginx-tor-geo.conf` file I did in step
1, then you don't need to do anything for step 2.

    include /etc/nginx/conf.d/*.conf;

If you already have that line inside an `http {}` block, move on. If not, add
`include /path/to/your/nginx-tor-geo.conf-from-step-1;`. 

If you had to add the line, you need to reload nginx. If you use systemd, then
run the command `systemctl reload nginx` as root. If you don't use systemd, then
`service nginx reload` will probably work, but it really depends.

# 3. Configure your `server {}` to detect Tor users

You should already have a `server {}` block somewhere that is telling nginx
about the website you are hosting. If you have no idea where, try looking in the
files located in `/etc/nginx/sites-enabled/`.

Once you found the `server {}` block, you're almost done. Let's define some more
variables!

- `myspecial.onion` is the onion address for your onion service
- `/path/to/my/www` is the path to the HTML files for your service

So know that we've agreed on that, find the `location {}` block 
within the `server {}` block. Just add the following lines to the top of
the `location / {}` block.

    if ($torUsers) {
        return 301 http://myspecial.onion$request_uri;
    }

So for example, you might now have

    root /path/to/my/www;
    location / {
        if ($torUsers) {
            return 301 https://myspecia.onion$request_uri;
        }
        try_files $uri $uri/ =404;
    }

Reload nginx one more time, and if there's no errors, you're done.

---

Update Oct 2016: thanks to an anonymous user for the `sort -u` tip to avoid
duplicate entries in `$IPADDR` and to keep nginx logs clean.

Update December 2017: recommend not using this information and remove old
example since my domain no longer does this.

sources: <https://github.com/placeholdr/nginx-tor-redirect>
