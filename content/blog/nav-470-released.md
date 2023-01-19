---
title: 'NAV 4.7.0 released'
date: 2017-06-09T16:13:00.001+02:00
draft: false
url: /blog/2017/06/nav-470-released/
---

The initial 4.7 series release of NAV is now out!

Because we discovered serious but easily fixable problems rather early, we decided to postpone posting on the blog. A separate post for the bugfix-release is posted as usual.

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

## Changes

As always, we recommend you read the [release notes](https://nav.uninett.no/doc/4.7/release-notes.html#nav-4-7) for a fuller description of the new features and significant changes.

NAV 4.7 introduces the following user-visible features and improvements:

*   [#1174](https://github.com/UNINETT/nav/issues/1174/) (Rewrite ipdevpoll's multiprocess mode to use generic worker model)
*   [#1183](https://github.com/UNINETT/nav/issues/1183/)+#1463 (Monitor BGP connectivity)
*   [#1236](https://github.com/UNINETT/nav/issues/1236/)+1416 (Feature request: API for unrecognized neighbors)
*   [#1239](https://github.com/UNINETT/nav/issues/1239/) (multidashboard export import)
*   [#1411](https://github.com/UNINETT/nav/issues/1411/)+#1515 (Add PortAdmin "Write mem" support for H3C switches)
*   [#1428](https://github.com/UNINETT/nav/issues/1428/) (added broadcast & multicast counters to interfaces (ipdevinfo))
*   [#1467](https://github.com/UNINETT/nav/issues/1467/) (Add support for Comet MS series data loggers)
*   [#1468](https://github.com/UNINETT/nav/issues/1468/) (Rittal cmc iii support)
*   [#1469](https://github.com/UNINETT/nav/issues/1469/) (Powernet: Distinguish between phase load and bank load sensors.)
*   [#1472](https://github.com/UNINETT/nav/issues/1472/) (Added support for Raritan PDU2 mib PDUs)
*   [#1474](https://github.com/UNINETT/nav/issues/1474/) (Add a comprehensive view of collected sensors and their data on a new Sensors tab in ipdevinfo)
*   [#1475](https://github.com/UNINETT/nav/issues/1475/) (Collect sensor readings from Lenovo/IBM PDUs (Power Distribution Units))
*   [#1486](https://github.com/UNINETT/nav/issues/1486/)+#1488 (Add a rack based view of environment sensors in a room)
*   [#1489](https://github.com/UNINETT/nav/issues/1489/)+#1492 (Avoid redundant port counter collection from virtualized instances, such as Cisco VRF)
*   [#1498](https://github.com/UNINETT/nav/issues/1498/) (Add fullscreen mode for all maps)
*   [#1518](https://github.com/UNINETT/nav/issues/1518/) (Default setting for map starting point when selecting room geo location)
*   [#1522](https://github.com/UNINETT/nav/issues/1522/) (Auditlog)

These reported bugs have been fixed:

*   [#1403](https://github.com/UNINETT/nav/issues/1403/) (deleting a netbox makes data-collection stop)
*   [#1456](https://github.com/UNINETT/nav/issues/1456/) (The old status page code should be removed)
*   [#1462](https://github.com/UNINETT/nav/issues/1462/) (Netmap performance improvements)
*   [#1493](https://github.com/UNINETT/nav/issues/1493/) (Status widget, "Not device group" filter is wrong)
*   [#1496](https://github.com/UNINETT/nav/issues/1496/) (Missing jQuery tinysort javascript library)
*   [#1500](https://github.com/UNINETT/nav/issues/1500/) (Sensor details - fix spelling on "Thesholds")
*   [#1507](https://github.com/UNINETT/nav/issues/1507/) (The regexp for ifalias is not shown)
*   [#1511](https://github.com/UNINETT/nav/issues/1511/) (Minor IPAM improvements)
*   [#1512](https://github.com/UNINETT/nav/issues/1512/) (Update old javascript libraries)
*   [#1519](https://github.com/UNINETT/nav/issues/1519/) (ipdevinfo doesn't list aggregators for some Juniper interfaces)

Happy NAVing everyone!
