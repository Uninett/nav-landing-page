---
title: 'NAV 5.18.1 released'
date: 2026-05-13T10:41:16+02:00
draft: false
tags:
- release
---

The first maintenance release of the 5.18 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 11 (Bullseye), 12 (Bookworm) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).
**NB!** This will be the LAST package we publish for Debian 11 (Bullseye).

## Fixed

- Fixed post-login redirect not returning users to the page they originally requested ([#3954](https://github.com/Uninett/nav/issues/3954))
- Fix unclickable edit button for widget titles on the dashboard. ([#3980](https://github.com/Uninett/nav/issues/3980))
- Fixed removal of all aliases from rooms/locations in SeedDB not being persisted on save. ([#4002](https://github.com/Uninett/nav/issues/4002))
- Fixed LDAP authentication unconditionally rehashing the password on every login, which invalidated the Django session auth hash and broke MFA/TOTP setup for LDAP users. ([#4003](https://github.com/Uninett/nav/issues/4003))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-18) before upgrading.

Happy NAVing everyone!
