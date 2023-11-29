---
title: 'NAV 5.8.1 released'
date: 2023-11-29T15:03:00.000+02:00
draft: false
tags:
- release
---

The first maintenace release of the 5.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, but hope to do
so by the end of 2023.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Constrain version of 3rd party module `ciscoconfparse`, in order to avoid NAV not working under Python 3.7 ([#2770](https://github.com/Uninett/nav/issues/2770), [#2771](https://github.com/Uninett/nav/pull/2771))
- Fix ipdevpoll crash error from using SNMP v2c profile example that came with NAV ([#2767](https://github.com/Uninett/nav/issues/2767), [#2768](https://github.com/Uninett/nav/pull/2768))
- Gracefully handle encoding errors in invalid sysname/IP input in SeedDB IP Device form ([#2764](https://github.com/Uninett/nav/pull/2764))
- Gracefully handle errors from invalid profiles list input in SeedDB IP Device form ([#2765](https://github.com/Uninett/nav/pull/2765))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-8) before upgrading.

Happy NAVing everyone!

