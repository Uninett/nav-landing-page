---
title: 'NAV 5.0.2 released'
date: 2019-12-13T13:32:00.001+01:00
draft: false
url: /blog/2019/12/nav-502-released/
tags:
- release
---

The second maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## Deprecation warning

Python 2 reaches its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

## Fixed GitHub issues in this release:

*   [#2035](https://github.com/Uninett/nav/pull/2035) (Enable room geo positions to be writeable in API)
*   [#2036](https://github.com/Uninett/nav/issues/2036) (\[BUG\] logengine crash with AttributeError on every run on NAV 5.0.1)
*   [#2037](https://github.com/Uninett/nav/issues/2037) (\[BUG\] ipdevpolld multiprocess mode logs reams of TypeErrors)
*   [#2038](https://github.com/Uninett/nav/issues/2038) (\[BUG\] ipdevpoll psuwatch crash with TypeError immediately after upgrade to NAV 5)
*   [#2039](https://github.com/Uninett/nav/pull/2039) (Fix broken natural sort implementation on Python 3 )
*   [#2041](https://github.com/Uninett/nav/issues/2041) (Geomap does not work in NAV 5.0.1)
*   [#2043](https://github.com/Uninett/nav/issues/2043) (\[BUG\] Syslog analyzer search returns nothing)
*   [#2044](https://github.com/Uninett/nav/issues/2044) (\[BUG\] navclean does not work under Python 3)
*   [#2045](https://github.com/Uninett/nav/issues/2045) (\[BUG\] Exception is raised when visiting /api/1/alert/ID)
*   [#2047](https://github.com/Uninett/nav/issues/2047) (\[BUG\] ipdevpoll jobs crash with "A string literal cannot contain NUL (0x00) characters" messages for some devices)
*   [#2048](https://github.com/Uninett/nav/pull/2048) (Support MAC address device IDs from CDP records)
*   [#2049](https://github.com/Uninett/nav/issues/2049) (\[BUG\] ipdevinfo old style Switch port activity view is blank)
*   [#2050](https://github.com/Uninett/nav/issues/2050) (\[BUG\] Geomap is missing links between nodes)
*   [#2052](https://github.com/Uninett/nav/issues/2052) (\[BUG\] ipdevpoll inventory job sometimes crashes when saving POE Port information)
*   [#2054](https://github.com/Uninett/nav/issues/2054) (\[BUG\] pping resolves all boxDown alerts on restart)
*   [#2056](https://github.com/Uninett/nav/issues/2056) (\[BUG\] Cannot add activity graphs to dashboard)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!
