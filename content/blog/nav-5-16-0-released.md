---
title: 'NAV 5.16.0 released'
date: 2025-12-19T10:13:14+0100
draft: false
tags:
- release
---

The first feature release of the 5.16 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Security

- Upgrade jQuery library and dependencies ([#3582](https://github.com/Uninett/nav/issues/3582))
- Stop revealing actual API tokens in any type of log ([#3686](https://github.com/Uninett/nav/issues/3686))
- Escape column text in audit log table to mitigate potential XSS vulnerabilities ([#2803](https://github.com/Uninett/nav/issues/2803))

## Added

- Added support for searching for inactive devices by serial number in Device History tool ([#1996](https://github.com/Uninett/nav/issues/1996))
- Added OS version and NAV version to exception debug view ([#2082](https://github.com/Uninett/nav/issues/2082))
- Add proper audit log entries for API token manipulations (legacy and JWT) ([#3405](https://github.com/Uninett/nav/issues/3405))
- Added a Django authentication backend to do NAV legacy style LDAP authentication, in preparation for authentication system rewrite ([#3498](https://github.com/Uninett/nav/issues/3498))
- Added confirmation modal when deleting dashboards ([#3648](https://github.com/Uninett/nav/issues/3648))
- Added test/research program `nav_cisco_auth_sessions` to retrieve information about authentication framework sessions from Cisco switches ([#3711](https://github.com/Uninett/nav/issues/3711))
- Added support for searching by description in main info search ([#3149](https://github.com/Uninett/nav/issues/3149))
- Allow `NAV_CONFIG_DIR` environment variable to override where NAV looks for configuration files ([#3697](https://github.com/Uninett/nav/issues/3697))

## Changed

- Added new dependency `distro` for identifying Linux distributions ([#2082](https://github.com/Uninett/nav/issues/2082))
- Load info page search results with HTMX ([#3618](https://github.com/Uninett/nav/issues/3618))
- Load filtered device history with HTMX ([#3663](https://github.com/Uninett/nav/issues/3663))
- Disabled broken audit log actor sorting ([#3581](https://github.com/Uninett/nav/issues/3581))

## Fixed

- Fixed room urls for rooms with slashes in name ([#3661](https://github.com/Uninett/nav/issues/3661))
- Upgrade select2 dependency to latest version ([#1873](https://github.com/Uninett/nav/issues/1873))
- Strip null bytes from LLDP local chassis IDs to avoid `topo` job abort errors (ValueErrors) ([#2479](https://github.com/Uninett/nav/issues/2479))
- Fixed ipdevpoll inventory job crash when including Comet T3611 MIB for collecting information for other Comet sensors ([#3566](https://github.com/Uninett/nav/issues/3566))
- Properly redirect entire browser to login page when a background HTMX request is received on an unauthenticated session (e.g. after session times out) ([#3656](https://github.com/Uninett/nav/issues/3656))
- Fixed accessing seeddb/room URLs for rooms with '/' in names ([#3659](https://github.com/Uninett/nav/issues/3659))
- Fixed broken event search URL ([#3677](https://github.com/Uninett/nav/issues/3677))
- Fixed accessing SeedDB urls for locations, usages, organizations and device groups with '/' in names ([#3687](https://github.com/Uninett/nav/issues/3687))
- Fixed bug where subnets were not selectable in the IPAM subnet allocator ([#3692](https://github.com/Uninett/nav/issues/3692))
- Fixed bug in SeedDB IP Device form where enter in a text field triggered an unwanted connectivity check ([#3694](https://github.com/Uninett/nav/issues/3694))
- Added success messages for JWT Token Create and Edit views


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-16) before upgrading.

Happy NAVing everyone!

