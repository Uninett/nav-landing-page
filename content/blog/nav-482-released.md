---
title: 'NAV 4.8.2 released'
date: 2017-12-07T10:17:00.000+01:00
draft: false
url: /blog/2017/12/nav-482-released/
---

The second maintenance release of the 4.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) are published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

## Changes

Fixed GitHub issues:

*   [#1591](https://github.com/UNINETT/nav/issues/1591/) (SeedDB does not warn about too long room ids or location ids when bulk importing, it just crashes)
*   [#1628](https://github.com/UNINETT/nav/issues/1628/) (Room status widget crash with MultipleObjectsReturned in some cases)
*   [#1629](https://github.com/UNINETT/nav/issues/1629/) (Following a link to edit an IP Device that has been deleted crashes SeedDB)
*   [#1631](https://github.com/UNINETT/nav/issues/1631/) (ipdevpoll statuscheck job crashes in poe plugin)
*   [#1632](https://github.com/UNINETT/nav/issues/1632/) (The ipdevpoll 5minstats job crashes with an AttributeError in the statports plugin)
*   [#1633](https://github.com/UNINETT/nav/issues/1633/) (The ipdevpoll 5minstats job crashes in the statsystem plugin on VRF master devices)
*   [#1634](https://github.com/UNINETT/nav/issues/1634/) (The poe plugin still crashes on devices that have no set type)
*   [#1635](https://github.com/UNINETT/nav/issues/1635/) (The statuscheck ipdevpoll job crashes with an AttributeError if device reports inconsistent PoE Group indexes in POWER- ETHERNET-MIB)

Happy NAVing everyone!
