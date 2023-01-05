---
title: 'NAV 4.9.3 released'
date: 2019-02-28T13:00:00.000+01:00
draft: false
url: /2019/02/nav-493-released.html
---

The third maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) are published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has also been updated.

#### Fixed GitHub issues in this release:

*   [#757](https://github.com/Uninett/nav/issues/757) (devicehistory search by date ignores date)
*   [#1792](https://github.com/Uninett/nav/issues/1792) (Precision of several Eaton/MGE UPS sensors are wrong)
*   [#1812](https://github.com/Uninett/nav/issues/1812) (Malformed subid on (old) thresholdState events can cause status page and alert API endpoints to crash)
*   [#1818](https://github.com/Uninett/nav/issues/1818) (Update ENTITY-MIB definition to RFC 6933)
*   [#1855](https://github.com/Uninett/nav/issues/1855) (IPAM subnet suggest function is broken)
*   [#1856](https://github.com/Uninett/nav/issues/1856) (Geomap doesn't work in NAV 4.9)
*   [#1857](https://github.com/Uninett/nav/issues/1857) (E-mailing of business report subscriptions doesn't work)
*   [#1862](https://github.com/Uninett/nav/issues/1862) (Please add case-insensitive matching on interface names in ipdevinfo queries for 'ifname')
*   [#1865](https://github.com/Uninett/nav/issues/1865) (Servicemon resource leak causes all services to be reported as down)
*   [#1871](https://github.com/Uninett/nav/issues/1871) (Alert detail headers are not present in e-mail notifications from AlertEngine)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.  
Happy NAVing everyone!