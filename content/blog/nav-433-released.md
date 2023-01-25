---
title: 'NAV 4.3.3 released'
date: 2016-01-15T00:38:00.000+01:00
draft: false
url: /blog/2016/01/nav-433-released/
tags: 
- release
- bugfix
- 4.3.3
- 4.3
---

_This is posted a while after the actual release_

Due to a critical bugfix in the NAV service monitor, we are releasing the third maintenance release of the NAV 4.3 series now. We urge anyone using NAV’s buil-in service monitor to upgrade as soon as possible.

The source code is available for download at [Launchpad](https://launchpad.net/nav/4.3/4.3.3). New packages for Debian Wheezy and Jessie have been published in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual (and the virtual appliance has been updated).

## Changes

The following reported bugs have been fixed:

*   [LP#1518950](https://bugs.launchpad.net/nav/+bug/1518950/) (machine tracker - form should reflect link parameters)
*   [LP#1519362](https://bugs.launchpad.net/nav/+bug/1519362/) (Forgetting to add a name to an alert profile causes template selection to be cleared in form)
*   [LP#1520119](https://bugs.launchpad.net/nav/+bug/1520119/) (Servicemon silently stops checking services after running for a while)

Happy NAVing everyone!
