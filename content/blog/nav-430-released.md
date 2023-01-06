---
title: 'NAV 4.3.0 released'
date: 2015-06-12T01:23:00.000+02:00
draft: false
url: /blog/2015/06/nav-430-released/
tags: 
- 4.3
- nav
- regular
---

The initial 4.3 series release of NAV is now out, with only minor changes and some bugfixes since the release candidate. A big thanks to those who helped test the release candidate!

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.3/4.3.0). A new package for Debian Wheezy has been published in our [APT repository](https://nav.uninett.no/wiki/nav_on_debian) as usual (We have no packages for Debian Jessie yet, due to dependency problems and our own resource constraints).

The virtual appliance download has also been updated.

### Changes

This release makes some fundamental changes to NAV’s data model to improve support for non-physical devices (like Cisco VSS and Cisco VDC). Please read [the release notes](https://nav.uninett.no/doc/4.3/release-notes.html#nav-4-3) for further information.

User-visible features and improvements:

*   [LP#744943](https://bugs.launchpad.net/nav/+bug/744943/) (Add switch to toggle display of traffic lines in Geomap)
*   [LP#961212](https://bugs.launchpad.net/nav/+bug/961212/) (Show planned/active maintenance tasks for device in IP Device Info)
*   [LP#1149160](https://bugs.launchpad.net/nav/+bug/1149160/) (Auto-recognize HTTP URLs in reports and hyperlink them)
*   [LP#1166695](https://bugs.launchpad.net/nav/+bug/1166695/) (PortAdmin available from the toolbox)
*   [LP#1169550](https://bugs.launchpad.net/nav/+bug/1169550/) (NAV’s data model should reflect modern reality, with virtual device support)
*   [LP#1242872](https://bugs.launchpad.net/nav/+bug/1242872/) (Option to turn off traffic stats in Geomap)
*   [LP#1248081](https://bugs.launchpad.net/nav/+bug/1248081/) (New interface/tool to browse unrecognized neighbors)
*   [LP#1366895](https://bugs.launchpad.net/nav/+bug/1366895/) (Report widget)
*   [LP#1421644](https://bugs.launchpad.net/nav/+bug/1421644/) (Support Weathergoose traps from external temperature sensors)

Bugfixes:

*   [LP#1233093](https://bugs.launchpad.net/nav/+bug/1233093/) (Report pages crash under psycopg2 >= 2.5)
*   [LP#1397257](https://bugs.launchpad.net/nav/+bug/1397257/) (Port Admin may not work properly for any non-HP and non-Cisco device)
*   [LP#1447973](https://bugs.launchpad.net/nav/+bug/1447973/) (CDP/LLDP neighbor matching fails when multiple ports match the identification)
*   [LP#1447999](https://bugs.launchpad.net/nav/+bug/1447999/) (Existing adjacency candidate data in db is not deleted if a device’s CDP cache or LLDP remote table becomes empty)
*   [LP#1448086](https://bugs.launchpad.net/nav/+bug/1448086/) (Unable to identify LLDP neighbor’s port in some instances)
*   [LP#1458826](https://bugs.launchpad.net/nav/+bug/1458826/) (1minstats job crashes on invalid ENTITY-MIB references from CISCO-PROCESS-MIB)
*   [LP#1459138](https://bugs.launchpad.net/nav/+bug/1459138/) (Ignore Cisco reserved VLANs when collecting BRIDGE-MIB data)
*   [LP#1463724](https://bugs.launchpad.net/nav/+bug/1463724/) (Increase frequency of module status verification)

Happy NAVing everyone!