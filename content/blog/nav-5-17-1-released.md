---
title: 'NAV 5.17.1 released'
date: 2026-02-27T11:09:02+01:00
draft: false
tags:
- release
---

The first maintenance release of the 5.17 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

## Fixed

- Fix collapsed multiselects in status tool filters ([#3797](https://github.com/Uninett/nav/issues/3797))
- Event engine now yields to overdue scheduler callbacks between processing queued events, preventing long event batches from blocking time-critical tasks. ([#3798](https://github.com/Uninett/nav/issues/3798)) - Added missing index on `netboxentity.deviceid` to speed up lookups by device. ([#3794](https://github.com/Uninett/nav/pull/3794))
- Fix crash when rendering navlet error responses due to missing navlet ID ([#3802](https://github.com/Uninett/nav/issues/3802))
- Fixed a session crash (`UpdateError`) on the login page that could leak cleartext passwords in Django error emails. ([#3803](https://github.com/Uninett/nav/issues/3803))
- Fix chart widget failing to load images from URLs without query parameters ([#3805](https://github.com/Uninett/nav/issues/3805))
- Fixed `sc.05.16.0001.sql` migration failure on PostgreSQL 14 caused by ambiguous `||` operator when concatenating an integer without an explicit `::TEXT` cast. ([#3806](https://github.com/Uninett/nav/issues/3806))
- Fixed a crash in Netmap when the topology graph exceeds memcached's max item size. The graph is now returned successfully even when it cannot be cached. ([#3795](https://github.com/Uninett/nav/pull/3795))
- Improved active IP collector query performance (~10x) by utilizing partial database indexes on the `arp` table more effectively. ([#3793](https://github.com/Uninett/nav/pull/3793))
- PortAdmin's "commit configuration" endpoint now returns 503 instead of 500 when the device is unreachable or does not support configuration commits, and no longer triggers spurious admin error emails for these expected operational failures. ([#3801](https://github.com/Uninett/nav/pull/3801))
- Turned support for `REMOTE_USER` back on. Regression caused by the new auth-system and its complicated route to the finish line.

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-17) before upgrading.

Happy NAVing everyone!
