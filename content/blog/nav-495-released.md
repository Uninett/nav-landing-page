---
title: 'NAV 4.9.5 released'
date: 2019-05-02T11:55:00.001+02:00
draft: false
url: /blog/2019/05/nav-495-released/
tags:
- release
---

The fifth maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 8/9 (Jessie/Stretch) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has also been updated.

## Fixed GitHub issues in this release:

*   [#1890](https://github.com/Uninett/nav/issues/1890) (Temperature gauges do not render if multiple threshold rules apply to it)
    *   [#1921](https://github.com/Uninett/nav/pull/1921) (Handle arbitrary number of thresholds for a given sensor)
*   [#1902](https://github.com/Uninett/nav/issues/1902) (Sensor widgets should hyperlink to sensor's page view, not IP Device's page view)
*   [#1903](https://github.com/Uninett/nav/issues/1903) (Topology missing for LLDP-enabled Alcatel switches)
*   [#1906](https://github.com/Uninett/nav/issues/1906) ("Cisco chassis/module serial numbers decoded" report crashes when filtering)
*   [#1907](https://github.com/Uninett/nav/issues/1907) (servicemon DnsChecker fails when DNS server doesn't have a matching record)
*   [#1916](https://github.com/Uninett/nav/issues/1916) (UninettMailDispatcher does not work under NAV 4.9)
*   [#1917](https://github.com/Uninett/nav/issues/1917) (snmptrapd needs to log more details about received traps)
*   [#1923](https://github.com/Uninett/nav/issues/1923) (ENTITY-MIB implementation can no longer resolve physical device classes properly)
    *   [#1924](https://github.com/Uninett/nav/pull/1924) (Support cross-MIB type definitions in MibRetrievers)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!
