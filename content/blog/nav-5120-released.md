---
title: 'NAV 5.12.0 released'
date: 2024-12-16T14:50:00.000+01:00
draft: false
tags:
- release
---

The first feature release of the 5.12 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Removed

- Removed dependencies django-crispy-forms and crispy-forms-foundation ([#2794](https://github.com/Uninett/nav/issues/2794))

## Added

- Active maintenance tasks that only reference deleted components will be automatically cancelled ([#3229](https://github.com/Uninett/nav/issues/3229))
- Alert profiles filter match value dropdowns now support interactive value searches ([#3238](https://github.com/Uninett/nav/issues/3238))
- Added support for setting access port VLANs for Cisco Small Business switches in PortAdmin (by reverting to non-Cisco-specific handler routines for this subgroup of products) ([#3249](https://github.com/Uninett/nav/issues/3249))

## Changed

- Switched to building CSS from Sass using webpack instead of deprecated `libsass`. ([#2849](https://github.com/Uninett/nav/issues/2849))
- Run tests using tox version 4 ([#2973](https://github.com/Uninett/nav/issues/2973))
- The ipdevpoll plugin to fetch ARP cache data from a netbox's Palo Alto firewall API is now configured through a new management profile type assigned to that netbox ([#3147](https://github.com/Uninett/nav/issues/3147))
- The old-style `setup.py` script was removed and installation docs were updated ([#3176](https://github.com/Uninett/nav/issues/3176))
- Ensure that CSRF token info is included in all forms that have been refactored to remove the `django-crispy-forms` dependency ([#3157](https://github.com/Uninett/nav/issues/3157))

## Fixed

- Alert profiles filter match value dropdowns now support more than the old hard limit of 1000 choices ([#2908](https://github.com/Uninett/nav/issues/2908))
- Disable deletion of the default dashboard ([#3150](https://github.com/Uninett/nav/issues/3150))
- Rooms and locations with periods in their IDs can now be properly retrieved from the corresponding API endpoints ([#3186](https://github.com/Uninett/nav/issues/3186))
- Fix spurious crashing when loading some Netmap layer 3 views ([#3225](https://github.com/Uninett/nav/issues/3225))
- Improve description of deleted maintenance components ([#3228](https://github.com/Uninett/nav/issues/3228))
- Stop SNMP-based `arp` plugin from stepping on the `paloaltoarp` plugins toes.  Note that this **requires** updating the plugin order in the `ip2mac` job in `ipdevpoll.conf` ([#3252](https://github.com/Uninett/nav/issues/3252))
- Ensure that each account has exactly one default dashboard

 
## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-12) before upgrading.

Happy NAVing everyone!

