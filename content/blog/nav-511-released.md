---
title: 'NAV 5.1.1 released'
date: 2020-12-07T12:55:00.002+01:00
draft: false
url: /blog/2020/12/nav-511-released/
---

The first maintenance release of the 5.1 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 9 (Stretch) have been discontinued.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Fixed GitHub issues in this release

*   [#2200](https://github.com/Uninett/nav/issues/2200) (\[BUG\] HttpChecker crashes when username/password combo is configured)
*   [#2216](https://github.com/Uninett/nav/issues/2216) (\[BUG\] BGP sessions with AS numbers larger than 2147483647 cause ipdevpoll jobs to fail with psycopg2.errors.NumericValueOutOfRange)
*   [#2221](https://github.com/Uninett/nav/issues/2221) (NAV 5.1 Netmap is blank)
*   [#2222](https://github.com/Uninett/nav/issues/2222) (\[BUG\] configuring juniper device description results in HTML special characters code)
*   [#2224](https://github.com/Uninett/nav/issues/2224) (\[BUG\] status now shows box as 'down' even though it is up)
*   [#2225](https://github.com/Uninett/nav/issues/2225) (\[BUG\] Alert export errors prevent proper processing of events in eventengine)
*   [#2229](https://github.com/Uninett/nav/pull/2229) (\[BUG\] EventEngine alert export crashes on any alert from a device that is a member of a device group)
*   [#2230](https://github.com/Uninett/nav/issues/2230) (\[BUG\] Cannot enable dot1x mode in PortAdmin)
*   [#2234](https://github.com/Uninett/nav/issues/2234) (\[BUG\] Bulk import, 'NoneType' object has no attribute 'split')

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.1/release-notes.html#nav-5-1) when upgrading.

Happy NAVing everyone!