---
title: 'NAV 5.5.1 released'
date: 2022-11-09T09:24:00.000+02:00
draft: false
url: /blog/2022/11/nav-551-released/
tags:
- release
---

The first maintenance release of the 5.5 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated, but currently, the automated
GitHub workflows aren't working due to changes at GitHub.


Fixed
-------

*   Delete and ignore module devices with fake serial number `BUILTIN`, as reported by Juniper equipment, in order to avoid spamming with `device[SFH]wUpgrade` alerts ([#2491](https://github.com/Uninett/nav/issues/2491), [#2492](https://github.com/Uninett/nav/pull/2492))

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.5.x/release-notes.html#nav-5-5) before upgrading.

Happy NAVing everyone!
