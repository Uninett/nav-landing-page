---
title: 'NAV 5.13.2 released'
date: 2025-05-16T11:34:00+02:00
draft: false
tags:
- release
---

The second maintenance release of the 5.13 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Fixed

- Relax API permissions for endpoints used by NAV web GUI tools intended for
  non-admin users.  Several tools stopped working for non-admin users as a
  result of the permissions lockdown in the 5.13.1 security fix.
  - Relax permissions for API interface view endpoint
    ([#3373](https://github.com/Uninett/nav/issues/3373))
  - Relax permissions for API prefix usage view endpoint
    ([#3374](https://github.com/Uninett/nav/issues/3374))
  - Relax permissions for API list room endpoint
    ([#3375](https://github.com/Uninett/nav/issues/3375))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-13) before upgrading.

Happy NAVing everyone!

