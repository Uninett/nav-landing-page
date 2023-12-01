---
title: 'NAV 5.8.3 released'
date: 2023-12-01T13:10:00.000+02:00
draft: false
tags:
- release
---

The third maintenace release of the 5.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, but hope to do
so by the end of 2023.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Fix non-working SNMPv1 communication ([#2772](https://github.com/Uninett/nav/issues/2772), [#2779](https://github.com/Uninett/nav/issues/2779), [#2780](https://github.com/Uninett/nav/pull/2780))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-8) before upgrading.

Happy NAVing everyone!

