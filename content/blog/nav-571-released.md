---
title: 'NAV 5.7.1 released'
date: 2023-09-18T14:15:00.000+02:00
draft: false
tags:
- release
---

The first maintenance release of the 5.7 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, but hope to do
so by the end of 2023.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Fixed regression that caused Netmap to be unusable in 5.7.0 ([#2681](https://github.com/Uninett/nav/issues/2681), [#2683](https://github.com/Uninett/nav/pull/2683))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-7) before upgrading.

Happy NAVing everyone!

