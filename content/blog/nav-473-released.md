---
title: 'NAV 4.7.3 released'
date: 2017-11-13T09:15:00.000+01:00
draft: false
url: /2017/11/nav-473-released.html
---

The third maintenance release of the 4.7 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly. The appliance is still based on Debian Jessie, but will hopefully migrate to Debian Stretch soon.

### Changes

Fixed [issues](https://github.com/UNINETT/nav/issues) in this release:

*   [#1402](https://github.com/UNINETT/nav/issues/1402/) (Maintenance alerts about non existing devices)
*   [#1590](https://github.com/UNINETT/nav/issues/1590/) (IPAM: Add quickfix, logging for prefixes with no VLAN)
*   [#1592](https://github.com/UNINETT/nav/issues/1592/) (Report crashes when attempting to sort a column filtered on a non-ASCII value)
*   [#1593](https://github.com/UNINETT/nav/issues/1593/) (Logengine inserts quoted log messages into database)
*   [#1595](https://github.com/UNINETT/nav/issues/1595/) (Drawing sensor graphs fail for sensors that have no human readable description)
*   [#1601](https://github.com/UNINETT/nav/issues/1601/) (Updating room id creates a new room)
*   [#1603](https://github.com/UNINETT/nav/issues/1603/) (AlertEngine crashes when processing filters containing "not equals" matches)
*   [#1604](https://github.com/UNINETT/nav/issues/1604/) (Running ipdevpoll in multiprocess mode will delay resolving of snmpAgentDown alerts)
*   [#1605](https://github.com/UNINETT/nav/issues/1605/) (Log output from ipdevpoll multiprocess workers is lost)
*   [#1606](https://github.com/UNINETT/nav/issues/1606/) (linear gauge does not fill with gradient)
*   [#1610](https://github.com/UNINETT/nav/issues/1610/) (Remove stale topology information from ports that are down, where the assumed link partner is still up )

Happy NAVing everyone!