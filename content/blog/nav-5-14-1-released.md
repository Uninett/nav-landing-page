---
title: 'NAV 5.14.1 released'
date: 2025-09-01T13:30:59+0200
draft: false
tags:
- release
---

The first maintenance release of the 5.14 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Fixed

- Correctly display current chosen filter in Status tool ([#3442](https://github.com/Uninett/nav/issues/3442))
- Fixed showing activity graphs in port details in ipdevinfo ([#3484](https://github.com/Uninett/nav/issues/3484))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-14) before upgrading.

Happy NAVing everyone!

