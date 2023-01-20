---
title: 'NAV 4.2.2 released'
date: 2015-01-09T02:24:00.000+01:00
draft: false
url: /blog/2015/01/nav-422-released/
tags: 
- bugfix
- nav
- regular
- 4.2
---

The second maintenance release of the NAV 4.2 series is now available.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.2/4.2.2). A new package for Debian Wheezy has been published in our [APT repository](https://nav.uninett.no/wiki/nav_on_debian), as usual.

## Changes

**Important note:**

_This release adds commas to the list of characters escaped in Graphite metric names, which may change the name used for some of your existing metrics after an upgrade. If you want to keep your data, the underlying files need to be renamed manually in your Graphite installation. See the updated [release notes](https://nav.uninett.no/doc/4.2/release-notes.html#nav-4-2) for more details._

The following 23 reported issues have been fixed:

*   [LP#1169559](https://bugs.launchpad.net/nav/+bug/1169559/) (Print button for Netmap)
*   [LP#1394522](https://bugs.launchpad.net/nav/+bug/1394522/) (Netbox and Location bulk import formats must be changed to include data attributes)
*   [LP#1396913](https://bugs.launchpad.net/nav/+bug/1396913/) (Status page, filter on Device Group)
*   [LP#1396920](https://bugs.launchpad.net/nav/+bug/1396920/) (NAV 4, Internet Explorer Compatibility mode)
*   [LP#1396924](https://bugs.launchpad.net/nav/+bug/1396924/) (NAV 4.2 does not work with SASS 3.4 or newer, but the install docs do not specify this)
*   [LP#1397255](https://bugs.launchpad.net/nav/+bug/1397255/) (Subject text of psuDown alerts in status tool is non- descriptive)
*   [LP#1397886](https://bugs.launchpad.net/nav/+bug/1397886/) (device history script timeout on many results)
*   [LP#1398382](https://bugs.launchpad.net/nav/+bug/1398382/) (AssertionError prevents Netmap from loading any graph/map)
*   [LP#1398791](https://bugs.launchpad.net/nav/+bug/1398791/) (Maintenance system stops working when an IP device on maintenance is deleted)
*   [LP#1398815](https://bugs.launchpad.net/nav/+bug/1398815/) (Rooms, hyperlink inconsistensies between report and seeddb)
*   [LP#1399558](https://bugs.launchpad.net/nav/+bug/1399558/) (portadmin tries to write to memory for each change)
*   [LP#1400307](https://bugs.launchpad.net/nav/+bug/1400307/) (Need easier way to remove services)
*   [LP#1401114](https://bugs.launchpad.net/nav/+bug/1401114/) (dropdown for ipdevice when adding a service is fubar)
*   [LP#1401470](https://bugs.launchpad.net/nav/+bug/1401470/) (ipdevpoll TypeError: unsupported operand type(s) for +: ‘NoneType’ and 'float’)
*   [LP#1403066](https://bugs.launchpad.net/nav/+bug/1403066/) (Some routers fail to expand in Network Explorer)
*   [LP#1403432](https://bugs.launchpad.net/nav/+bug/1403432/) (report.conf, wrong url for netboxinfo)
*   [LP#1403797](https://bugs.launchpad.net/nav/+bug/1403797/) (Geomap is insanely slow after migration to Graphite in NAV 4.0)
*   [LP#1403803](https://bugs.launchpad.net/nav/+bug/1403803/) (Geomap “loading data” indicator is missing)
*   [LP#1403884](https://bugs.launchpad.net/nav/+bug/1403884/) (geomap sends data request on every tiny movement)
*   [LP#1404207](https://bugs.launchpad.net/nav/+bug/1404207/) (Intermittent ValueErrors thrown from pynetsnmp causes ipdevpoll jobs to fail)
*   [LP#1404222](https://bugs.launchpad.net/nav/+bug/1404222/) (Conflicting sysnames cause ipdevpoll jobs to crash)
*   [LP#1404225](https://bugs.launchpad.net/nav/+bug/1404225/) (Multiple DNS PTR records for the same IP address causes sysname to swing back and forth in NAV)
*   [LP#1407625](https://bugs.launchpad.net/nav/+bug/1407625/) (/search/devicegroup takes too long)

Happy NAVing everyone!
