---
title: 'NAV 5.7.0 released'
date: 2023-09-07T15:30:00.000+02:00
draft: false
tags:
- release
---

The first feature release of the 5.7 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, but hope to do
so by the end of 2023.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Added

- Even more complex and flexible configuration of NAV logging is now supported through `logging.yml` ([#2659](https://github.com/Uninett/nav/pull/2659))
- Added howto guide for log configuration ([#2660](https://github.com/Uninett/nav/pull/2660))
- Currently non-functional (aka. "blacklisted") alert sender mechanisms are now flagged in the Alert Profiles tool wherever an affected alert address is displayed ([#2653](https://github.com/Uninett/nav/issues/2653), [#2664](https://github.com/Uninett/nav/issues/2664), [#2677](https://github.com/Uninett/nav/pull/2677), [#2678](https://github.com/Uninett/nav/pull/2678))
- Added support for polling and alerting on Juniper chassis and system alerts ([#2358](https://github.com/Uninett/nav/issues/2358), [#2388](https://github.com/Uninett/nav/pull/2388))
  - Juniper only provides alert counters via SNMP, no alert details, unfortunately.
  - Since NAV doesn't support alert state updates, a new eventengine plugin handles alert count transitions by resolving old alerts and creating new ones ([#2432](https://github.com/Uninett/nav/issues/2432), [#2519](https://github.com/Uninett/nav/pull/2519))
- Added a new `contains_address` filter to the `prefix` API endpoint, to enable lookup of matching prefix/vlan details from a single IP or subnet address ([#2577](https://github.com/Uninett/nav/issues/2577), [#2578](https://github.com/Uninett/nav/pull/2578))
- Defined and added abstract methods for Power-over-Ethernet configuration to PortAdmin management handler classes ([#2636](https://github.com/Uninett/nav/pull/2636))
  - These are needed for the upcoming vendor specific implementations of PoE config in PortAdmin.
- Implemented configuration file parsing for upcoming local JWT token feature ([#2568](https://github.com/Uninett/nav/pull/2568))

## Fixed

### User-visible fixes

- Properly dispose of outgoing alert notifications to invalid alert addresses ([#2661](https://github.com/Uninett/nav/pull/2661))
- Fixed crash when attempting to log device errors with an empty comment in the Device History tool ([#2579](https://github.com/Uninett/nav/issues/2579), [#2580](https://github.com/Uninett/nav/pull/2580))
- Fixed bad styling and missing linebreaks in traceback section of the 500 error page ([#2607](https://github.com/Uninett/nav/issues/2607), [#2628](https://github.com/Uninett/nav/pull/2628))
- Show help text instead of error when running `nav` command without arguments ([#2601](https://github.com/Uninett/nav/issues/2601), [#2603](https://github.com/Uninett/nav/pull/2603))
- Prevent users from entering invalid `sysObjectID` values when editing Netbox types in SeedDB ([#2584](https://github.com/Uninett/nav/pull/2584), [#2566](https://github.com/Uninett/nav/issues/2566))
- Removed upper version bound for *Pillow* image manipulation library, to fix security warnings ([#2567](https://github.com/Uninett/nav/pull/2567))
- Alerts that cannot be sent due to blacklisted media plugins will no longer fill up `alertengine.log` every 30 seconds, unless DEBUG level logging is enabled ([#1787](https://github.com/Uninett/nav/issues/1787), [#2652](https://github.com/Uninett/nav/pull/2652))
- DNS lookups in ipdevinfo are now properly case insensitive ([#2615](https://github.com/Uninett/nav/issues/2615), [#2650](https://github.com/Uninett/nav/pull/2650))
- Alert Profiles will now properly require Slack alert addresses to be valid URLs ([#2657](https://github.com/Uninett/nav/pull/2657))
- 5 minute and 15 minute load average values will now be collected correctly for Juniper devices ([#2671](https://github.com/Uninett/nav/issues/2671), [#2672](https://github.com/Uninett/nav/pull/2672))
- Fix cabling API, which broke due to internal refactorings ([#2621](https://github.com/Uninett/nav/pull/2621))
- Only install NAV's custom `epollreactor2` in ipdevpoll if running on Linux ([#2503](https://github.com/Uninett/nav/issues/2503), [#2604](https://github.com/Uninett/nav/pull/2604))
  - Stops ipdevpoll from crashing on BSDs.

### Developer-centric fixes

- Moved more of NAV's packaging definition to `pyproject.toml` ([#2655](https://github.com/Uninett/nav/pull/2655))
- Pin pip to version 23.1.0 for CI pipelines to continue working ([#2647](https://github.com/Uninett/nav/pull/2647))
- Improve ipdevpoll logging of SQL queries and from Twisted library ([#2640](https://github.com/Uninett/nav/pull/2640))
- Stop making skipped validation tests for non HTML content ([#2623](https://github.com/Uninett/nav/pull/2623))
- Version-locked indirect dependencies of test suites ([#2622](https://github.com/Uninett/nav/pull/2622), [#2617](https://github.com/Uninett/nav/issues/2617))
- Improve SNMP forwarding/proxying container setup, including adding IPv6 support ([#2637](https://github.com/Uninett/nav/pull/2637), [#2516](https://github.com/Uninett/nav/pull/2516))
- Documented a recipe for establishing SNMP tunnels when testing devices on otherwise unreachable networks ([#2426](https://github.com/Uninett/nav/issues/2426), [#2435](https://github.com/Uninett/nav/pull/2435))
- Run Django development web server in "insecure" mode to improve simulation of a production environment when debug flag is turned off ([#2625](https://github.com/Uninett/nav/pull/2625))
- Added a proper docstring to `bootstrap_django()` function ([#2619](https://github.com/Uninett/nav/pull/2619), [#2168](https://github.com/Uninett/nav/issues/2168))
- Stop restoring stale tox environment caches in GitHub workflows ([#2605](https://github.com/Uninett/nav/pull/2605))
- Added tests for ipdevpoll worker euthanization ([#2599](https://github.com/Uninett/nav/pull/2599), [#2548](https://github.com/Uninett/nav/issues/2548))
- Added tests to ensure snmptrapd can properly look up a NAV router that sends traps from one of its non-management IP addresses ([#2500](https://github.com/Uninett/nav/issues/2500), [#2510](https://github.com/Uninett/nav/pull/2510))
- Avoid redundant graphite time formatting strings by re-using constant ([#2588](https://github.com/Uninett/nav/pull/2588), [#2543](https://github.com/Uninett/nav/issues/2543))
- Make detection of running in a virtualenv more compatible with modern toolchain ([#2573](https://github.com/Uninett/nav/pull/2573))
- Revert to having tox run its own dependency installer ([#2572](https://github.com/Uninett/nav/pull/2572))
- Added explicit back-relation names for several Django ORM models ([#2544](https://github.com/Uninett/nav/pull/2544), [#2546](https://github.com/Uninett/nav/pull/2546), [#2547](https://github.com/Uninett/nav/pull/2547), [#2549](https://github.com/Uninett/nav/pull/2549), [#2550](https://github.com/Uninett/nav/pull/2550), [#2551](https://github.com/Uninett/nav/pull/2551))


## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-7) before upgrading.

Happy NAVing everyone!

