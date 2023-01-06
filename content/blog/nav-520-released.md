---
title: 'NAV 5.2.0 released'
date: 2021-09-16T11:09:00.000+02:00
draft: false
url: /blog/2021/09/nav-520-released/
---

The initial feature release of the 5.2 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 11 (Bullseye) have not been built yet.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### User-visible features and improvements:

*   [#1928](https://github.com/Uninett/nav/issues/1928) (Document 802.1X support of PortAdmin for end users)
*   [#2289](https://github.com/Uninett/nav/pull/2289) (Add config option to disallow editing of uplinks and downlinks in PortAdmin)
*   [#2295](https://github.com/Uninett/nav/pull/2295) (Redefine alert severity levels and make them configurable)
*   [#2297](https://github.com/Uninett/nav/pull/2297) (Document the event and alert type hierarchy)

#### Fixed GitHub issues in this release

*   [#2296](https://github.com/Uninett/nav/issues/2296) (\[BUG\] Portadmin save API incorrectly returns 500 error where 400 is appropriate)
*   [#2298](https://github.com/Uninett/nav/issues/2298) (\[BUG\] PortAdmin RpcError on JunOS 20 and newer)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.2.x/release-notes.html#nav-5-2) when upgrading.

Happy NAVing everyone!