---
title: 'NAV 5.15.1 released'
date: 2025-11-17T11:34:20+0100
draft: false
tags:
- release
---

The first maintenance release of the 5.15 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Fixed

- Fixed crash reports being sent by unauthenticated clients accessing the API ([#3650](https://github.com/Uninett/nav/issues/3650))
- Fixed non-working port overviews for devices that contain modules with slashes in their name. A broken interfaces API endpoint caused both *ipdevinfo* and *interface browser* port lists to malfunction.  ([#3652](https://github.com/Uninett/nav/issues/3652))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-15) before upgrading.

Happy NAVing everyone!

