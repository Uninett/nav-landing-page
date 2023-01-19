---
title: 'NAV 4.9.4 released'
date: 2019-03-28T08:53:00.000+01:00
draft: false
url: /blog/2019/03/nav-494-released/
---

The fourth maintenance release of the 4.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 8/9 (Jessie/Stretch) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

The Debian packages for NAV 4.9 have been rebuilt using dh-virtualenv, which means that most of the Python dependencies are now embedded into the packages themselves. If you have previously added a priority apt pin for packages from apt.uninett.no, you may now remove it, as there are no longer any other packages needed from that repository to run NAV.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance has also been updated.

**NB: This release introduces a new dependency to `py2-ipaddress==3.4.1`**

## Fixed GitHub issues in this release:

*   [#1639](https://github.com/Uninett/nav/issues/1639) (Not all NAV programs respect TIME\_ZONE from nav.conf)
*   [#1762](https://github.com/Uninett/nav/issues/1762) (navdump drops function-data)
*   [#1788](https://github.com/Uninett/nav/issues/1788) (Deleting an alert profile subscription that has queued alerts will cause alertengine to process all those alerts as if they were new ones on the queue. )
*   [#1885](https://github.com/Uninett/nav/issues/1885) (LDAP authentication against Microsoft AD using suffix bind is broken in NAV 4.9)
*   [#1894](https://github.com/Uninett/nav/issues/1894) (Terminals that don't support colors cause nav start/stop commands to crash)
*   [#1895](https://github.com/Uninett/nav/issues/1895) (Verify nav.conf values as part of nav start)
*   [#1896](https://github.com/Uninett/nav/issues/1896) (UnicodeEncodeError when LDAP user with non-ASCII characters in DN logs in)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!
