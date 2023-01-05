---
title: 'NAV 4.9.8 released'
date: 2019-08-22T14:54:00.000+02:00
draft: false
url: /2019/08/nav-498-released.html
---

The eighth maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has been updated.

#### Fixed GitHub issues in this release:

*   [#1753](https://github.com/Uninett/nav/issues/1753) (SNMP-less servers are no longer connected in the NAV topology)
*   [#1941](https://github.com/Uninett/nav/issues/1941) (Interface information pop-ups in the status widget tends to hang)
*   [#1942](https://github.com/Uninett/nav/issues/1942) (get\_mib() should be able to load MIB modules from outside the nav.smidumps package)
*   [#1962](https://github.com/Uninett/nav/issues/1962) (Environment rack widget edit mode crashes if there are racks in rooms with non-ascii characters in their name)
*   [#1964](https://github.com/Uninett/nav/issues/1964) (smsd crashes when discarding non-dispatchable messages with non-ASCII chars (or for users with non-ASCII chars in their name))
*   [#1972](https://github.com/Uninett/nav/pull/1972) (Ensure PostgreSQL unique constraints are consistently named)
*   [#1973](https://github.com/Uninett/nav/pull/1973) (Stop explicitly installing pl/pgSQL during db init.)
*   [#1975](https://github.com/Uninett/nav/issues/1975) (Unhandled ValueError in eventengine when snmptrapd posts invalid linkState events)
*   [#1976](https://github.com/Uninett/nav/pull/1976) (Properly display sensor data scale on sensor details page.)
*   [#1977](https://github.com/Uninett/nav/pull/1977) (Use Juniper 802.1X VLAN workaround in default configuration)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!