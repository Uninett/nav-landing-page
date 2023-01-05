---
title: 'NAV 4.3.1 released'
date: 2015-08-20T06:50:00.000+02:00
draft: false
url: /2015/08/nav-431-released.html
tags: 
- bugfix
- 4.3
- nav
- regular
- 4.3.1
---

The first maintenance release of the NAV 4.3 series is now out.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.3/4.3.1). New packages for Debian Wheezy and Jessie have been published in our [APT repository](https://nav.uninett.no/wiki/nav_on_debian) as usual.

### Changes

The following reported bugs have been fixed:

*   [LP#1464660](https://bugs.launchpad.net/nav/+bug/1464660/) (macwatch AttributeError when attempting to post events under NAV 4.3.0)
*   [LP#1466734](https://bugs.launchpad.net/nav/+bug/1466734/) (Portadmin should link back to ipdevinfo)
*   [LP#1467508](https://bugs.launchpad.net/nav/+bug/1467508/) (report export csv not working)
*   [LP#1469620](https://bugs.launchpad.net/nav/+bug/1469620/) (Ipdevinfo: switchport activity only show activity for last 30 days)
*   [LP#1469988](https://bugs.launchpad.net/nav/+bug/1469988/) (arnold does not reset autoenable date on manual detentions)
*   [LP#1478827](https://bugs.launchpad.net/nav/+bug/1478827/) (Include vendor and description in the netbox API endpoint)
*   [LP#1478835](https://bugs.launchpad.net/nav/+bug/1478835/) (portadmin snmp timeout while saving)
*   [LP#1480262](https://bugs.launchpad.net/nav/+bug/1480262/) (Rendering a port traffic graph results in a UnicodeEncodeError)
*   [LP#1480814](https://bugs.launchpad.net/nav/+bug/1480814/) (Non-ASCII characters in username will crash login page if authenticating against a Microsoft AD server)
*   [LP#1483145](https://bugs.launchpad.net/nav/+bug/1483145/) (seeddb invalid ip crashes check connectivity)
*   [LP#1484386](https://bugs.launchpad.net/nav/+bug/1484386/) (Floating graph control panel intermittently appears at top of page when selecting Port Metrics tab in ipdevinfo)
*   [LP#1484423](https://bugs.launchpad.net/nav/+bug/1484423/) (ipdevpoll inventory job fails with AttributeError: ‘NoneType’ object has no attribute 'strip’)
*   [LP#1484427](https://bugs.launchpad.net/nav/+bug/1484427/) (ipdevpoll 5minstats job fails on some Cisco WLCs)
*   [LP#1486415](https://bugs.launchpad.net/nav/+bug/1486415/) (IntegrityError when posting chassis events from ipdevpoll)
*   [LP#1486430](https://bugs.launchpad.net/nav/+bug/1486430/) (Jobs “inventory” and “statuscheck” fails after switch OS upgrade)

Happy NAVing everyone!