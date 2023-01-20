---
title: 'NAV 5.5.2 released'
date: 2022-11-10T10:23:00.000+02:00
draft: false
url: /blog/2022/11/nav-552-released/
---

The second maintenance release of the 5.5 series of NAV is now out,
fixing a couple of serious collection and trap processing issues!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated, but currently, the automated
GitHub workflows aren't working due to changes at GitHub.


Fixed
-------

*   Fix serious collection breakdown in ipdevpoll by re-generating a valid Python representation of CISCO-ENHANCED-MEMPOOL-MIB ([#2494](https://github.com/Uninett/nav/issues/2494), [#2495](https://github.com/Uninett/nav/pull/2495))
*   Fix broken trap processing in snmptrapd ([#2497](https://github.com/Uninett/nav/issues/2497), [#2498](https://github.com/Uninett/nav/pull/2498))


Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.5.x/release-notes.html#nav-5-5) before upgrading.

Happy NAVing everyone!
