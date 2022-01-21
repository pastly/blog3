---
title: "How CSS Alone Can Help Track You"
date: 2016-09-04
slug: 2016-09-04-how-css-alone-can-help-track-you
type: posts
draft: false
categories:
  - default
tags:
  - tor
  - tor-browser
  - css
  - attack
---

*This post first appeared on my old blog in September 2016. It is preserved,
but maybe not updated, here.*

---

A common question people ask when they first start using the Tor Browser Bundle
is "why does the browser recommend I don't change my window size?" Reasonable
question. And if you disable JavaScript, you may think that's enough to make
window size irrelevant. Not quite.


**Nov 2019 update**: Tor Browser 9.0 introduced a feature called
[letterboxing](https://blog.torproject.org/new-release-tor-browser-90) to help
mitigate the concerns introduced in this post and the linked demo. I summarize
my thoughts regarding the update on Reddit
[here](https://old.reddit.com/r/TOR/comments/dzwtpn/window_size/f8bo4p3/).
It's still best to leave your Window size alone, but it probably isn't as bad
to resize your window now. If you abhor letterboxing, set
`privacy.resistFingerprinting.letterboxing` in `about:config` to false.

**June 2019 update**:
[TorZillaPrint](https://ghacksuserjs.github.io/TorZillaPrint/TorZillaPrint.html)
will tell you a bunch of things in addition to your window size as determined
by this method.  Remember that [[I caution against reading too much into the
results of a fingerprint test|about-to-use-SkxEFK1m]], but if you know what
to do with this information (even I often don't), then this looks like a useful
website. Thanks for reaching out, Thorin.

**Jan 2019 update**: Add section after "Solutions?" for how to do this with `<picture>`.

**April 2018 update**: I noticed the broken demo link, made a new (hopefully better) demo, and
link to it.

# CSS Features

1. `@media` rules can conditionally apply styles
2. Certain attributes can be URLs.

`@media` rules are commonly used to make a website "responsive," which is web
design speak for "look good on any device." A common condition to care about is
the width of the window. If the width is relatively small, its relatively safe
to assume the user is using a mobile device. More importantly, with a small
width it would be nice to change that top menu bar into a collapsed [hamburger
button](/img/hamburger.png)
and to change the page layout from two columns to one.

Additionally, some CSS attributes can point to URLs. This is commonly used if a
resource doesn't reside on the current domain. For example, fonts and images.

# The Attack

See it in action [here](https://demos.traudt.xyz/css/media/index.html).

Let's have our stylesheet include a ton of `@media` lines that set the page
background to a different URL based on the width of the page.

    @media only screen and (min-width: 500px) { #W {background-image: url(w-0500.png);} }
    @media only screen and (min-width: 501px) { #W {background-image: url(w-0501.png);} }
    @media only screen and (min-width: 502px) { #W {background-image: url(w-0502.png);} }
    @media only screen and (min-width: 503px) { #W {background-image: url(w-0503.png);} }
    [...]
    @media only screen and (min-height: 2997px) { #H {background-image: url(h-2997.png);} }
    @media only screen and (min-height: 2998px) { #H {background-image: url(h-2998.png);} }
    @media only screen and (min-height: 2999px) { #H {background-image: url(h-2999.png);} }
    @media only screen and (min-height: 3000px) { #H {background-image: url(h-3000.png);} }

Now all the attack needs to do is watch his logs to see what images are
requested. If you have a window size different than most other people's, then
you'll stand out. And if the attack owns (or compromises) other websites that
you use in the same browsing session, he could track you across websites. 

The best part: unless you are actively looking for this by checking the source
of every page (and the resources every page loads), then you may not even notice
this happening to you. The demo changed the background image, which was
painfully obvious. The attacker could change the image of a non-displayed
element.

    div#track_users { display: none; }
    @media only screen and (min-width: 100px) { #track_users {background-image: url(100.png);} }
    [...]

You'll never see it coming.


# Solutions?

You could find a way to disable CSS. But this will make the vast majority of
sites out there difficult to browse.

Maybe privacy-orientated browsers such as the Tor Browser Bundle should find a
way to ignore `@media`. Or maybe only ignore `@media` when used with window size
options. Or maybe interact with `@media` options as if the user's resolution is
in some short hard-coded list of possible resolutions.

I don't know if any of those possible solutions are possible. I also don't know
how hard they would be to implement. My Firefox development experience is rather
limited. So for the time being, if your threat model calls for it, **leave the
Tor Browser window size alone**.

# CSS Not Required Either?

[This Reddit post](https://redd.it/afpgq1) led me to
[this onion service](http://b5fxcdl6qvatoxio.onion/) which has the following
interesting bit of HTML5.

    <picture> 
        <source media="(min-width: 1200px)" srcset="pixel.php?screensize=large">
        <source media="(min-width: 992px)" srcset="pixel.php?screensize=medium">
        <source media="(min-width: 768px)" srcset="pixel.php?screensize=small">
        <img src="pixel.php?screensize=tiny" style="width:auto">
    </picture>

If bowers will pick different source images for this
[&lt;picture> tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
even when CSS is disabled, then this is a technique to accomplish exactly what
I've demonstrated above even without CSS.

[[!tag tor-browser tor css attack]]
