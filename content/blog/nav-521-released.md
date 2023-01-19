---
title: 'NAV 5.2.1 released'
date: 2021-09-23T14:13:00.002+02:00
draft: false
url: /blog/2021/09/nav-521-released/
---

The first maintenance release of the 5.2 series of NAV is now out!

This release fixes a particularly nasty regression bug in pping, which would prevent you from being alerted about boxDown events. If you are already running 5.2.0, we recommend that you upgrade as soon as possible.

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 11 (Bullseye) have not been built yet.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## Fixed GitHub issues in this release

*   [#2304](https://github.com/Uninett/nav/issues/2304) (Display alert severity values in the event/alert details page)
*   [#2306](https://github.com/Uninett/nav/issues/2306) (\[BUG\] pping is unable to report unreachable devices in NAV 5.2.0)
*   [#2308](https://github.com/Uninett/nav/issues/2308) (\[BUG\] Alert Profile severity filters that ship with NAV are outdated)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.2.x/release-notes.html#nav-5-2) when upgrading.

Happy NAVing everyone!
