---
title: 'NAV 4.5.3 released'
date: 2016-09-05T08:41:00.000+02:00
draft: false
url: /blog/2016/09/the-third-maintenance-release-of-nav-4/
---

The third maintenance release of the NAV 4.5 series is now out.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.5/4.5.3). A new package for Debian Jessie has been published in our [APT repository](https://nav.uninett.no/install-instructions/#debian)as usual (and the virtual appliance is being updated).

## Changes

The following reported bugs have been fixed:

*   [LP#1592747](https://bugs.launchpad.net/nav/+bug/1592747/) (Cisco chassis serial number decoding report should include modules as well)
*   [LP#1597666](https://bugs.launchpad.net/nav/+bug/1597666/) (No data collected on some Comet web probes)
*   [LP#1608869](https://bugs.launchpad.net/nav/+bug/1608869/) (graph widget does not update)
*   [LP#1608920](https://bugs.launchpad.net/nav/+bug/1608920/) (make graph widget time controls optional)
*   [LP#1619136](https://bugs.launchpad.net/nav/+bug/1619136/) (Specifying both starttime and endtime values crashes the arp API endpoint)
*   [LP#1619138](https://bugs.launchpad.net/nav/+bug/1619138/) (Searching for IP addresses in the arp API endpoint is horribly inefficient)

The fix for [LP#1619138](https://bugs.launchpad.net/nav/+bug/1619138/) also entails that searching for IP prefixes is also possible on the `arp` API endpoint.

Happy NAVing everyone!
