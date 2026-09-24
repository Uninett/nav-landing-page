---
title: 'NAV 5.19.1 released'
date: 2026-09-24T14:52:57+02:00
draft: false
tags:
- release
---

The first maintenance release of the 5.19 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

## Fixed

- The browsable REST API no longer loads Bootstrap CSS from an external CDN, so it renders correctly on air-gapped/offline clients. ([#4089](https://github.com/Uninett/nav/issues/4089))
- Pinned `junos-eznc` below 2.8.1 to keep PortAdmin and SeedDB working for IPv6-addressed Juniper devices, until napalm brackets IPv6 hosts. ([#4119](https://github.com/Uninett/nav/issues/4119))
- Fixed the shipped OIDC `authentication.toml` example, which was rejected by config validation; OIDC providers now accept an entry-level `scope` setting like social providers do. ([#4121](https://github.com/Uninett/nav/issues/4121))
- Fixed a `UnicodeDecodeError` that could prevent ipdevpoll from loading `ipdevpoll.conf` under a non-UTF-8 locale such as `LANG=C`. Configuration files read by ipdevpoll and several other subsystems are now decoded as UTF-8 regardless of the system locale. ([#4132](https://github.com/Uninett/nav/issues/4132))
- Add test dependency `cryptography` - `snmpsim` uses `pysnmp` which uses `cryptography`, but only declares it as *development* dependency ([#4162](https://github.com/Uninett/nav/issues/4162))
- `REMOTE_USER`/SSO authentication works again. Since NAV 5.17.0 the configured variable was ignored entirely, and every visitor was silently treated as the anonymous default account. ([#4168](https://github.com/Uninett/nav/issues/4168))
- Fixed intermittently broken widget drag-and-drop on dashboards, caused by a race between dashboard loading and JavaScript initialization. ([#4180](https://github.com/Uninett/nav/issues/4180))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-19) before upgrading.

Happy NAVing everyone!
