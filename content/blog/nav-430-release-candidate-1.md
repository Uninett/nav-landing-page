---
title: 'NAV 4.3.0 release candidate 1'
date: 2015-05-21T08:59:00.000+02:00
draft: false
url: /blog/2015/05/nav-430-release-candidate-1/
tags: 
- nav
- regular
- rc
---

We have a release candidate for NAV 4.3.0 ready to download for those who want an early peek.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.3/4.3.0). A new package for Debian Wheezy has been published in our APT repository, but in the “navbeta” archive instead of the regular “nav” archive - modify [the instructions](https://nav.uninett.no/wiki/nav_on_debian) accordingly (We have no packages for Debian Jessie yet, due to dependency problems and our own resource constraints).

We have also published a “beta” Virtual Appliance on our homepage, if you want to test the release candidate separately from your production install (remember, there is no downgrade path!)

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

*   [LP#1397257](https://bugs.launchpad.net/nav/+bug/1397257/) (Port Admin may not work properly for any non-HP and non-Cisco device)
*   [LP#1447973](https://bugs.launchpad.net/nav/+bug/1447973/) (CDP/LLDP neighbor matching fails when multiple ports match the identification)
*   [LP#1447999](https://bugs.launchpad.net/nav/+bug/1447999/) (Existing adjacency candidate data in db is not deleted if a device’s CDP cache or LLDP remote table becomes empty)
*   [LP#1448086](https://bugs.launchpad.net/nav/+bug/1448086/) (Unable to identify LLDP neighbor’s port in some instances)

Happy NAVing everyone!