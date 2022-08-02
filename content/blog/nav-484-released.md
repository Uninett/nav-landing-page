---
title: 'NAV 4.8.4 released'
date: 2018-04-05T16:18:00.000+02:00
draft: false
url: /2018/04/nav-484-released.html
---

The fourth maintenance release of the 4.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) are published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

### Changes

Fixed GitHub issues:

*   [#1638](https://github.com/UNINETT/nav/issues/1638/) ('array index out of range' when viewing a trunk port in PortAdmin)
*   [#1643](https://github.com/UNINETT/nav/issues/1643/) (Location with active alerts - edit title)
*   [#1650](https://github.com/UNINETT/nav/issues/1650/) (Submitting a threshold rule without a target crashes with a KeyError)
*   [#1655](https://github.com/UNINETT/nav/issues/1655/) (Auditlog only displaying the first 100 entries in the log)
    *   [#1654](https://github.com/UNINETT/nav/issues/1654/) (Fix broken auditlog browsing and auditlog more things)
*   [#1656](https://github.com/UNINETT/nav/issues/1656/) (Sensor widget crashes when sensor is missing)
*   [#1660](https://github.com/UNINETT/nav/issues/1660/) (UninettMailDispatcher does not support non-ASCII characters and requires SMTP server on localhost)
*   [#1661](https://github.com/UNINETT/nav/issues/1661/) (Business reports, link availability - want description)
*   [#1664](https://github.com/UNINETT/nav/issues/1664/) (Remove bracket syntax for url parameters to Graphite)
*   [#1665](https://github.com/UNINETT/nav/issues/1665/) (Interface details tries to get sensor data on empty sensorlist)
*   [#1669](https://github.com/UNINETT/nav/issues/1669/) (Shouldn't use CAM to select topology for aggregated ports where LLDP is available on the physical ports)
    *   [#1685](https://github.com/UNINETT/nav/issues/1685/) (Do not consider CAM data from aggregator ports when there is LLDP/CDP topology available from its aggregated ports)
*   [#1670](https://github.com/UNINETT/nav/issues/1670/) (Treshold editor doesn't work for metrics with hash characters in name)
*   [#1673](https://github.com/UNINETT/nav/issues/1673/) (Repeated traceback e-mails for Internal Server Error: /netmap/traffic/layer2/)
*   [#1676](https://github.com/UNINETT/nav/issues/1676/) (Audit log changes to API tokens)
*   [#1677](https://github.com/UNINETT/nav/issues/1677/) (ipdevinfo should link to an IP Device's audit log)
*   [#1678](https://github.com/UNINETT/nav/issues/1678/) (EventMixIn.get\_subject() should never return a string)
*   [#1680](https://github.com/UNINETT/nav/issues/1680/) (SeedDB patch editor only lists switch ports, not physical ports)

Happy NAVing everyone!