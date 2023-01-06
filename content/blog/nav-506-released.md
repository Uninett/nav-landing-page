---
title: 'NAV 5.0.6 released'
date: 2020-08-27T16:37:00.001+02:00
draft: false
url: /blog/2020/08/nav-506-released/
---

The sixth maintenance release of the 5.0 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 9/10 (Stretch/Buster) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual.

Please also be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Deprecation warning

Python 2 reached its end-of-life on **January 1, 2020**. NAV 5.0 therefore moves to Python 3, and as such, you will need at least Python 3.5 to run NAV.

Most of NAV will still run on Python 2 as of the 5.0 release, but from this point, Python 2 will be deprecated and we will start removing code that exists solely to keep compatibility with Python 2.

#### Fixed GitHub issues in this release:

*   [#2144](https://github.com/Uninett/nav/pull/2144) (Prevent ipdevinfo from crashing on weird device names)
*   [#2149](https://github.com/Uninett/nav/issues/2149) (Inventory failing on DLink DGS-1100 : 'TypeError: argument of type 'int' is not iterable')
*   [#2150](https://github.com/Uninett/nav/issues/2150) (\[BUG\] Interface down is causing widget 'status' to display 'Could not load widget' due to HTTP 500)
*   [#2165](https://github.com/Uninett/nav/issues/2165) (\[BUG\] Delayed delivery alert subscriptions in single time period alert profiles are never sent)
*   [#2167](https://github.com/Uninett/nav/pull/2167) (Fix potential typecast issue with SQL migration to NAV 5.0)
*   [#2169](https://github.com/Uninett/nav/issues/2169) (\[BUG\] macwatch.py crashes when logging notifications about found MAC addresses)
*   [#2170](https://github.com/Uninett/nav/issues/2170) (\[BUG\] Alertengine stops dispatching Slack notifications indefinitely if Slack complains of too many requests)
*   [#2171](https://github.com/Uninett/nav/pull/2171) (Warn about user accounts that have issues with their passwords)
*   [#2172](https://github.com/Uninett/nav/pull/2172) (Prevent login/password changes to default account)
*   [#2177](https://github.com/Uninett/nav/issues/2177) (\[BUG\] Attempting to move IP devices to another room crashes SeedDB)
*   [#2178](https://github.com/Uninett/nav/issues/2178) (\[BUG\] PDU widget stops displaying properly if room is deleted)
*   [#2179](https://github.com/Uninett/nav/issues/2179) (\[BUG\] UPS widget does not display properly if UPS is deleted from NAV)
*   [#2180](https://github.com/Uninett/nav/issues/2180) (\[BUG\] Entering invalid dates in Device History search form causes crash)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.0/release-notes.html#nav-5-0) when upgrading.

Happy NAVing everyone!