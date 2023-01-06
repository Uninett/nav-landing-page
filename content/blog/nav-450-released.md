---
title: 'NAV 4.5.0 released'
date: 2016-06-09T13:05:00.000+02:00
draft: false
url: /blog/2016/06/nav-450-released/
---

The initial 4.5 series release of NAV is now out.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.5/4.5.0). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

With this release, we discontinue our packaging support for the old Debian Wheezy release. If you wish to package for Wheezy yourself, you can fork the packaging code located at [Bitbucket](https://bitbucket.org/mbrekkevold/nav-debian/).

The virtual appliance will be updated shortly.

### Changes

NAV 4.5 introduces the following user-visible features and improvements:

*   [LP#1321249](https://bugs.launchpad.net/nav/+bug/1321249/) (A new tool for generating Graphite metrics from PostgreSQL queries)
*   [LP#1531851](https://bugs.launchpad.net/nav/+bug/1531851/) (Trend comparison in graphs)
*   [LP#1531853](https://bugs.launchpad.net/nav/+bug/1531853/) (API: more flexible authorization and administration)
*   [LP#1534481](https://bugs.launchpad.net/nav/+bug/1534481/) (Maintenance task selection based on device group)
*   [LP#1546434](https://bugs.launchpad.net/nav/+bug/1546434/) (Add bulk upload of images in room view)
*   [LP#1577318](https://bugs.launchpad.net/nav/+bug/1577318/) (Add timestamp filtering to cam and arp API)
*   [LP#1588187](https://bugs.launchpad.net/nav/+bug/1588187/) (Cabling/patch registration and presentation in need of serious usability improvements)

These reported bugs have been fixed:

*   [LP#1551217](https://bugs.launchpad.net/nav/+bug/1551217/) (Alert from 3rd party - maintenance mode not respected) \[the 4.4.4 release did not fix the eventengine part of this issue, this release does\]
*   [LP#1590654](https://bugs.launchpad.net/nav/+bug/1590654/) (Lost ipdevpoll database connections aren't properly reset under Django 1.7)

Happy NAVing everyone!