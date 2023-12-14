---
title: 'NAV 5.8.4 released'
date: 2023-12-14T10:35:00.000+02:00
draft: false
tags:
- release
---

The fourth maintenace release of the 5.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Allow admins to configure ports with invalid or unset native VLANs in PortAdmin ([#2477](https://github.com/Uninett/nav/issues/2477), [#2786](https://github.com/Uninett/nav/pull/2786))
- Fix bug that caused PoE config to be completely disabled for Cisco devices where at least one port did not support PoE ([#2781](https://github.com/Uninett/nav/pull/2781))
- Fix PortAdmin save button moving around for ports without PoE support ([#2782](https://github.com/Uninett/nav/pull/2782))
- Fix PortAdmin bug that prevented switching PoE state back and forth without reloading entire page ([#2785](https://github.com/Uninett/nav/pull/2785))
- Fix regression that caused maintenance tasks to be un-editable ([#2783](https://github.com/Uninett/nav/issues/2783), [#2784](https://github.com/Uninett/nav/pull/2784))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-8) before upgrading.

Happy NAVing everyone!

