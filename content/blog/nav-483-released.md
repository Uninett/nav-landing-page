---
title: 'NAV 4.8.3 released'
date: 2018-01-12T08:28:00.000+01:00
draft: false
url: /blog/2018/01/nav-483-released/
tags:
- release
---

The third maintenance release of the 4.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) are published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

## Changes

Fixed GitHub issues:

*   [#1619](https://github.com/UNINETT/nav/issues/1619/) (Port-filter in ipdevinfo ports-tab does not remember choice in IE Edge)
*   [#1640](https://github.com/UNINETT/nav/issues/1640/) (snmptrapd documentation is outdated)
*   [#1641](https://github.com/UNINETT/nav/issues/1641/) (Inefficient deletion of obsolete SwPortVlan records)
*   [#1642](https://github.com/UNINETT/nav/issues/1642/) (Port details page crashes with NoReverseMatch exception for ports with slashes in names)
*   [#1644](https://github.com/UNINETT/nav/issues/1644/) (Certain UPS units trigger an AssertionError inside ipdevpoll's bridge plugin, crashing the inventory job)
*   [#1645](https://github.com/UNINETT/nav/issues/1645/) (navtopology crashes on self-loops)
*   [#1647](https://github.com/UNINETT/nav/issues/1647/) (NAV 4.8.2 LDAP error at first login / user creation)
*   [#1648](https://github.com/UNINETT/nav/issues/1648/) (Several NAV subsystems crash when config files contain non- ASCII comments)
*   [#1649](https://github.com/UNINETT/nav/issues/1649/) (Negative values leads to mangled graphs)

Happy NAVing everyone!
