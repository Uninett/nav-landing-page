---
title: 'NAV 5.13.0 released'
date: 2025-03-07T10:29:00+01:00
draft: false
tags:
- release
---

The first feature release of the 5.13 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 12 (Bookworm) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian).

Please be extra aware of config file changes, especially in
`ipdevpoll.conf`. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure
to update your running config.

## Security

- Omit Palo Alto API keys from ARP plugin log output ([#3251](https://github.com/Uninett/nav/issues/3251))

## Added

- Add option for showing OUI vendor name in Machine Tracker searches ([#3292](https://github.com/Uninett/nav/issues/3292))
- Add cronjob for populating database with OUI data nightly ([#3320](https://github.com/Uninett/nav/issues/3320))
- Run test suite by default on Python 3.11 and Django 4.2 ([#2850](https://github.com/Uninett/nav/issues/2850))
- Added tests for device history search ([#3261](https://github.com/Uninett/nav/issues/3261))

## Changed

- Upgraded Django requirement to 4.2 ([#2789](https://github.com/Uninett/nav/issues/2789))
- Upgraded and cleaned up various Docker environments used for development and testing to Debian Bookworm / Python 3.11 ([#3284](https://github.com/Uninett/nav/issues/3284))

## Fixed

- Fix minor incompatibilities with Django 4.2 ([#2850](https://github.com/Uninett/nav/issues/2850))
- Fixed non-responsive search function in room map widget ([#3207](https://github.com/Uninett/nav/issues/3207))
- Validate interval inputs in several search forms to avoid unhandled overflow errors (switch port activity, radius top talkers report, radius error log search, radius account log search) ([#3242](https://github.com/Uninett/nav/issues/3242), [#3245](https://github.com/Uninett/nav/issues/3245), [#3246](https://github.com/Uninett/nav/issues/3246), [#3247](https://github.com/Uninett/nav/issues/3247))
- Verify that multiple quarantine rules cannot be added with identical VLANs in Arnold ([#3244](https://github.com/Uninett/nav/issues/3244))
- Fixed broken module history view in device history ([#3258](https://github.com/Uninett/nav/issues/3258))
- Stop sending error mails to site admins from graphite-web proxy endpoint when graphite response code is in the 5XX range ([#3259](https://github.com/Uninett/nav/issues/3259))
- Ignore case of sysname in IP device info ([#3262](https://github.com/Uninett/nav/issues/3262))
- Add user-agent header when downloading OUI text file ([#3291](https://github.com/Uninett/nav/issues/3291))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-13) before upgrading.

Happy NAVing everyone!

