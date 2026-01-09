---
title: 'NAV 5.16.1 released'
date: 2026-01-09T13:27:31+0100
draft: false
tags:
- release
---

The first maintenance release of the 5.16 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Fixed

- Fixed location search for locations with slashes in names ([#3717](https://github.com/Uninett/nav/issues/3717))
- Fixed `pping` and `snmptrapd` crashes when attempting to look for config files in inaccessible directories ([#3720](https://github.com/Uninett/nav/issues/3720))
- Support RFC3339/ISO8601-formatted timestamps when parsing syslog messages in `logengine` ([#3722](https://github.com/Uninett/nav/issues/3722))
- Fixed GeoMap display of rooms/locations with slashes in their IDs ([#3724](https://github.com/Uninett/nav/issues/3724))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-16) before upgrading.

Happy NAVing everyone!

