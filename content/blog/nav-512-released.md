---
title: 'NAV 5.1.2 released'
date: 2021-01-15T10:45:00.003+01:00
draft: false
url: /2021/01/nav-512-released.html
---

The second maintenance release of the 5.1 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 9 (Stretch) have been discontinued.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Fixed GitHub issues in this release

*   [#2210](https://github.com/Uninett/nav/issues/2210) (\[BUG\] Traffic graphs use the SI unit system rather than binary prefixes)
*   [#2215](https://github.com/Uninett/nav/issues/2215) (\[BUG\] NAV will refuse to identify LLDP remote port names that contain trailing NUL bytes)
*   [#2235](https://github.com/Uninett/nav/issues/2235) (\[BUG\] TypeError at /alertprofiles/filters/add-expression/ _init_\_() takes 1 positional argument but 2 were given)
*   [#2238](https://github.com/Uninett/nav/issues/2238) (\[BUG\] Geomap doesn't work if DOMAIN\_SUFFIX is not set in nav.conf)
*   [#2239](https://github.com/Uninett/nav/issues/2239) (\[BUG\] using DOMAIN\_SUFFIX breaks netbox links in Geomap)
*   [#2241](https://github.com/Uninett/nav/issues/2241) (Allow custom tabs for port details view)
*   [#2250](https://github.com/Uninett/nav/pull/2250) (Fix formatting of small and negative numbers in Rickshaw graphs)
*   [#2252](https://github.com/Uninett/nav/pull/2252) (Fix broken serial numbers for Juniper, APC PowerNet and old HP devices)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.1/release-notes.html#nav-5-1) when upgrading.

Happy NAVing everyone!