---
title: 'NAV 4.9.7 released'
date: 2019-06-07T10:42:00.000+02:00
draft: false
url: /blog/2019/06/nav-497-released/
---

The seventh maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 8/9 (Jessie/Stretch) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. _Please be advised that the Debian 8 package will be discontinued soon_.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has also been updated.

#### Fixed GitHub issues in this release:

*   [#1882](https://github.com/Uninett/nav/issues/1882) (Invalid VLANs are generated from Juniper switches)
*   [#1920](https://github.com/Uninett/nav/issues/1920) (Provide a hook for adding extra information in the What-If tab in the IP Device Info page)
*   [#1946](https://github.com/Uninett/nav/issues/1946) (Vlans are categorized as linknets on Cisco Nexus with HSRP)
*   [#1953](https://github.com/Uninett/nav/issues/1953) (Adding new public filter in Alert Profiles fails)
*   [#1958](https://github.com/Uninett/nav/issues/1958) (NAV creates Graphite metrics with illegal characters in name)
*   [#1960](https://github.com/Uninett/nav/pull/1960) (Add option to control user administrator privileges from LDAP)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!