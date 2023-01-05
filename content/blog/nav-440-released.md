---
title: 'NAV 4.4.0 released'
date: 2016-01-15T00:44:00.000+01:00
draft: false
url: /2016/01/nav-440-released.html
tags: 
- release
- 4.4
- nav
- regular
- 4.4.0
---

The initial 4.4 series release of NAV is now out.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.4/4.4.0). New packages for Debian Wheezy and Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

The virtual appliance will be updated shortly.

### Changes

NAV 4.4 now requires Django 1.7. Unfortunately, Django 1.7 was obsoleted in December, but since we mainly target Debian stable (Jessie), security fixes will be backported by Debian to Django 1.7 for a long time to come. (If you are still running Debian Wheezy, you can obtain python-django 1.7 from the official wheezy-backports repository).

NAV 4.4 introduces the following user-visible features and improvements:

*   [LP#1350815](https://bugs.launchpad.net/nav/+bug/1350815/) (Add zooming in graphs, like Cacti)
*   [LP#1465571](https://bugs.launchpad.net/nav/+bug/1465571/) (PortAdmin should log to separate log file)
*   [LP#1466373](https://bugs.launchpad.net/nav/+bug/1466373/) (seeddb confirm navigation when form is not saved)
*   [LP#1466440](https://bugs.launchpad.net/nav/+bug/1466440/) (Device groups should be searchable from the navbar)
*   [LP#1466462](https://bugs.launchpad.net/nav/+bug/1466462/) (Report pagination is nearly invisible)
*   [LP#1483578](https://bugs.launchpad.net/nav/+bug/1483578/) (request: enable-button in /arnold/details/)
*   [LP#1511363](https://bugs.launchpad.net/nav/+bug/1511363/) (Organize scope-list in Subnet Matrix-frontend)
*   [LP#1526789](https://bugs.launchpad.net/nav/+bug/1526789/) (Support sensor discovery on Geist-branded WeatherGoose products)
*   [LP#1528124](https://bugs.launchpad.net/nav/+bug/1528124/) (Autocreate new types with sensible vendor id’s)
*   [LP#1531159](https://bugs.launchpad.net/nav/+bug/1531159/) (portadmin: support for Cisco voice vlans)

These reported bugs have been fixed:

*   [LP#1248205](https://bugs.launchpad.net/nav/+bug/1248205/) (403 Forbidden on front page with apache 2.4)
*   [LP#1518246](https://bugs.launchpad.net/nav/+bug/1518246/) (subnet matrix - first subnet is not shown)
*   [LP#1518251](https://bugs.launchpad.net/nav/+bug/1518251/) (subnet matrix - /23 prefixes are displayed incorrectly)
*   [LP#1518254](https://bugs.launchpad.net/nav/+bug/1518254/) (subnet matrix - link to prefix is suddenly a scope)
*   [LP#1521107](https://bugs.launchpad.net/nav/+bug/1521107/) (Messages widget does not refresh)
*   [LP#1521124](https://bugs.launchpad.net/nav/+bug/1521124/) (Django security fix in Debian makes time periods display as blank)
*   [LP#1526282](https://bugs.launchpad.net/nav/+bug/1526282/) (Module replacements will sometimes crash ipdevpoll inventory job with IntegrityError)
*   [LP#1532701](https://bugs.launchpad.net/nav/+bug/1532701/) (Snmptrapd fails to post link events if module name is unknown)

Happy NAVing everyone!