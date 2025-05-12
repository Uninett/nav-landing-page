---
title: 'NAV 5.13.1 (SECURITY FIX) released'
date: 2025-05-12T14:45:00+02:00
draft: false
tags:
- release
- security
---

The first maintenance release of the 5.13 series of NAV is now out, and
contains a security patch for a serious privilege escalation
vulnerability in the web GUI.  We recommend that all users *upgrade as
soon as possible*.

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Security

- Lock down API access for unprivileged users

  By default, NAV granted full API access to logged-in users, regardless of
  their configured privilege level.  This would give unprivileged users access
  to manipulate NAV configuration and even elevate their own user privileges to
  administrator level.  [Read the full security advisory
  here.](https://github.com/Uninett/nav/security/advisories/GHSA-gprr-5vvf-582g)

## Changed

- Update NAPALM dependency to 5.0 to keep NAV web GUI working
  ([#2358](https://github.com/Uninett/nav/issues/2358))

## Fixed

- Fix filtering of 'Last seen' and sorting by 'Last active' in netbox
  interfaces view in room info
  ([#3329](https://github.com/Uninett/nav/issues/3329))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-13) before upgrading.

Happy NAVing everyone!

