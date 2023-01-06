---
title: 'NAV 5.1.4 released'
date: 2021-06-24T11:51:00.001+02:00
draft: false
url: /blog/2021/06/nav-514-released/
---

The fourth maintenance release of the 5.1 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 9 (Stretch) have been discontinued.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Fixed GitHub issues in this release

*   [#2281](https://github.com/Uninett/nav/issues/2281) (\[BUG\] Saving alert permissions crashes Alert Profiles)
*   [#2282](https://github.com/Uninett/nav/pull/2282) (PortAdmin SNMP error handling is broken in several ways)
*   [#2284](https://github.com/Uninett/nav/issues/2284) (\[BUG\] IP device interfaces don't get updated with speed information)
*   [#2285](https://github.com/Uninett/nav/pull/2285) (Extract Cisco PoE port mapping method)
*   [#2288](https://github.com/Uninett/nav/pull/2288) (Disable the PortAdmin "Enable" checkbox for interfaces that aren't editable)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.1/release-notes.html#nav-5-1) when upgrading.

Happy NAVing everyone!