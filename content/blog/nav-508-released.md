---
title: 'NAV 5.0.8 released'
date: 2020-10-23T13:26:00.001+02:00
draft: false
url: /blog/2020/10/nav-508-released/
tags:
- release
---

The eighth maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## Deprecation warning

Python 2 reached its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

## This release fixes a single regression introducedd in NAV 5.0.7

*   [#2196](https://github.com/Uninett/nav/issues/2196) (\[BUG\] ipdevpoll topo job crashes with a PostgreSQL operational error, due to an index size error)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!
