---
title: 'NAV 5.1.3 released'
date: 2021-04-09T09:51:00.000+02:00
draft: false
url: /blog/2021/04/nav-513-released/
---

The third maintenance release of the 5.1 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 9 (Stretch) have been discontinued.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

#### Fixed GitHub issues in this release

*   [#2159](https://github.com/Uninett/nav/issues/2159) (\[BUG\] UPS widget is inconsistent between showing minutes and seconds remaining time)
*   [#2240](https://github.com/Uninett/nav/issues/2240) (\[BUG\] Workaround for wrong interface speed SNMP implementations)
*   [#2253](https://github.com/Uninett/nav/pull/2253) (Drastically improve page load times on maintenance edit form)
*   [#2254](https://github.com/Uninett/nav/issues/2254) (\[BUG\] Search after partial IP-address crashes)
*   [#2255](https://github.com/Uninett/nav/issues/2255) (ipdevinfo maintenance task link should be to task details view, not the task editor)
*   [#2257](https://github.com/Uninett/nav/pull/2257) (Exclude Coriant Groove port sensors from collection based on portAdminStatus)
*   [#2260](https://github.com/Uninett/nav/issues/2260) (IP Device custom data should be "urlized")
*   [#2263](https://github.com/Uninett/nav/issues/2263) (\[BUG\] Job 'inventory' for xxx aborted: Job aborted due to save failure (cause=ValueError('A string literal cannot contain NUL (0x00) characters.')))
*   [#2264](https://github.com/Uninett/nav/issues/2264) (Hardcoded vendor name)
*   [#2267](https://github.com/Uninett/nav/issues/2267) (Link to filtered report must be urlencoded)
*   [#2269](https://github.com/Uninett/nav/issues/2269) (\[BUG\] ipdevinfo shows empty Function-field for some hosts)
*   [#2270](https://github.com/Uninett/nav/issues/2270) (\[BUG\] Documentation search does not work)
*   [#2275](https://github.com/Uninett/nav/issues/2275) (SshChecker not handling connections properly)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.1/release-notes.html#nav-5-1) when upgrading.

Happy NAVing everyone!