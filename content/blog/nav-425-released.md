---
title: 'NAV 4.2.5 released'
date: 2015-03-23T02:19:00.000+01:00
draft: false
url: /blog/2015/03/nav-425-released/
tags: 
- bugfix
- 4.2
---

The fifth maintenance release of the NAV 4.2 series is now available.

This replaces the 4.2.4 release, which broke the parallel pinger, and possibly other event-posting components. Again, to those who already upgraded to 4.2.4, we apologize for the inconvenience. More details at the bug report here:

[https://bugs.launchpad.net/nav/+bug/1434520](https://bugs.launchpad.net/nav/+bug/1434520)

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.2/4.2.5). A new package for Debian Wheezy has been published in our [APT repository](https://nav.uninett.no/wiki/nav_on_debian), as usual.

*   [LP#1403365](https://bugs.launchpad.net/nav/+bug/1403365/) (offMaintenance alerts for same device every 5 minutes)
*   [LP#1422298](https://bugs.launchpad.net/nav/+bug/1422298/) (device history crashes when viewing weathergoose events)
*   [LP#1422316](https://bugs.launchpad.net/nav/+bug/1422316/) (thresholdmon AttributeError crash)
*   [LP#1425536](https://bugs.launchpad.net/nav/+bug/1425536/) (Status widget error when filtering on Device group)
*   [LP#1425846](https://bugs.launchpad.net/nav/+bug/1425846/) (alert profiles does not display without refresh)
*   [LP#1427666](https://bugs.launchpad.net/nav/+bug/1427666/) (watchdog is slow)
*   [LP#1428071](https://bugs.launchpad.net/nav/+bug/1428071/) (Portadmin crashes when searching by sysname or ip)
*   [LP#1428578](https://bugs.launchpad.net/nav/+bug/1428578/) (seeddb test for snmp version crashes if neither v1 or v2c is supported)
*   [LP#1429868](https://bugs.launchpad.net/nav/+bug/1429868/) (ipdevpoll jobs that are no longer supposed to run for a device as flagged as “overdue”)
*   [LP#1430795](https://bugs.launchpad.net/nav/+bug/1430795/) (SeedDB room edit form asks for user’s location, shows no map until permission is given)
*   [LP#1430797](https://bugs.launchpad.net/nav/+bug/1430797/) (Geomap shows no map at all when no room positions are defined)
*   [LP#1430802](https://bugs.launchpad.net/nav/+bug/1430802/) (SeedDB room edit insists on inserting a geoposition)
*   [LP#1430803](https://bugs.launchpad.net/nav/+bug/1430803/) (SeedDB room form position indicator icon is missing)
*   [LP#1431780](https://bugs.launchpad.net/nav/+bug/1431780/) (Trunk port status is never reset on non-Cisco equipment)
*   [LP#1432056](https://bugs.launchpad.net/nav/+bug/1432056/) (mod\_wsgi option WSGIApplicationGroup should be %{GLOBAL} by default)
*   [LP#1432057](https://bugs.launchpad.net/nav/+bug/1432057/) (\[appliance\] missing python-dnspython)
*   [LP#1432620](https://bugs.launchpad.net/nav/+bug/1432620/) (Unable to load Netmap layer 3 map with ELINK peers)
*   [LP#1432682](https://bugs.launchpad.net/nav/+bug/1432682/) (Should be able to specify exact subnet prefixes to ignore)
*   [LP#1433063](https://bugs.launchpad.net/nav/+bug/1433063/) (netmap zoom and pan does not work for some views)
*   [LP#1433120](https://bugs.launchpad.net/nav/+bug/1433120/) (Shouldn’t generate linkState alerts for intentionally shutdown interfaces)

Happy NAVing everyone!
