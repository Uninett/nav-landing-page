---
title: 'NAV 5.17.0 released'
date: 2026-02-13T12:49:17+01:00
draft: false
tags:
- release
---

The first feature release of the 5.17 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm), 11 (Bullseye) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

Please be sure to check the [release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-17) before upgrading, as there may be recommended changes to your config files.

## Security

- Enable CSRF protection in entire NAV web UI ([#3395](https://github.com/Uninett/nav/issues/3395))

## Added

- DHCP usage statistics graphs are now shown on VLAN and prefix pages when found in Graphite ([#2373](https://github.com/Uninett/nav/issues/2373))
- Added "more than" / "less than" option to the "Last Seen" filter on the Room view interface list ([#3313](https://github.com/Uninett/nav/issues/3313))
- Added hyperlink to management profile options in SeedDB netbox form ([#3643](https://github.com/Uninett/nav/issues/3643))
- Added browse tree and description search for easier maintenance task component selection ([#3778](https://github.com/Uninett/nav/issues/3778))
- Added support for SNMP v3-based CAM data collection on Cisco switches (Adds support for SNMP v3 context switching for logical MIB instances) ([#2811](https://github.com/Uninett/nav/issues/2811))
- Added script to generate GitHub, blog and e-mail release announcements from `CHANGELOG.md`

## Changed

- Finally switched from NAV's homegrown authentication system to Django's own. This makes NAV compatible with a lot of 3rd party libraries, and is a necessary step to support MFA.

  This is a big change. Test thoroughly before putting this version into
  production. This is especially important if you have configured `REMOTE_USER`
  authentication.  NAV's classic `REMOTE_USER` support has a lot of bells and
  whistles that Django's support lacks. We have added support for NAV's config
  options but it is a little used feature. There should be no need to update
  the confg file.  ([#3626](https://github.com/Uninett/nav/issues/3626))
- Allow users to set a subscribed dashboard as their default ([#3572](https://github.com/Uninett/nav/issues/3572))
- Refactored `dhcpstats` backend. Users beware: option `user_context_poolname_key` in `dhcpstats.conf` renamed to `user_context_groupname_key` and its default value changed from `name` to `group`.  ([#3766](https://github.com/Uninett/nav/issues/3766))
- Upgraded jQuery library to version 4 ([#3730](https://github.com/Uninett/nav/issues/3730))
- Upgraded Marionette to V4 in the IPAM tool ([#1873](https://github.com/Uninett/nav/issues/1873))
- Refactored dashboard navlets to use HTMX for rendering and updates ([#3635](https://github.com/Uninett/nav/issues/3635))
- Stopped CI testing on Python 3.12 by default ([#3741](https://github.com/Uninett/nav/issues/3741))

## Fixed

- Re-enabled sorting by actor in auditlog table, now actually working robustly! ([#3581](https://github.com/Uninett/nav/issues/3581))
- Fixed breadcrumbs missing from JWT Create and Edit frontend pages ([#3682](https://github.com/Uninett/nav/issues/3682))
- Fixed bug where Netmap views could not be created or updated ([#3737](https://github.com/Uninett/nav/pull/3737))
- Ensure that the auditlog entries for deleting accounts behave like other entries. ([#3738](https://github.com/Uninett/nav/issues/3738))
- Fixed IP Device select in Add New Service form ([#3749](https://github.com/Uninett/nav/issues/3749))
- Filtering on SeedDB Patch and Cable pages now searches all visible columns instead of only the `jack` field ([#3760](https://github.com/Uninett/nav/issues/3760))
- Popover arrow is now correctly positioned when aligned to the end ([#3770](https://github.com/Uninett/nav/issues/3770))
- Fix bug where Getting Started tour does not highlight the correct element ([#3771](https://github.com/Uninett/nav/issues/3771))
- PortAdmin's save feedback modal now appears instantly instead of being delayed by a network round-trip ([#3772](https://github.com/Uninett/nav/issues/3772))
- Add global CSRF token handlers for all HTMX and jQuery AJAX POST requests, to ensure things do not break unintentionally when CSRF validation is enabled
- Fixed a crash in `nav config where` when no config file directory could be found

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-17) before upgrading.

Happy NAVing everyone!
