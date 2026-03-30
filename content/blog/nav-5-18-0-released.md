---
title: 'NAV 5.18.0 released'
date: 2026-03-30T12:38:15+02:00
draft: false
tags:
- release
---

The first feature release of the 5.18 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

Please be sure to check the [release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-18) before upgrading, as there may be recommended changes to your config files.

## Security

- The CSRF cookie is now marked as secure when `needs_tls` is enabled in `webfront.conf`, matching the existing behavior of the session cookie. ([#3829](https://github.com/Uninett/nav/issues/3829))
- Passwords are no longer leaked in cleartext in Django error emails when LDAP authentication crashes. ([#3870](https://github.com/Uninett/nav/issues/3870))

## Removed (developer-centric)

- Removed obsolete Docker-based test environment. Replaced by test suite changes that can run in 'normal' development environments. ([#3849](https://github.com/Uninett/nav/issues/3849))

## Added

- Rooms and locations can now have multiple names (aliases). Aliases are searchable throughout NAV -- in the navbar, global search, device history, maintenance, netmap, network explorer, status widgets, and the REST API. Aliases can be managed in *SeedDB* and via bulk import/export. They are displayed on room/location detail pages, in search results, and in SeedDB list views. ([#3314](https://github.com/Uninett/nav/issues/3314), [#3315](https://github.com/Uninett/nav/issues/3315), [#3815](https://github.com/Uninett/nav/issues/3815), [#3818](https://github.com/Uninett/nav/issues/3818), [#3819](https://github.com/Uninett/nav/issues/3819), [#3820](https://github.com/Uninett/nav/issues/3820), [#3821](https://github.com/Uninett/nav/issues/3821), [#3822](https://github.com/Uninett/nav/issues/3822), [#3823](https://github.com/Uninett/nav/issues/3823), [#3836](https://github.com/Uninett/nav/issues/3836), [#3840](https://github.com/Uninett/nav/issues/3840), [#3841](https://github.com/Uninett/nav/issues/3841), [#3844](https://github.com/Uninett/nav/issues/3844), [#3851](https://github.com/Uninett/nav/issues/3851), [#3852](https://github.com/Uninett/nav/issues/3852), [#3868](https://github.com/Uninett/nav/issues/3868), [#3880](https://github.com/Uninett/nav/issues/3880), [#3895](https://github.com/Uninett/nav/issues/3895))
- Added support for two-factor authentication (TOTP), OAuth2, OIDC, and SAML login via `django-allauth`. Authentication can be configured through the new TOML config file `webfront/authentication.toml`. ([#3622](https://github.com/Uninett/nav/issues/3622), [#3676](https://github.com/Uninett/nav/issues/3676), [#3834](https://github.com/Uninett/nav/issues/3834), [#3862](https://github.com/Uninett/nav/issues/3862), [#3873](https://github.com/Uninett/nav/issues/3873), [#3889](https://github.com/Uninett/nav/issues/3889), [#3934](https://github.com/Uninett/nav/issues/3934), [#3936](https://github.com/Uninett/nav/issues/3936))
- Added a report of devices without a known uplink in the topology.
- Debug log runtimes of individual NAVbar search providers.

## Changed

- Auditlog entries can now be sorted by individual columns. Hyperlinks to more details are now provided for actors, objects and targets that still exist in the NAV database. ([#3776](https://github.com/Uninett/nav/pull/3776))
- Updated markdown dependency to 3.8.1. ([#3812](https://github.com/Uninett/nav/issues/3812))
- Downgraded spammy `WARNING` log about alerts referencing deleted objects to `DEBUG` level. ([#3927](https://github.com/Uninett/nav/issues/3927))

## Changed (developer-centric)

- Standardize vendored JavaScript library management.

  Vendored JS files now follow a consistent `<name>-<version>.min.js` naming
  convention and are tracked as npm dependencies for easier version management.
  A `vendor.py` tool is included to automate installing and copying vendored
  files. ([#2470](https://github.com/Uninett/nav/issues/2470))
- Tox environments and GitHub workflows switched over to uv for dependency management. ([#3859](https://github.com/Uninett/nav/issues/3859))

## Fixed

- Fix network explorer search not working after the first search per page load. ([#3853](https://github.com/Uninett/nav/issues/3853))
- Fixed l2trace crash when tracing through a netbox with no associated prefix. ([#3866](https://github.com/Uninett/nav/issues/3866))
- LDAP login no longer crashes with a 500 error when a user cannot be found during group membership verification. ([#3871](https://github.com/Uninett/nav/issues/3871))
- Fix report column tooltips (`$explain_`) not showing when the column also has a `$name_` override. ([#3876](https://github.com/Uninett/nav/issues/3876))
- Fixed a crash in SeedDB bulk import when IP addresses contain trailing whitespace. ([#3884](https://github.com/Uninett/nav/issues/3884))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-18) before upgrading.

Happy NAVing everyone!
