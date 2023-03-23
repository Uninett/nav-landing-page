---
title: 'NAV 5.6.1 released'
date: 2023-03-23T12:04:00.000+02:00
draft: false
tags:
- release
---

The first maintenance release of the 5.6 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as
usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Fixed

### User-visible fixes
- Ensure event variables are always posted in transactions, so the event engine does not accidentally end up processing incomplete event information ([#2594](https://github.com/Uninett/nav/pull/2594))
- Report broken cache configuration as an error in Ranked Statistics tool, rather than taking down the whole NAV site ([#2561](https://github.com/Uninett/nav/issues/2561), [#2563](https://github.com/Uninett/nav/pull/2563))
- Show error message on invalid ip address in ipdevinfo ([#2590](https://github.com/Uninett/nav/pull/2590), [#2589](https://github.com/Uninett/nav/issues/2589))
- Link to correct room in room report if room has a space in its name ([#2593](https://github.com/Uninett/nav/pull/2593), [#2592](https://github.com/Uninett/nav/issues/2592))
- Work around duplicate internal serial numbers in Juniper equipment by trusting data only from the device with the lowest entity index ([#2583](https://github.com/Uninett/nav/pull/2583), [#2493](https://github.com/Uninett/nav/issues/2493))
- Make save function in AlertHistory, EventHistory and AlertQueue atomic  ([#2594](https://github.com/Uninett/nav/pull/2594))
- Ignore LDAP server referral responses, rather then erroring out during the login process ([#2576](https://github.com/Uninett/nav/pull/2576), [#1166](https://github.com/Uninett/nav/issues/1166))
- Include the `new_version` variable in alert message templates for device hw/fw/sw upgrades ([#2565](https://github.com/Uninett/nav/pull/2565))
- Update NAV blog widget to use the new blog URL ([#2585](https://github.com/Uninett/nav/pull/2585))
- Handle invalid IP address input in ipdevinfo device searches gracefully, rather then crashing with a 500 error ([#2589](https://github.com/Uninett/nav/issues/2589), [#2590](https://github.com/Uninett/nav/pull/2590))
- Fix broken links to room details from room report for rooms with spaces in their names ([#2592](https://github.com/Uninett/nav/issues/2592), [#2593](https://github.com/Uninett/nav/pull/2593)))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.6.x/release-notes.html#nav-5-6) before upgrading.

Happy NAVing everyone!

