---
title: 'NAV 4.3.2 released'
date: 2015-11-19T05:52:00.000+01:00
draft: false
url: /2015/11/nav-432-released.html
tags: 
- bugfix
- 4.3
- nav
- regular
---

The second maintenance release of the NAV 4.3 series is now out.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.3/4.3.2). New packages for Debian Wheezy and Jessie have been published in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual (and the virtual appliance has been updated).

### Changes

The following reported bugs have been fixed:

*   [LP#1487436](https://bugs.launchpad.net/nav/+bug/1487436/) (arnold rejects ip-addresses that ends with the number 0)
*   [LP#1488003](https://bugs.launchpad.net/nav/+bug/1488003/) (Alert Profiles UI does not enable multi-value select for the “IN” filter operator)
*   [LP#1488010](https://bugs.launchpad.net/nav/+bug/1488010/) (link to ipdevinfo if applicable for subjects without absolute url)
*   [LP#1488441](https://bugs.launchpad.net/nav/+bug/1488441/) (room map widget does not load map)
*   [LP#1488774](https://bugs.launchpad.net/nav/+bug/1488774/) (Arnold documentation should be updated and moved from wiki to Sphinx)
*   [LP#1489843](https://bugs.launchpad.net/nav/+bug/1489843/) (javascript require-libs timeout)
*   [LP#1492246](https://bugs.launchpad.net/nav/+bug/1492246/) (Topology of disabled interfaces may linger in some cases)
*   [LP#1494190](https://bugs.launchpad.net/nav/+bug/1494190/) (clicking on a shared time period in alert profiles selects all)
*   [LP#1494232](https://bugs.launchpad.net/nav/+bug/1494232/) (hovering a shared time period in alert profiles highlights all)
*   [LP#1494233](https://bugs.launchpad.net/nav/+bug/1494233/) (When exporting switch port information from a room view as CSV, the output contains extra spaces and newlines in the first column)
*   [LP#1494279](https://bugs.launchpad.net/nav/+bug/1494279/) (Inconsistent Servicemon checker names)
*   [LP#1496396](https://bugs.launchpad.net/nav/+bug/1496396/) (Service checker descriptions and service checker argument descriptions are not displayed to the user in SeedDB)
*   [LP#1496780](https://bugs.launchpad.net/nav/+bug/1496780/) (Threshold alerts are not very descriptive on the status page)
*   [LP#1497970](https://bugs.launchpad.net/nav/+bug/1497970/) (Add SEMI-MIB to retrieve serial number for HP 1810 switch)
*   [LP#1498323](https://bugs.launchpad.net/nav/+bug/1498323/) (Traps from WeatherGoose devices no longer work after rebranding from IT Watchdogs to Geist)
*   [LP#1499343](https://bugs.launchpad.net/nav/+bug/1499343/) (The wiki page describing background processes in NAV should be moved to Sphinx docs)
*   [LP#1500423](https://bugs.launchpad.net/nav/+bug/1500423/) (ipdevpoll: Transaction managed block ended with pending COMMIT/ROLLBACK)
*   [LP#1500425](https://bugs.launchpad.net/nav/+bug/1500425/) (Inventory and statuscheck jobs of ipdevpoll still can fail after an OS upgrade)
*   [LP#1505524](https://bugs.launchpad.net/nav/+bug/1505524/) (Retrieve software version for HP 1810 switch)
*   [LP#1505945](https://bugs.launchpad.net/nav/+bug/1505945/) (Add API endpoint for VLAN information)
*   [LP#1507467](https://bugs.launchpad.net/nav/+bug/1507467/) (Temperature sensor gauges as widgets)
*   [LP#1513046](https://bugs.launchpad.net/nav/+bug/1513046/) (LLDP neighbors with “funny” names may cause ipdevinfo NoReverseMatch crash)
*   [LP#1516956](https://bugs.launchpad.net/nav/+bug/1516956/) (Services should be considered on maintenance when their parent IP Device is on maintenance)
*   [LP#1516972](https://bugs.launchpad.net/nav/+bug/1516972/) (Maintenance status is not visible in service matrix and service lists)

Happy NAVing everyone!