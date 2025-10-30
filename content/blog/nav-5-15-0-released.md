---
title: 'NAV 5.15.0 released'
date: 2025-10-30T15:09:28+0100
draft: false
tags:
- release
---

The first feature of the 5.15 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Security

- In preparation for properly protecting against CSRF attacks throughout NAV:
  - Added CSRF tokens to AJAX POST requests ([#3465](https://github.com/Uninett/nav/issues/3465))
  - Removed CSRF tokens from GET requests ([#3472](https://github.com/Uninett/nav/issues/3472))

## Removed

- Removed unused vendored Foundation CSS stylesheets ([#3479](https://github.com/Uninett/nav/issues/3479))
- Removed vendored Foundation JavaScript library from codebase ([#3542](https://github.com/Uninett/nav/issues/3542))

## Added

- Show VLAN netident in ipdevinfo port list ([#2160](https://github.com/Uninett/nav/issues/2160))
- Dashboards are now shareable between users ([#2344](https://github.com/Uninett/nav/issues/2344))
- Show device MAC address in the Device Info tab of ipdevinfo ([#3222](https://github.com/Uninett/nav/issues/3222))
- Added Django 5.2 and Python 3.13 to default test matrix ([#3467](https://github.com/Uninett/nav/issues/3467))
- Improved user feedback in PortAdmin by loading live port details in background, after initial page load ([#3544](https://github.com/Uninett/nav/issues/3544))
- Added search results preview in navbar ([#3577](https://github.com/Uninett/nav/issues/3577))
- Documented how to enable IPv6 connectivity inside devcontainer (Docker)

## Changed

- Updated NAPALM dependency to 5.1.0 ([#3495](https://github.com/Uninett/nav/issues/3495))
- Replaced SeedDB IP Device "check connectivity" JavaScript with HTMX, including improved user feedback ([#3560](https://github.com/Uninett/nav/issues/3560))

### Non-visible and developer-centric changes

- The dated Foundation JavaScript libraries and CSS stylesheets are being replaced by a combination of HTMX-based features, new internal libraries and newer alternative libraries. The goal is to keep the outward user interface more or less unchanged:

  - Use HTMX modals in SeedDB Patch tool ([#3461](https://github.com/Uninett/nav/issues/3461))
  - Replaced tooltip in status actions with accessible help text toggle ([#3463](https://github.com/Uninett/nav/issues/3463))
  - Replaced Foundation Joyride with `Driver.js` implementation ([#3468](https://github.com/Uninett/nav/issues/3468))
  - Replaced Foundation Topbar JS with JQuery ([#3476](https://github.com/Uninett/nav/issues/3476))
  - Replaced Foundation Equalizer with JQuery ([#3477](https://github.com/Uninett/nav/issues/3477))
  - Replaced foundation alert plugin with custom JavaScript ([#3481](https://github.com/Uninett/nav/issues/3481))
  - Replaced native tooltips with NAV tooltips ([#3482](https://github.com/Uninett/nav/issues/3482))
  - Replaced navlet modals with HTMX implementation ([#3487](https://github.com/Uninett/nav/issues/3487))
  - Replaced search hint modals in Radius tool with HTMX ([#3494](https://github.com/Uninett/nav/issues/3494))
  - Replaced radius detail modals with HTMX ([#3514](https://github.com/Uninett/nav/issues/3514))
  - Added fit-content size to modals to support large content
  - Replace IPAM subnet diagram help modal with HTMX
  - Replaced "about logging" modal with HTMX
  - Replaced Foundation dropdowns with custom implementation
  - Replaced "import dashboard" modal with HTMX
  - Replaced Machine Tracker modals with HTMX
  - Replaced modals in ipdevinfo tool with HTMX
  - Replaced threshold form help modal with HTMX
  - Added custom NAV tooltip as replacement for Foundation JS ([#3449](https://github.com/Uninett/nav/issues/3449))
  - Added reusable HTMX modal utilities and styles ([#3461](https://github.com/Uninett/nav/issues/3461))
  - Added modal closing behaviour controls for close button visibility and outside click handling ([#3537](https://github.com/Uninett/nav/issues/3537))
  - Added support for positioning popover on multiple sides ([#3550](https://github.com/Uninett/nav/issues/3550))
  - Replaced feedback modal in Portadmin with HTMX ([#3540](https://github.com/Uninett/nav/issues/3540))
  - Replaced Foundation dropdowns with popovers ([#3531](https://github.com/Uninett/nav/issues/3531))
  - Upgraded tinysort dependency ([#3580](https://github.com/Uninett/nav/issues/3580))
  - Replaced Foundation Clearing Lightbox with custom Lightbox plugin for room/location picture gallery ([#3530](https://github.com/Uninett/nav/issues/3530))
  - Use fixed position tooltips in status widgets and SeedDB list tree ([#3576](https://github.com/Uninett/nav/issues/3576))
  - Added support for controlling popovers with client side events ([#3578](https://github.com/Uninett/nav/issues/3578))
  - Replaced outdated timepicker library with flatpickr ([#3587](https://github.com/Uninett/nav/issues/3587))

- Modernized Django URL config, mostly by replacing usage of `re_path()` with `path()` ([#3515](https://github.com/Uninett/nav/issues/3515), ([#3548](https://github.com/Uninett/nav/issues/3548), ([#3631](https://github.com/Uninett/nav/issues/3631))

## Fixed

- Protect against unexpected NUL bytes in SNMP strings by stripping them ([#2479](https://github.com/Uninett/nav/issues/2479))
- Fixed bug where status widget tooltip gets stuck ([#3301](https://github.com/Uninett/nav/issues/3301))
- Show friendly error message in Arnold when attempting to block ports on switches that do not feature a writeable management profile ([#3383](https://github.com/Uninett/nav/issues/3383))
- Fixed bug where ipdevinfo job refresh does not display error messages properly ([#3385](https://github.com/Uninett/nav/issues/3385))
- Made it possible to un-revoke JWT refresh token by recreating the token ([#3457](https://github.com/Uninett/nav/issues/3457))
- Fixed broken all-time searches in Radius tool ([#3500](https://github.com/Uninett/nav/issues/3500))
- Removed "no racks" alert after adding a new rack to a room ([#3506](https://github.com/Uninett/nav/issues/3506))
- Show distinct filter groups in Groups and Permissions modal in Alert Profiles ([#3523](https://github.com/Uninett/nav/issues/3523))
- Show errors on invalid IP in Network Explorer search ([#3534](https://github.com/Uninett/nav/issues/3534))
- Fixed saving rooms/locations with active alerts widgets after editing ([#3561](https://github.com/Uninett/nav/issues/3561))
- Fixed sudo-ing to the default (anonymous) account ([#3571](https://github.com/Uninett/nav/issues/3571))
- Fixed PortAdmin bug where restarting interfaces fails ([#3589](https://github.com/Uninett/nav/issues/3589))
- Fixed tooltips in Device History and Subnet Matrix tools ([#3591](https://github.com/Uninett/nav/issues/3591))
- Enabled GetBulk / bulkwalk operations under synchronous SNMP v3 communication (enormously speeding up PortAdmin SNMPv3 queries) ([#3594](https://github.com/Uninett/nav/issues/3594))
- Adjusted size and position of "close modal" icon to avoid overlap with text
- Fixed bug where QR Code button is not clickable

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-15) before upgrading.

Happy NAVing everyone!

