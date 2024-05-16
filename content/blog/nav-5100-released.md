---
title: 'NAV 5.10.0 released'
date: 2024-05-16T15:50:00.000+01:00
draft: false
tags:
- release
---

The first feature release of the 5.10 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Do note that 5.10 is the **last series we will package for Debian 11**, as NAV
5.11 will drop support for Python versions older than 3.9

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Removed

- Removed references to IRC support channel from documentation, as the channel
  is closing down ([#2907](https://github.com/Uninett/nav/issues/2907))

## Deprecated

- Support for Python versions older than 3.9 will be dropped in NAV 5.11.

## Added

- New ipdevpoll plugin to fetch ARP cache data from Palo Alto firewall APIs
  ([#2613](https://github.com/Uninett/nav/issues/2613))
- Introduced `towncrier` to aid in collaborative NAV changelog authoring
  ([#2869](https://github.com/Uninett/nav/issues/2869))
- Add library utilities to produce QR codes to arbitrary URLs, for use in
  upcoming features ([#2887](https://github.com/Uninett/nav/issues/2887))

## Changed

- Change the Docker Compose-based development environment to use more build
  caching and avoid running too many things as root
  ([#2859](https://github.com/Uninett/nav/issues/2859))
- Changed required PostgreSQL version to 11

## Fixed

- Avoid running command line scripts twice on every invocation
  ([#2877](https://github.com/Uninett/nav/issues/2877),
  [#2878](https://github.com/Uninett/nav/pull/2878))
- Fixed `full-nav-restore.sh` developer helper script that broke after Docker
  Compose development was reorganized
  ([#2888](https://github.com/Uninett/nav/issues/2888))
- Fix missing delete icon in form selector labels
  ([#2898](https://github.com/Uninett/nav/issues/2898))
 
## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-10) before upgrading.

Happy NAVing everyone!

