---
title: 'NAV 5.0.5 released'
date: 2020-03-13T16:09:00.000+01:00
draft: false
url: /blog/2020/03/nav-505-released/
tags:
- release
---

It's Friday the 13th and a pandemic is upon us, so we thought: Why not release the fifth maintenance version of the 5.0 series of NAV!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## Deprecation warning

Python 2 reached its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

## Fixed GitHub issues in this release:

*   [#1994](https://github.com/Uninett/nav/issues/1994) (snmptrapd linkupdown plugin does not handle v2 traps)
*   [#2101](https://github.com/Uninett/nav/issues/2101) (\[BUG\] Geomap data API endpoint crashes with a TypeError)
*   [#2109](https://github.com/Uninett/nav/issues/2109) (\[BUG\] ipdevinfo sensor details page crashes with AttributeError on unit-less sensors)
*   [#2111](https://github.com/Uninett/nav/issues/2111) (\[BUG\] Logging non-ASCII characters crashes NAV programs)
*   [#2113](https://github.com/Uninett/nav/pull/2113) (Document advice for robust e-mail)
*   [#2114](https://github.com/Uninett/nav/issues/2114) (\[BUG\] Unable to save status filter in \[Status\] page)
*   [#2119](https://github.com/Uninett/nav/pull/2119) (\[BUG\] Latitude/Longitude is displayed weirdly in the SeedDB room list)
*   [#2123](https://github.com/Uninett/nav/pull/2123) (Drop support for legacy status preference pickles)
*   [#2129](https://github.com/Uninett/nav/pull/2129) (Euthanize unresponsive ipdevpoll workers)
*   [#2130](https://github.com/Uninett/nav/issues/2130) (\[BUG\] Cannot import dashboard)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!
