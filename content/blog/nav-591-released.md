---
title: 'NAV 5.9.1 released'
date: 2024-03-15T12:58:00.000+01:00
draft: false
tags:
- release
---

The first maintenance release of the 5.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Fixed broken `navclean` and `navsynctypes`  scripts ([#2875](https://github.com/Uninett/nav/pull/2875), [#2874](https://github.com/Uninett/nav/issues/2874))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-9) before upgrading.

Happy NAVing everyone!

