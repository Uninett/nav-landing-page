---
title: 'NAV 4.4.3 released'
date: 2016-04-05T13:17:00.000+02:00
draft: false
url: /blog/2016/04/nav-443-released/
tags:
- release
---

The third maintenance release of the NAV 4.4 series was released 31.03.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.4/4.4.3). New packages for Debian Wheezy and Jessie have been published in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual (and the virtual appliance is being updated).

## Changes

The following reported bugs have been fixed:

*   [LP#1538270](https://bugs.launchpad.net/nav/+bug/1538270/) (PortAdmin crashes when non admin try to remove a vlan from the trunk)
*   [LP#1543529](https://bugs.launchpad.net/nav/+bug/1543529/) (portadmin: default vlan is not setable for non-admin if auth is enabled)
*   [LP#1543953](https://bugs.launchpad.net/nav/+bug/1543953/) (Wrong units in Gbits/s graphs)
*   [LP#1544059](https://bugs.launchpad.net/nav/+bug/1544059/) (Subnet matrix is no longer helpful when no scopes have been defined)
*   [LP#1551205](https://bugs.launchpad.net/nav/+bug/1551205/) (Subject description of 3rd party alerts in status page are uninformative)
*   [LP#1552198](https://bugs.launchpad.net/nav/+bug/1552198/) (ranked statistics give vague error when no data exists)
*   [LP#1554466](https://bugs.launchpad.net/nav/+bug/1554466/) (PortAdmin: when proper cisco voice vlans enabled changing vlan changes native vlan)
*   [LP#1559004](https://bugs.launchpad.net/nav/+bug/1559004/) (Extract VLAN information from Juniper routers)
*   [LP#1563369](https://bugs.launchpad.net/nav/+bug/1563369/) (Rickshaw graphs do not update on interval change)

Happy NAVing everyone!
