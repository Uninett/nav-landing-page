---
title: 'NAV 5.0.3 released'
date: 2019-12-19T13:50:00.002+01:00
draft: false
url: /2019/12/nav-503-released.html
---

The third maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Deprecation warning

Python 2 reaches its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

#### Fixed GitHub issues in this release:

*   [#2015](https://github.com/Uninett/nav/issues/2015) (Broken Mikrotik LLDP-MIB implementation causes ipdevpoll LLDP plugin to crash)
*   [#2055](https://github.com/Uninett/nav/pull/2055) (\[BUG\] Navlets crash/appear blank if their config is stored as legacy pickles)
*   [#2057](https://github.com/Uninett/nav/pull/2057) (Make servicemon run on Python 3)
*   [#2058](https://github.com/Uninett/nav/issues/2058) (\[BUG\] navpgdump crashes with TypeError on Python 3 if exclusion options are provided)
*   [#2059](https://github.com/Uninett/nav/pull/2059) (\[BUG\] Coriant Groove sensors names appear as reprs of bytes objects under Python 3)
*   [#2060](https://github.com/Uninett/nav/issues/2060) (\[BUG\] smsd gammudispatcher error handling fails on Python 3)
*   [#2061](https://github.com/Uninett/nav/issues/2061) (\[BUG\] silent\_include tag template crashes any view that uses it)
*   [#2062](https://github.com/Uninett/nav/issues/2062) (\[BUG\] ipdevpoll considers the same devices changed on every reload loop, causing massive scheduling problems)
*   [#2063](https://github.com/Uninett/nav/pull/2063) (Massively reduce the number of queries produced by the API /alert endpoint)
*   [#2065](https://github.com/Uninett/nav/issues/2065) (\[BUG\] some servicemon checker runs crash with a UnboundLocalError)
*   [#2066](https://github.com/Uninett/nav/pull/2066) (Increase the max number of shown alerts in Status page to 1000 and provide feedback spinner when loading data)
*   [#2067](https://github.com/Uninett/nav/issues/2067) (\[BUG\] Alertengine Slack dispatcher fails with TypeError)
*   [#2068](https://github.com/Uninett/nav/issues/2068) (\[BUG\] Workaround for faulty Aruba ENTITY-MIB::entLogicalTable implementation crashes with TypeError on Python 3)
*   [#2069](https://github.com/Uninett/nav/issues/2069) (\[BUG\] ipdevpoll inventory job crashes with a Django ValidationError)
*   [#2070](https://github.com/Uninett/nav/issues/2070) (\[BUG\] Servicemon SMTP checker fails with " a bytes-like object is required, not 'str'")
*   [#2071](https://github.com/Uninett/nav/issues/2071) (\[BUG\] Active maintenance task list crashes when tasks contain deleted IP devices)
*   [#2072](https://github.com/Uninett/nav/issues/2072) (\[BUG\] Servicemon RadiusChecker always fails with "secret must be a binary string" message)
*   [#2073](https://github.com/Uninett/nav/issues/2073) (\[BUG\] Room image upload crashes with a TypeError)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!