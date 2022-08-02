---
title: 'NAV 4.4.4 released'
date: 2016-06-09T13:01:00.000+02:00
draft: false
url: /2016/06/nav-444-released.html
---

The fourth maintenance release of the NAV 4.4 series was released 02.06.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.4/4.4.4). New packages for Debian Wheezy and Jessie have been published in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual (and the virtual appliance is being updated).

### Changes

The following reported bugs have been fixed:

*   [LP#1551217](https://bugs.launchpad.net/nav/+bug/1551217/) (Alert from 3rd party - maintenance mode not respected)
*   [LP#1569704](https://bugs.launchpad.net/nav/+bug/1569704/) (Supplied Apache config example doesn't explicitly allow access to read files in the upload location)
*   [LP#1570814](https://bugs.launchpad.net/nav/+bug/1570814/) (DNS lookups in web UI leak UDP sockets until resource exhaustion)
*   [LP#1571010](https://bugs.launchpad.net/nav/+bug/1571010/) (timeformat unreadable in scheduled messages)
*   [LP#1572580](https://bugs.launchpad.net/nav/+bug/1572580/) (Malformed month names in syslog messages cause logengine crash)
*   [LP#1572599](https://bugs.launchpad.net/nav/+bug/1572599/) (Adding VLAN graphs to dashboard does nothing)
*   [LP#1572894](https://bugs.launchpad.net/nav/+bug/1572894/) (portadmin: Save all button disappears on small screens)
*   [LP#1573486](https://bugs.launchpad.net/nav/+bug/1573486/) (netmap crashes when a room is not connected to a location)
*   [LP#1573569](https://bugs.launchpad.net/nav/+bug/1573569/) (portadmin: crash when cisco voice enabled and visiting hp device)
*   [LP#1578108](https://bugs.launchpad.net/nav/+bug/1578108/) (eventengine enters an infinite loop and stops processing events)
*   [LP#1588201](https://bugs.launchpad.net/nav/+bug/1588201/) (Status page describes many threshold alerts only as "Sensor object")

Happy NAVing everyone!