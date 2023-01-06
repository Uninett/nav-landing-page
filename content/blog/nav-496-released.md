---
title: 'NAV 4.9.6 released'
date: 2019-05-23T12:45:00.000+02:00
draft: false
url: /blog/2019/05/nav-496-released/
---

The sixth maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 8/9 (Jessie/Stretch) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has also been updated.

#### Fixed GitHub issues in this release:

*   [#1782](https://github.com/Uninett/nav/pull/1782) (ipdevpoll snmpcheck algorithm no longer works as expected)
    *   [#1952](https://github.com/Uninett/nav/pull/1952) ((snmpcheck) Store up/down state in NetboxInfo, so we can properly sen…)
*   [#1931](https://github.com/Uninett/nav/issues/1931) (Support for HPE Metered PDUs)
    *   [#1933](https://github.com/Uninett/nav/pull/1933) (Add support for HPE metered PDUs)
*   [#1935](https://github.com/Uninett/nav/issues/1935) (The VLAN dropdowns in PortAdmin needs to show the description in addition to the id, if any)
    *   [#1955](https://github.com/Uninett/nav/pull/1955) (Show net ident for vlans in the portadmin vlan dropdown box)
*   [#1944](https://github.com/Uninett/nav/issues/1944) (Sensor links in Environment Rack navlet does not work)
*   [#1948](https://github.com/Uninett/nav/pull/1948) (Verify LDAP entitlements)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!