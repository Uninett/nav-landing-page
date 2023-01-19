---
title: 'NAV 4.2.6 released'
date: 2015-04-23T06:18:00.000+02:00
draft: false
url: /blog/2015/04/nav-426-released/
tags: 
- bugfix
- nav
- regular
- 4.2
---

The sixth maintenance release of the NAV 4.2 series is now available.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.2/4.2.6). A new package for Debian Wheezy has been published in our [APT repository](https://nav.uninett.no/wiki/nav_on_debian), as usual.

Debian Jessie (the next stable release of Debian) is scheduled for release on Saturday 25th April, so we will start working on building a package for Jessie as well.

## Changes

The following 11 reported issues have been fixed:

Bugfixes:

*   [LP#1248083](https://bugs.launchpad.net/nav/+bug/1248083/) (The ipdevinfo “Affected” tab should be renamed to “what if”)
*   [LP#1248085](https://bugs.launchpad.net/nav/+bug/1248085/) (ipdevinfo “affected” tab needs to properly list the affected organizations)
*   [LP#1338388](https://bugs.launchpad.net/nav/+bug/1338388/) (Netmap link traffic does not always show)
*   [LP#1435451](https://bugs.launchpad.net/nav/+bug/1435451/) (Vendors report should only show Vendors in use)
*   [LP#1436125](https://bugs.launchpad.net/nav/+bug/1436125/) (No CPU graph from some Cisco CPUs)
*   [LP#1436388](https://bugs.launchpad.net/nav/+bug/1436388/) (VLAN number cannot be forced by router port description)
*   [LP#1437318](https://bugs.launchpad.net/nav/+bug/1437318/) (PostgreSQL load driven up by overzealous pruning of old ipdevpoll\_job\_log entries in NAV 4.2.5)
*   [LP#1438930](https://bugs.launchpad.net/nav/+bug/1438930/) (No negative values can be displayed in graphs)
*   [LP#1442538](https://bugs.launchpad.net/nav/+bug/1442538/) (Graphite-web doesn’t support metric aliases with non-ASCII characters)
*   [LP#1443775](https://bugs.launchpad.net/nav/+bug/1443775/) (alert templates for climate humidity notifications does not exist)
*   [LP#1444416](https://bugs.launchpad.net/nav/+bug/1444416/) (netmap L3 crash in urlresolvers.py)

Happy NAVing everyone!
