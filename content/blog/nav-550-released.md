---
title: 'NAV 5.5.0 released'
date: 2022-11-04T13:06:00.000+02:00
draft: false
url: /blog/2022/11/nav-550-released/
---

The initial feature release of the 5.5 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

Changed
-------

*   Bump <code>lxml</code> from 4.6.5 to 4.9.1 in /tests ([#2443](https://github.com/Uninett/nav/pull/2443))
*   Links and documented references to the NAV mailing lists have changed to the `lister.sikt.no` domain.

Added
-------

*   Add link to #nav irc channel on Libera.Chat to README file ([#2475](https://github.com/Uninett/nav/pull/2475))
*   Add `mac_addresses` attribute to `/netbox/` API endpoint ([#2487](https://github.com/Uninett/nav/pull/2487), [#2490](https://github.com/Uninett/nav/pull/2490))
*   Add ability to filter by alert severity in the status tool ([#2467](https://github.com/Uninett/nav/pull/2467))
*   Support for fetching ARP cache entries from all Arista VRF instances ([#2262](https://github.com/Uninett/nav/issues/2262), [#2454](https://github.com/Uninett/nav/pull/2454)))
*   Link aggregation information added to NAV API ([#1765](https://github.com/Uninett/nav/issues/1765), [#2440](https://github.com/Uninett/nav/pull/2440))
*   Support fetching memory stats from `CISCO-ENHANCED-MEMPOOL-MIB` ([#2236](https://github.com/Uninett/nav/issues/2236), [#2439](https://github.com/Uninett/nav/pull/2439))
*   Added a flag to `navcheckservice` that shows all available handler plugins ([#2378](https://github.com/Uninett/nav/issues/2378), [#2437](https://github.com/Uninett/nav/pull/2437))
*   Post `deviceHwUpgrade`/`deviceSwUpgrade`/`deviceFwUpgrade` events when changes are detected to devices' hardware, software or firmware revisions ([#2393](https://github.com/Uninett/nav/issues/2393), [#2413](https://github.com/Uninett/nav/pull/2413))
*   Call a `cleanup()` method for individual container objects after ipdevpoll save stage ([#2421](https://github.com/Uninett/nav/pull/2421))
*   Added `Device` methods to resolve and return related objects/entities (chassis, modules, fans, power supplied) and extended device descriptions ([#2428](https://github.com/Uninett/nav/pull/2428))

Fixed
-------

*   Avoid potential resource leaks by properly closing configuration files after reading them ([#2451](https://github.com/Uninett/nav/pull/2451))
*   Geomap "link to this configuration" now actually opens the correct location at the correct zoom level ([#2412](https://github.com/Uninett/nav/issues/2412), [#2488](https://github.com/Uninett/nav/pull/2488))
*   snmptrapd can now identify an SNMP agent from any of its interface addresses ([#2387](https://github.com/Uninett/nav/issues/2387), [#2461](https://github.com/Uninett/nav/pull/2461))
*   PortAdmin now ignores incorrectly configured VLAN tags (tagged as `NA`) on Juniper switches, instead of crashing ([#2452](https://github.com/Uninett/nav/issues/2452), [#2453](https://github.com/Uninett/nav/pull/2453))
*   Fix potential ipdevpoll crashes due to database fetches in wrong thread ([#2478](https://github.com/Uninett/nav/issues/2478), [#2480](https://github.com/Uninett/nav/pull/2480))
*   Handle Graphite connection issues gracefully in ranked statistics page ([#2459](https://github.com/Uninett/nav/pull/2459))
*   Handle Graphite connection issues gracefully in device group detail page ([#2345](https://github.com/Uninett/nav/issues/2345), [#2434](https://github.com/Uninett/nav/pull/2434))
*   Removed needless carbon data chunking from `activeipcollector` ([#1696](https://github.com/Uninett/nav/issues/1696), [#2462](https://github.com/Uninett/nav/pull/2462))
*   Evaluate `0.0` as a valid numeric metric value during threshold rule evaluations ([#2447](https://github.com/Uninett/nav/issues/2447)
*   Updated dead links in Geomap documentation ([#2419](https://github.com/Uninett/nav/pull/2419))
*   Link from IPAM to reserve prefixed in SeedDB now works again ([#2410](https://github.com/Uninett/nav/issues/2410), [#2422](https://github.com/Uninett/nav/pull/2422))
*   Improved inefficient database queries in Arnold ([#2425](https://github.com/Uninett/nav/pull/2425))
*   Updated tox examples in hacking documentation ([#2427](https://github.com/Uninett/nav/issues/2427), [#2430](https://github.com/Uninett/nav/pull/2430))
*   Fixed an `AttributeError` crash bug in the `naventity` command line program ([#2433](https://github.com/Uninett/nav/issues/2433), [#2444](https://github.com/Uninett/nav/pull/2444))

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.5.x/release-notes.html#nav-5-5) before upgrading.

Happy NAVing everyone!
