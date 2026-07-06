---
title: 'NAV 5.19.0 released'
date: 2026-07-06T12:02:28+00:00
draft: false
tags:
- release
---

The first feature release of the 5.19 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

## Removed

- Stopped supporting Python versions older than 3.11 ([#3994](https://github.com/Uninett/nav/issues/3994))
- Removed `tomli` dependency ([#3996](https://github.com/Uninett/nav/issues/3996))

## Added

- The ipdevpoll `cam` plugin can now optionally log CAM records for switch ports connected to _unmanaged_ neighbors, so that Machine Tracker can locate both the unmanaged device itself and any end hosts behind it. For now, this must be explicitly enabled: See the `[cam]` section in the ipdevpoll reference docs for details. ([#2915](https://github.com/Uninett/nav/issues/2915))
- `navtopology --l2` now logs a per-run summary line to `navtopology.log` with phase timings, per-source resolved-link counts, and database write counts. Per-edge DEBUG lines from the reducer are also tagged with the heuristic that produced each resolution. ([#4067](https://github.com/Uninett/nav/issues/4067))
- The interface details page now shows the full aggregate and stacking hierarchy as a tree, surfacing the derived layer-2 topology (including per-member MLAG neighbours) even when the link is recorded on a lower-layer member port rather than the aggregate itself. ([#4081](https://github.com/Uninett/nav/issues/4081))
- Collect Juniper DOM threshold values as sensors ([#2340](https://github.com/Uninett/nav/issues/2340))
- Added API endpoint for getting, creating and deleting maintenance tasks ([#2927](https://github.com/Uninett/nav/issues/2927))
- Room aliases are now shown as tooltips in IP device info ([#3881](https://github.com/Uninett/nav/issues/3881))
- Added new column to user admin tool user list to show which users have enabled 2-factor authentication ([#4005](https://github.com/Uninett/nav/issues/4005))
- Added `navdashboard` CLI tool for listing, exporting and importing dashboards ([#4028](https://github.com/Uninett/nav/issues/4028))
- Added REST API endpoint for organizations at `api/organization/`
- Added read-only REST API endpoint for router port information at `api/gwportprefix/`

## Changed

#### User-visible changes
- Upgraded Django from 4.2 to 5.2. Remove unused `pytz` dependency. Changed minimum required PostgreSQL version to 14. ([#3958](https://github.com/Uninett/nav/issues/3958))
- Upgraded Sphinx version to 9.0.4 ([#3950](https://github.com/Uninett/nav/issues/3950))
- Excluded JavaScript test files from installed package. ([#3916](https://github.com/Uninett/nav/issues/3916))
- Improved the usability of the two-factor authentication pages with status indicators, clearer warnings, guided setup steps, and copy-to-clipboard support for recovery codes and TOTP secrets. ([#3961](https://github.com/Uninett/nav/issues/3961))
- Improved docs for configuring allauth social auth providers, sans OIDC. ([#5075](https://github.com/Uninett/nav/issues/5075))
- Updated "Installing NAV on Debian" guide to Debian Trixie ([#2886](https://github.com/Uninett/nav/issues/2886))
- Added PostgreSQL rule to never allow the `default` user to be active ([#4027](https://github.com/Uninett/nav/issues/4027))
- Hide map for rooms/locations without coordinates ([#4008](https://github.com/Uninett/nav/issues/4008))
- Hide empty lines in room detail view ([#3893](https://github.com/Uninett/nav/issues/3893))
#### Refactorings (developer-centric)
- Replaced TOML config parser with Pydantic models for authentication config. ([#4025](https://github.com/Uninett/nav/issues/4025))
- Migrated `gauge` and `linear_gauge` from D3 v3 to D3 v7. ([#3907](https://github.com/Uninett/nav/issues/3907))
- Migrated IPAM prefix visualizations from D3 v3 to D3 v7. ([#3965](https://github.com/Uninett/nav/issues/3965))
- Migrated the netmap force-directed graph from D3 v3 to D3 v7. ([#3966](https://github.com/Uninett/nav/issues/3966))
- Replace deprecated `USE_L10N = False` setting with a custom `FORMAT_MODULE_PATH` to preserve ISO date formatting for Django 5.0 compatibility.
- Refactored the Watchdog page to fetch its statistics via HTMX instead of a custom RequireJS/jQuery module. ([#4054](https://github.com/Uninett/nav/issues/4054))
- Refactored the sensor-details page to fetch its current on/off state via HTMX instead of a custom RequireJS/jQuery module. ([#4056](https://github.com/Uninett/nav/issues/4056))
- Improve Devex when using docker compose for development. ([#4036](https://github.com/Uninett/nav/issues/4036))

## Fixed

- Restored audit-log and application-log recording of user logins, which stopped when the login flow moved to `django-allauth` in 5.18.0. ([#4106](https://github.com/Uninett/nav/issues/4106))
- Fixed topology detector assigning the wrong neighbor to aggregate (LAG) interfaces, such as Juniper `ae` interfaces, whose members are discovered through one or more layers of stacked interfaces. ([#4029](https://github.com/Uninett/nav/issues/4029))
- Fixed VLAN topology detection dropping detected VLANs from aggregated (LAG) uplinks, e.g. Juniper `ae` interfaces, where the layer-2 topology resolves on the physical member ports while the 802.1q configuration lives on the aggregate above them. ([#1687](https://github.com/Uninett/nav/issues/1687))
- Made 'My stuff' dropdown behave consistently ([#3799](https://github.com/Uninett/nav/issues/3799))
- Fixed a crash in the Room/Location Status navlets when an alert lacks an associated SMS message record. ([#3899](https://github.com/Uninett/nav/issues/3899))
- Fixed a race condition crash in asyncdns `ForwardResolver` where a DNS error on one record type (A/AAAA) could cause an `AttributeError` when the other record type resolved successfully. ([#3902](https://github.com/Uninett/nav/issues/3902))
- Fixed pipe characters in management profile names or netbox data breaking bulk dump/import ([#3960](https://github.com/Uninett/nav/issues/3960))
- Fixed the broken "approximate database size" indicator on the Watchdog page. ([#4052](https://github.com/Uninett/nav/issues/4052))
- Fixed `ipdevpoll` crashing shortly after startup on systems that forbid writable-and-executable memory. ([#4066](https://github.com/Uninett/nav/issues/4066))
- `pping` no longer misclassifies hosts whose ICMP echo reply round-trip time measures as exactly 0s (a logic error that would only occur during system clock adjustments) ([#4071](https://github.com/Uninett/nav/issues/4071))
- Fixed outdated list of available API endpoints in the documentation ([#4085](https://github.com/Uninett/nav/issues/4085))
- Stopped the room image views from returning spurious server errors (and emailing admins) when deleting already-deleted images or on malformed requests. ([#4103](https://github.com/Uninett/nav/issues/4103))
- Stopped allowing the `navuser` `unlock` and `passwd` commands to work for the `default` user
- `AuthorizationMiddleware` now raises an error if `HtmxMiddleware` has not run before it ([#3713](https://github.com/Uninett/nav/issues/3713))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-19) before upgrading.

Happy NAVing everyone!
