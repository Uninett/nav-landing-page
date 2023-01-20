---
title: 'NAV 5.0.4 released'
date: 2020-01-16T11:14:00.000+01:00
draft: false
url: /blog/2020/01/nav-504-released/
---

The fourth maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## Deprecation warning

Python 2 reached its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

## Fixed GitHub issues in this release:

*   [#2074](https://github.com/Uninett/nav/issues/2074) (\[BUG\] ipdevpoll inventory job crashes for many devices with an AttributeError)
*   [#2075](https://github.com/Uninett/nav/issues/2075) (\[BUG\] Editing existing API tokens shows no enabled endpoints)
*   [#2076](https://github.com/Uninett/nav/issues/2076) (\[BUG\] Missing Javascript multiselect library used by Useradmin API token form)
*   [#2077](https://github.com/Uninett/nav/issues/2077) (\[BUG\] string handling in snmptrapd is broken on Python 3)
*   [#2081](https://github.com/Uninett/nav/issues/2081) (\[BUG\] Bulk importing netboxes without a managment profile raises an exception)
*   [#2083](https://github.com/Uninett/nav/issues/2083) (\[BUG\] TypeError is raised when creating a csv for download from a room-search)
*   [#2085](https://github.com/Uninett/nav/issues/2085) (\[BUG\] TypeError is raised when getting navlet)
*   [#2087](https://github.com/Uninett/nav/issues/2087) (\[BUG\] Reports with many pages crash once page 4 is visited)
*   [#2090](https://github.com/Uninett/nav/issues/2090) (\[BUG\] Marking machine as disabled in arnold raises TypeError)
*   [#2092](https://github.com/Uninett/nav/issues/2092) (\[BUG\] ipdevinfo sensor tab produces too large Graphite request)
*   [#2093](https://github.com/Uninett/nav/issues/2093) (\[BUG\] PortAdmin crashes when viewing a switch with non-ASCII port descriptions)
*   [#2097](https://github.com/Uninett/nav/issues/2097) (\[BUG\] Adding a manual detention without a number of days until autoenable crashes Arnold)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!
