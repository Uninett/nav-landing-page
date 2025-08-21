---
title: 'NAV 5.14.0 released'
date: 2025-08-21T13:47:00+02:00
draft: false
tags:
- release
---

The first feature release of the 5.14 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Added

### User-visible additions

- New SQL reports in the *Report* tool:
  - Added an `operational entities` SQL report.  ([#1947](https://github.com/Uninett/nav/issues/1947))
  - Added an `Events detected last 24 hours` SQL report.  ([#3305](https://github.com/Uninett/nav/issues/3305))
- Collection job refreshing from web UI:
  - Added button to refresh `ipdevpoll` background jobs directly from *IP Device Info* tool. ([#3350](https://github.com/Uninett/nav/issues/3350))
  - `ipdevpoll` can now immediately reschedule jobs on incoming refresh events on the NAV event queue. Refreshes can be ordered from the command line using the `navrefresh` program.  ([#2626](https://github.com/Uninett/nav/issues/2626))
- Added QR code link features:
  - Added link to "My Stuff" menu to generate QR code link to current page.  ([#2897](https://github.com/Uninett/nav/issues/2897))
  - Added button to SeedDB that downloads a ZIP file with QR Codes linking to the selected netboxes/rooms. ([#2899](https://github.com/Uninett/nav/issues/2899))
  - Added config option to switch between generating SVG or PNG QR codes.  ([#2916](https://github.com/Uninett/nav/issues/2916))
- API additions:
  - Added API endpoint for looking up vendor of MAC address.  ([#3337](https://github.com/Uninett/nav/issues/3337))
  - Added API endpoint for the `NetboxEntity` model.  ([#3378](https://github.com/Uninett/nav/issues/3378))
  - JWT token signing features:
    - Added API endpoint for JWT refresh tokens.  ([#3270](https://github.com/Uninett/nav/issues/3270))
    - Added new tab to *User and API administration* tool for managing JWT refresh tokens.  ([#3273](https://github.com/Uninett/nav/issues/3273))
    - Expiration times for issued JWT refresh tokens can be configured via `jwt.conf`. ([#3016](https://github.com/Uninett/nav/issues/3016))
    - Added support for including API endpoint read/write permission claims to JWT tokens.
- Added password security warnings:
  - Show a banner if the logged in user's password is insecure or old and it should be changed. ([#3345](https://github.com/Uninett/nav/issues/3345))
  - Show a banner to admins if other users' passwords are insecure or old.  ([#3346](https://github.com/Uninett/nav/issues/3346))
- Added support for the *T3611* sensor from Comet.  ([#3307](https://github.com/Uninett/nav/issues/3307))
- Added support for fetching DHCP pool statistics from Kea DHCP API.  ([#2931](https://github.com/Uninett/nav/issues/2931))


### Developer-centric additions

- Added HTMX as new front-end library.  ([#3386](https://github.com/Uninett/nav/issues/3386))
- Document practical usage of devcontainer for developers.  ([#3398](https://github.com/Uninett/nav/issues/3398))
- Added developer utilities for easily dumping/loading production data into devcontainer.

## Changed

### User-visible changes

- Replaced QuickSelect component picker with dynamic HTMX-based search in Maintenance tool.  ([#3425](https://github.com/Uninett/nav/issues/3425))
- Replaced QuickSelect component picker with dynamic HTMX-based search in Device history tool.  ([#3434](https://github.com/Uninett/nav/issues/3434))
- Dependency changes:
  - Updated NAPALM dependency to 5.0 ([#2358](https://github.com/Uninett/nav/issues/2358))
  - Updated `django-rest-framework` to version 3.14+, for proper compatibility Django 4.2 ([#3403](https://github.com/Uninett/nav/issues/3403))

### Developer-centric changes

- Replaced usage of `twisted.internet.defer.returnValue` with regular Python `return`, due to deprecation in newest Twisted version.  ([#2955](https://github.com/Uninett/nav/issues/2955))
- Redefined NAV account model to be usable as a Django user model.  ([#3332](https://github.com/Uninett/nav/issues/3332))
- Remove unused `ColumnsForm` ([#3243](https://github.com/Uninett/nav/issues/3243))


## Fixed

- Fixed missing ARP API endpoint documentation for IP address filtering.  ([#3215](https://github.com/Uninett/nav/issues/3215))
- Fixed broken location *history* searches from location view page.  ([#3360](https://github.com/Uninett/nav/issues/3360))
- Restored ISO timestamps in the web UI (as they were before NAV 5.13) ([#3369](https://github.com/Uninett/nav/issues/3369))
- Fixed broken `Add to dashboard` functionality for boolean value sensors ([#3394](https://github.com/Uninett/nav/issues/3394))
- Fixed sorting by timestamp columns in threshold rule table and Useradmin API-token table. ([#3410](https://github.com/Uninett/nav/pull/3410))
- Take advantage of auxiliary `end_time` indexes on ARP table to improve prefix usage lookups in API. ([#3413](https://github.com/Uninett/nav/pull/3413))
- Made Docker test environment usable for devs on Apple silicon Macs.

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-14) before upgrading.

Happy NAVing everyone!

