---
title: 'NAV 4.8.0 released'
date: 2017-11-24T08:19:00.000+01:00
draft: false
url: /blog/2017/11/the-initial-feature-release-of-4/
---

The initial feature release of the 4.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 8/9 (Jessie/Stretch) have, unfortunately, NOT been built yet, due to unforeseen difficulties with our new build routine. They will hopefully be published in our [APT repository](https://nav.uninett.no/install-instructions/#debian)tomorrow.

The virtual appliance will be updated once the Debian packages are ready.

## Changes

User-visible features and improvements:

*   [#1156](https://github.com/UNINETT/nav/issues/1156/) (Detect topology of unrouted VLANs)
*   [#1225](https://github.com/UNINETT/nav/issues/1225/) (Service Http(s)Checker should be ok with 401 status if no user/password is configured)
*   [#1232](https://github.com/UNINETT/nav/issues/1232/) (Collect Digital Optical Monitoring (DOM) data)
    *   [#1559](https://github.com/UNINETT/nav/issues/1559/) (Added support for DOM value for juniper devices using JUNIPER-DOM-MIB)
*   [#1240](https://github.com/UNINETT/nav/issues/1240/) (Add a widget with alerts grouped by location)
    *   [#1554](https://github.com/UNINETT/nav/issues/1554/) (Added a Locations with active alerts widget)
*   [#1242](https://github.com/UNINETT/nav/issues/1242/) (information about power over ethernet (poe) interfaces)
*   [#1243](https://github.com/UNINETT/nav/issues/1243/) (email availability reports)
    *   [#1570](https://github.com/UNINETT/nav/issues/1570/) (E-mail subscription to Business reports)
*   [#1313](https://github.com/UNINETT/nav/issues/1313/) (Deleting a netbox is extremely slow)
    *   [#1542](https://github.com/UNINETT/nav/issues/1542/) (Deleting netbox in background with navclean)
*   [#1420](https://github.com/UNINETT/nav/issues/1420/) (Upload and browse pictures on Locations, just as with rooms)
    *   [#1555](https://github.com/UNINETT/nav/issues/1555/) (Added support for pictures in locations)
*   [#1503](https://github.com/UNINETT/nav/issues/1503/) (Extended Location information)
*   [#1505](https://github.com/UNINETT/nav/issues/1505/) (Better ports overview)
    *   [#1562](https://github.com/UNINETT/nav/issues/1562/) (New and improved, filterable interface listing for devices)
    *   [#1600](https://github.com/UNINETT/nav/issues/1600/) (Portlist improvements)
*   [#1506](https://github.com/UNINETT/nav/issues/1506/) (Add option to show source of ARP records in Machine Tracker, to avoid confusion in HSRP/VRRP lans)
    *   [#1541](https://github.com/UNINETT/nav/issues/1541/) (Added option for showing origin in machinetracker)
*   [#1513](https://github.com/UNINETT/nav/issues/1513/) (Support adding, updating and deleting IP Devices using the API)
    *   [#1612](https://github.com/UNINETT/nav/issues/1612/) (Enable write operations for netbox and room API endpoints)
*   [#1533](https://github.com/UNINETT/nav/issues/1533/) (Feature request: toggle all VLANs in portadmin trunk)
*   [#1545](https://github.com/UNINETT/nav/issues/1545/) (Added auditlog for trunk edit in portadmin)
*   [#1584](https://github.com/UNINETT/nav/issues/1584/) (Cleanup django\_sessions periodically)
*   [#1599](https://github.com/UNINETT/nav/issues/1599/) (Option to filter nodes by category in ipdefvinfo neighbor graph)
*   [#1611](https://github.com/UNINETT/nav/issues/1611/) (Display list of allowed VLANs on trunks in port details)

Other fixed GitHub issues in this release:

*   [#1211](https://github.com/UNINETT/nav/issues/1211/) (Optical transmit/receive power sensors should have a relation to an interface)
    *   [#1558](https://github.com/UNINETT/nav/issues/1558/) (Make sensors relatable to interfaces)
*   [#1345](https://github.com/UNINETT/nav/issues/1345/) (Collect bridge addresses for neighbor identification)
    *   [#1548](https://github.com/UNINETT/nav/issues/1548/) (Collect base bridge address from BRIDGE-MIB as part of the bridge plugin)
*   [#1510](https://github.com/UNINETT/nav/issues/1510/) (Create new SQL baseline)
    *   [#1544](https://github.com/UNINETT/nav/issues/1544/) (Updated the SQL Baseline with changes before 4.7)
    *   [#1614](https://github.com/UNINETT/nav/issues/1614/) (SQL baseline cleanup)
*   [#1523](https://github.com/UNINETT/nav/issues/1523/) (Netmap lists interface under wrong netbox)
*   [#1549](https://github.com/UNINETT/nav/issues/1549/) (Topology algorithms partial rewrite)
*   [#1557](https://github.com/UNINETT/nav/issues/1557/) (Power over Ethernet support in ipdevinfo)
*   [#1564](https://github.com/UNINETT/nav/issues/1564/) (snmpcheck: Fix database access from main thread and per process cache)
*   [#1566](https://github.com/UNINETT/nav/issues/1566/) (Remove inline pydns)
*   [#1585](https://github.com/UNINETT/nav/issues/1585/) (Remove support for outdated versions of pysnmp)
*   [#1602](https://github.com/UNINETT/nav/issues/1602/) (Remove django-oauth2-provider library dependency)

Happy NAVing everyone!
