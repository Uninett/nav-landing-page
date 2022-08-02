---
title: 'NAV 4.6.0 released'
date: 2016-12-01T15:27:00.001+01:00
draft: false
url: /2016/12/nav-460-released.html
---

The initial 4.6 series release of NAV is now out!

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.6/4.6.0). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

### Changes

As always, we recommend you read [the release notes](https://nav.uninett.no/doc/4.6/release-notes.html#nav-4-6) for a fuller description of the new features and significant changes.

NAV 4.6 introduces the following user-visible features and improvements:

*   [LP#1567943](https://bugs.launchpad.net/nav/+bug/1567943/) (multiple dashboards)
*   [LP#1248086](https://bugs.launchpad.net/nav/+bug/1248086/) (alert on loss of redundancy in an aggregated (portchannel) link)
*   [LP#1531850](https://bugs.launchpad.net/nav/+bug/1531850/) (more flexible system for location of equipment)
*   [LP#1634874](https://bugs.launchpad.net/nav/+bug/1634874/) (choose columns in status widget)
*   [LP#1646405](https://bugs.launchpad.net/nav/+bug/1646405/) (Improve functions for IP Address Management \[IPAM\])
*   [LP#1646408](https://bugs.launchpad.net/nav/+bug/1646408/) (prefix details page)
*   [LP#1646411](https://bugs.launchpad.net/nav/+bug/1646411/) (Collect and store static routes)
*   [LP#1646413](https://bugs.launchpad.net/nav/+bug/1646413/) (Work around buggy Q-BRIDGE-MIB implementation in Juniper EX switches)
*   [LP#1646416](https://bugs.launchpad.net/nav/+bug/1646416/) (Add a command line program to manipulate NAV users)

These reported bugs have been fixed:

*   [LP#1626856](https://bugs.launchpad.net/nav/+bug/1626856/) (ipdevpoll inventory job crashes if a device reports multiple modules with the same name)
*   [LP#1629823](https://bugs.launchpad.net/nav/+bug/1629823/) (prefix usage api endpoint lists empty results)
*   [LP#1630506](https://bugs.launchpad.net/nav/+bug/1630506/) (Arnold detention crashes when switch reports SNMP agent error)
*   [LP#1634903](https://bugs.launchpad.net/nav/+bug/1634903/) (LLDP topology bug when two devices share the same initial sysname)
*   [LP#1638568](https://bugs.launchpad.net/nav/+bug/1638568/) (Incomplete topology information causes eventengine to post boxShadow alerts instead of boxDown alerts)
*   [LP#1640714](https://bugs.launchpad.net/nav/+bug/1640714/) (Erroneous interpretation of LLDP-MIB port numbers may cause wrong topology to be detected)
*   [LP#1641522](https://bugs.launchpad.net/nav/+bug/1641522/) (Chart Widget unresponsive)

Happy NAVing everyone!