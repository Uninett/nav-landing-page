---
title: 'NAV 5.0.0 released'
date: 2019-11-07T12:26:00.000+01:00
draft: false
url: /blog/2019/11/nav-500-released/
tags:
- release
---

The first feature release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly

## Deprecation warning

Python 2 reaches its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

## User-visible features and improvements:

*   [#1793](https://github.com/Uninett/nav/issues/1793) (Add maintenance filter option to netbox API endpoint)
    *   [#1995](https://github.com/Uninett/nav/pull/1995) (Add maintenance filter to Netbox API endpoint)
*   [#1859](https://github.com/Uninett/nav/pull/1859) (Improve portadmin support for dot1x)
*   [#1905](https://github.com/Uninett/nav/pull/1905) (Add support for alcatel DDM-sensors)
*   [#1908](https://github.com/Uninett/nav/issues/1908) (Add display widget for binary/boolean sensors to "racks")
*   [#1919](https://github.com/Uninett/nav/issues/1919) (Add support for external sensors from newer Watchdog products)

*   [#1926](https://github.com/Uninett/nav/pull/1926) (Add support for most external sensors on newer watchdog products)

*   [#1930](https://github.com/Uninett/nav/pull/1930) (Refactor IT-WATCHDOGS-MIB MibRetriever implementations)
*   [#1943](https://github.com/Uninett/nav/pull/1943) (Improve support for boolean sensors in racks)
*   [#1947](https://github.com/Uninett/nav/pull/1947) (Management profiles)
*   [#1969](https://github.com/Uninett/nav/pull/1969) (Store local chassis ids from LLDP-MIB and use for neighbor lookups)
*   [#1970](https://github.com/Uninett/nav/pull/1970) (Add API for management profiles)
*   [#1971](https://github.com/Uninett/nav/issues/1971) (Provide option to automatically enable CDP on voice ports)

*   [#1974](https://github.com/Uninett/nav/pull/1974) (enabling CDP when a voice port is set using portadmin)

*   [#1987](https://github.com/Uninett/nav/pull/1987) (Refactor power supply and fan monitoring functionality)
*   [#1988](https://github.com/Uninett/nav/pull/1988) (Add status monitoring for Juniper PSUs and FANs)
*   [#1989](https://github.com/Uninett/nav/pull/1989) (Collect optical sensor measurements from Coriant Groove devices)
*   [#1998](https://github.com/Uninett/nav/pull/1998) (Remove support for alert dispatching over Jabber)
*   [#2002](https://github.com/Uninett/nav/pull/2002) (Refactor installation documentation.)
*   [#2005](https://github.com/Uninett/nav/pull/2005) (Export stream of serialized alerts from the event engine)
*   [#2007](https://github.com/Uninett/nav/pull/2007) (Support REMOTE\_USER header for web authentication)
*   [#2008](https://github.com/Uninett/nav/pull/2008) (Add more database stats to Watchdog's "NAV by the numbers")

## Fixed GitHub issues in this release:

*   [#1978](https://github.com/Uninett/nav/pull/1978) (Netmap layer 2 traffic data requests to Graphite are too slow and too large)
*   [#1979](https://github.com/Uninett/nav/issues/1979) (Location alerts widget crashes intermittently)
*   [#1980](https://github.com/Uninett/nav/issues/1980) (Using the wrong Radius dictionary file can cause servicemon to eat all available system memory and hang)
*   [#1984](https://github.com/Uninett/nav/issues/1984) (Blank sysnames should not be allowed)
    *   [#1985](https://github.com/Uninett/nav/pull/1985) (Disallow blank sysnames)
*   [#1990](https://github.com/Uninett/nav/pull/1990) (Make type changes immediately when unknown types are encountered)
*   [#2004](https://github.com/Uninett/nav/issues/2004) (\[BUG\] Interface browser shows wrong "last used" date)
*   [#2009](https://github.com/Uninett/nav/pull/2009) (Ensure rooms require a location attribute also in the SQL schema)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!
