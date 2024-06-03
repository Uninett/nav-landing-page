---
title: 'NAV 5.10.2 released'
date: 2024-06-03T10:23:00.000+01:00
draft: false
tags:
- release
---

The second maintenance release of the 5.10 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Do note that 5.10 is the **last series we will package for Debian 10**, as NAV
5.11 will drop support for Python versions older than 3.9

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Changed

- `snmptrapd` renamed to `navtrapd` to avoid naming conflicts with Net-SNMP programs ([#2926](https://github.com/Uninett/nav/issues/2926))

## Fixed

- Replace incorrect fix for premature ARP record closure introduced in 5.10.1 ([#2910](https://github.com/Uninett/nav/issues/2910))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-10) before upgrading.

Happy NAVing everyone!
