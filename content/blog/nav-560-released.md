---
title: 'NAV 5.6.0 released'
date: 2023-01-20T14:00:00.000+02:00
draft: false
url: /blog/2023/01/nav-560-released/
tags:
- release
---

The first feature release of the 5.6 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as
usual.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Added

### User-visible features

- NAPALM/NETCONF management profiles can now be configured with custom timeout values ([#2460](https://github.com/Uninett/nav/pull/2460), [#2390](https://github.com/Uninett/nav/issues/2390))
- Post lifecycle events the first time new chassis/module/PSU/fan devices are seen ([#2391](https://github.com/Uninett/nav/issues/2391), [#2414](https://github.com/Uninett/nav/pull/2414))
- Accept JSON Web Tokens signed by third-parties as valid API authentication/authorization tokens ([#2483](https://github.com/Uninett/nav/issues/2483), [#2511](https://github.com/Uninett/nav/pull/2511))
- Collect "chassis" serial numbers from Aruba wireless controllers ([#2514](https://github.com/Uninett/nav/pull/2514))
- Added an API endpoint for module information ([#2517](https://github.com/Uninett/nav/issues/2517), [#2520](https://github.com/Uninett/nav/pull/2520))
- Result caching added to ranked statistics - including the ability to populate the cache regularly behind-the-scenes in a cronjob (([#1504](https://github.com/Uninett/nav/issues/1504), [#2398](https://github.com/Uninett/nav/pull/2398))

### Developer-centric features

- Added `buglog.py` option to fetch issue numbers from git reflog ([#2474](https://github.com/Uninett/nav/pull/2474))
- Added tests for  `get_memory_usage` for all memory MIBs ([#2376](https://github.com/Uninett/nav/issues/2376), [#2441](https://github.com/Uninett/nav/pull/2441))
- Added tests to discover invalid MIB dumps from smidump ([#2501](https://github.com/Uninett/nav/issues/2501), ([#2521](https://github.com/Uninett/nav/pull/2521))
- Updated/added explicit relation names to various ORM models ([#2539](https://github.com/Uninett/nav/pull/2539), [#2540](https://github.com/Uninett/nav/pull/2540), [#2541](https://github.com/Uninett/nav/pull/2541), [#2542](https://github.com/Uninett/nav/pull/2542))

## Fixed

### User-visible fixes

- Empty alert messages are no longer sent when device software upgrades are detected ([#2533](https://github.com/Uninett/nav/issues/2533))
- Merged two fixes from the 5.4.x stable series that never actually made it into the 5.5 series:
  - Metric values of *0.0* are evaluated correctly by threshold rules ([#2447](https://github.com/Uninett/nav/issues/2447))
  - Validate maintenance calendar input form to avoid e-mail spam from bots scanning for vulnerabilities ([#2420](https://github.com/Uninett/nav/issues/2420), [#2431](https://github.com/Uninett/nav/pull/2431))
- Properly log (for posterity) old and new revision numbers with every software/hardware/firmware upgrade event NAV posts ([#2515](https://github.com/Uninett/nav/pull/2515), [#2545](https://github.com/Uninett/nav/pull/2545), [#2560](https://github.com/Uninett/nav/pull/2560))
- snmpwalk routine for synchronous NAV code now correctly handles end-of-mib-view errors ([#1925](https://github.com/Uninett/nav/issues/1925), [#2489](https://github.com/Uninett/nav/pull/2489))
- Removed deprecation warnings from command line programs `navsnmp`, `naventity` and `navoidverify` ([#2389](https://github.com/Uninett/nav/issues/2389), [#2429](https://github.com/Uninett/nav/pull/2429))

### Developer-centric fixes

- Use pip-compile's backtracking dependency resolver to fix failing CI pipelines ([#2509](https://github.com/Uninett/nav/pull/2509))
- Updated libsnmp dependency for newer Ubuntu runners in GitHub pipelines ([#2532](https://github.com/Uninett/nav/pull/2532))
- Use same version of Django for pylint runs as the latest stable release ([#2536](https://github.com/Uninett/nav/pull/2536))
- Fixed a slew of new CI pipeline / test suite problems that appear after new years ([#2537](https://github.com/Uninett/nav/pull/2537))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.6.x/release-notes.html#nav-5-6) before upgrading.

Happy NAVing everyone!

