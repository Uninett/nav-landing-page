---
title: 'NAV 5.0.1 released'
date: 2019-12-05T11:19:00.000+01:00
draft: false
url: /blog/2019/12/nav-501-released/
---

The first maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Deprecation warning

Python 2 reaches its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

#### Fixed GitHub issues in this release:

*   [#2016](https://github.com/Uninett/nav/issues/2016) (ipdevpoll inventory job crashes when processing manufacturing dates from ENTITY-MIB under Python 3)
*   [#2019](https://github.com/Uninett/nav/issues/2019) (IP Device info "Neighbor" tab is blank)
*   [#2023](https://github.com/Uninett/nav/issues/2023) (Netmap layer 3 crashing)
*   [#2025](https://github.com/Uninett/nav/issues/2025) (SeedDB bulk import file upload crashes)
*   [#2030](https://github.com/Uninett/nav/pull/2030) (Ensure internal snmp agent check state stays in sync with global snmpAgentState)
*   [#2031](https://github.com/Uninett/nav/pull/2031) (Fix PortAdmin crash on invalid IP search)
*   [#2032](https://github.com/Uninett/nav/pull/2032) (Replace SNMP community columns in SeedDB netbox listing with management profile lists)
*   [#2033](https://github.com/Uninett/nav/pull/2033) (Don't crash when logging in users with old-style password hashes)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!