---
title: "BM Major Releases"
date: 2020-03-04
slug: 2020-03-04-bm-major-releases"
type: posts
draft: false
categories:
  - default
tags:
  - bm
---

*What follows are three posts announcing new major releases of BM (Blog Maker),
the software I wrote and "maintained" that hosted my old blog, in January 2017
and March 2020. These are preserved here, but not updated. Links will be
broken.*

---

# BM v3.0.0 is Released

Today I've released a new major version of [[!taglink BM]], consisting of about 140
commits! See the [changelog](https://gogs.system33.pw/mello/bm/src/master/CHANGELOG.md#v300---2017-01-16)
for a summary of all the changes, and please
report issues at [the issue tracker](https://gogs.system33.pw/mello/bm/issues).
Here's the important and exciting highlights.

## Important

__`make` cannot be called by the user anymore__ as BM needs to setup the
environment for it. It probably should have never been called by hand, and
hiding the Makefile in v3.0.0 further discourages manual `make` calls.

__Post URLs have changed__, but probably won't do so again for a while--if
ever--as this is quite rude of me to do. Now post URLs are limited to the
first three words of the post title plus the ID. Before it was all words of the
title.

## Exciting

__Permalinks__ have been added. This was prompted in part by the previous
change. If the option for it is enabled (which it is by default), a little
permalink will be added in every post's header. Permalinks consist soley of a
post's ID, so they will never change so long as you don't manually change a
post's ID!

__BM can optionally make the source post files available for download by your
readers__. If the option is set, not only will `/posts/foobar-12345678.html` be
generated as usual, but `/posts/foobar-12345678.bm` will as well, the latter
being an exact copy of the file you edit.

__A 404 page__ has been added. Special webserver configuration is required to
get the most out of it. See [the wiki](https://gogs.system33.pw/mello/bm/wiki/AdvancedConfiguration).

## Thoughts

This release took a very long time. It introduced many backend changes, most
concerning a major design change: move as much dependency logic into the
Makefile as possible. Before the majority of BM's logic was in three large
scripts. Now

- post data is extracted into seperate files (in `meta/`)
- as little work is done as possible when changes are made (this will need
  continued improvement)
- later build steps only depend on the post data files that they require

It was an interesting challenge figuring out how to call my bash functions and
use bash variables inside the Makefile. The gist of how it works is

- sourcing `globals.sh` before calling `make`
- calling bash's `set -a` at the top of the `globals.sh` file
- calling `set +a` at the end for good measure

This exports all function and variable definitions into the environment that
make runs in.

### Future

Going forward, I already have a few features in mind for minor releases, even
after tackling the huge pile that built up while working on v3.0.0.

The first easy thing I'll likely do is adding a license option, so users can
easily license the contents of their blogs.

But another big idea that a Redditor suggested to me is themeing. Right now BM
has one look. It's "easy" to change that look, especially if what you want to
change is coloring or spacing. But wouldn't it be nice to be able to easily
switch between themes with a single command? You could download additional
themes, share them, etc. This is a large change that will take some time, and
undoubtedly a new major version.

Another big idea that I'm chewing on in my free time is moving all posts and
customizable files into a single directory. This would pave the way towards
easily allowing you to version control your posts __and__ your configuration
options (and maybe even theme). In fact, it's conceivable that BM could even
make commits for you. This is another large change that would also take a new
major version.

In general, you can see the things I'm thinking about and working on at the
[issue tracker](https://gogs.system33.pw/mello/bm/issues).

### Do you use BM?

Finally, I'd like to ask anyone out there who uses BM and doesn't mind their
blog, wiki, whatever being public to please let me know! I'd love to hear about
your experience using BM.


# BM v4.0.0 is Released

[changelog]: https://gogs.system33.pw/mello/bm/src/master/CHANGELOG.md#v400---2017-01-29
[issues]: https://gogs.system33.pw/mello/bm/issues
[wikitheme]: https://gogs.system33.pw/mello/bm/wiki/Home#theme-selection
[wikitheming]: https://gogs.system33.pw/mello/bm/wiki/Theming

Yesterday I released _yet another_ new major version of [[!taglink BM]]! The
[changelog][changelog] has a summary of changes. As before, please report any
issues at the [issue tracker][issues].

## Important

There are two big changes that should be noted.

Your configuration file needs to move. It used to be in `include/bm.conf`, but
that directory has been emptied out. Your configuration file now belongs in your
posts directory, `posts/bm.conf`. BM comes with a script in `tools/` to help you
transition from v3 to v4, but really it's as simple as moving your configuration
file. After you've moved it, you may delete the include directory. It __should__
be empty.

The other major change is themes! Themes allow you to quickly change the look of
your website. They can easily be shared as all the important bits and pieces are
in one directory per theme. Here's the "terminal" theme that I created and will
officially support in addition to the default theme.

![terminal theme](/img/bm-4.0-1.png)

For information how how to set your theme, [see here][wikitheme]. For
information about creating your own theme, [see here][wikitheming]. It's very
easy, especially if you start out copy/pasting an already good one.

## Other new features

__Page signing__ was added. Now, given a gpg fingerprint, BM will automatically
cryptographically sign all output files (even the CSS!) and leave a note in the
footer saying so in officially supported themes.

![signature note](/img/bm-4.0-2.png)

(Ignore the version number, this was added in v4.0.0. I should probably decide
something about "in development" versioning...)

If page signing is enabled, then `/pubkey.gpg` will also be automatically
generated with the public key used for signing.

__Licensing your content has been made easier__. A new config option,
`[[LICENSE_TEXT]]`, was added. The contents of it will be placed verbatim in the
footer of officially supported themes. I have set my `[[LICENSE_TEXT]]` to the
following string in order to get the Creative Commons image link you see on my
blog.

    <a href='https://creativecommons.org/licenses/by-sa/4.0/'>
    <img src='https://licensebuttons.net/l/by-sa/4.0/80x15.png'/></a>

The above produces

<a href='https://creativecommons.org/licenses/by-sa/4.0/'>
<img src='https://licensebuttons.net/l/by-sa/4.0/80x15.png'/></a>

Such complicated license text is obviously not necessary.

## Future

Some of the next things I want to work on include

- Adding an easier way to modify theme metadata
- Move the selected theme symlink to the post directory in order to...
- Put all the user-specific files (config, post files, theme) in one directory
  so it can be completely version controlled and swapped in and out.
- An option to exclude a post from the homepage
- An asset directory, which has its contents copied to the build (for images and
  things that aren't post files but you want to host and make available for
  download)

To watch my progress or to suggest things, see the [issue tracker][issues].

If you're using BM, I would love to hear about it! Please let me know somehow.

# BM v5.0.0 is Released
Hey look. This dead project is getting a new major version. Don't count on this
continuing to happen! ;)

## Important

The default/bundled markdown parser is changed from `Markdown.pl` to
`cmark-gfm`.  While making the change, I *sometimes* noticed the content of my
pages being rendered differently. Once the change was finally fully made,
however, the content renders the same. I have no idea why it would be
different, nor do I know what I was doing to make it break/unbreak.

Thus, to be cautious, I'm calling this a breaking change. Thus a new major
version for [[!taglink BM]] is required.

The full spec for Github Flavored Markdown is
[here](https://github.github.com/gfm/). BM bundles `cmark-gfm` v0.29.0, so
assuming the spec still says it applies to that version at the top, BM *should*
support everything you read there. I haven't tested anything other than
~~strikethrough~~ and 

| tables | tables |
|--------|--------|
| tables | tables |

I do not expect to update the bundled `cmark-gfm` with any regularity. I don't
even expect to update BM!

## Other new features

Since v4.0.0

**A static directory**.  Put stuff in `static/` and it will be copied to
`build/static/`. Put your resume at `static/docs/resume.pdf` and link to it
with `[my resume](/static/docs/resume.pdf)`.

**RSS feed generation**.  I think I implemented it poorly. I don't know. I
don't use RSS feeds.
