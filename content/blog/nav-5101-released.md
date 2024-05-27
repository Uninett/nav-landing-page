---
title: 'NAV 5.10.1 released'
date: 2024-05-27T13:45:00.000+01:00
draft: false
tags:
- release
---

The first maintenance release of the 5.10 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Do note that 5.10 is the **last series we will package for Debian 10**, as NAV
5.11 will drop support for Python versions older than 3.9

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

- Fix Machine Tracker DNS search crashing from exhausting all available file
  descriptors ([#2669](https://github.com/Uninett/nav/issues/2669))
- ARP records of unreachable devices are now closed by `navclean` cron job at
  configurable expiry intervals, rather than immediately as a response to a
  short ICMP packet loss ([#2913](https://github.com/Uninett/nav/issues/2913))
- Palo Alto API XML responses are now parsed based on keys instead of indexes
  ([#2924](https://github.com/Uninett/nav/issues/2924))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-10) before upgrading.

Happy NAVing everyone!
