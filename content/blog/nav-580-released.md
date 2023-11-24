---
title: 'NAV 5.8.0 released'
date: 2023-11-24T15:45:00.000+02:00
draft: false
tags:
- release
---

The first feature release of the 5.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, but hope to do
so by the end of 2023.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Added

- Initial SNMPv3 support added to most parts of NAV
  - Add an SNMPv3 management profile type ([#2693](https://github.com/Uninett/nav/issues/2693), [#2699](https://github.com/Uninett/nav/pull/2699))
  - Add SNMPv3 session support to the synchronous SNMP libraries used by most parts of NAV except ipdevpoll ([#2700](https://github.com/Uninett/nav/issues/2700), [#2710](https://github.com/Uninett/nav/pull/2710))
  - Add SNMPv3 reachability tests in SeedDB IP Device registration forms ([#2704](https://github.com/Uninett/nav/issues/2704), [#2734](https://github.com/Uninett/nav/pull/2734), [#2727](https://github.com/Uninett/nav/issues/2727), [#2730](https://github.com/Uninett/nav/pull/2730))
  - Add SNMPv3 support to Portadmin ([#2712](https://github.com/Uninett/nav/issues/2712), [#2731](https://github.com/Uninett/nav/pull/2731))
  - Add SNMPv3 support to `navsnmp` command line program ([#2724](https://github.com/Uninett/nav/issues/2724), [#2725](https://github.com/Uninett/nav/pull/2725))
  - Add SNMPv3 support to Arnold ([#2726](https://github.com/Uninett/nav/issues/2726), [#2733](https://github.com/Uninett/nav/pull/2733))
  - Add SNMPv3 session support to ipdevpoll's asynchronous SNMP libraries ([#2736](https://github.com/Uninett/nav/issues/2736), [#2743](https://github.com/Uninett/nav/pull/2743))
  - Add SNMPv3 support to`navoidverify` and `naventity` command line programs ([#2747](https://github.com/Uninett/nav/issues/2747), [#2748](https://github.com/Uninett/nav/pull/2748))
- Power-over-Ethernet configuration support for Cisco and Juniper equipment in PortAdmin ([#2632](https://github.com/Uninett/nav/issues/2632), [#2633](https://github.com/Uninett/nav/issues/2633), [#2666](https://github.com/Uninett/nav/pull/2666), [#2635](https://github.com/Uninett/nav/pull/2635), [#2759](https://github.com/Uninett/nav/pull/2759))
- Extract VLAN association from router port names on Checkpoint firewalls ([#2684](https://github.com/Uninett/nav/issues/2684), [#2701](https://github.com/Uninett/nav/pull/2701))
- Add link to our GitHub discussion forums in "Getting help" documentation ([#2746](https://github.com/Uninett/nav/pull/2746))
- Add subcommand to `navuser` command line program for deleting users ([#2705](https://github.com/Uninett/nav/pull/2705))
- Add toggle in `webfront.conf` for automatic creation of remote users ([#2698](https://github.com/Uninett/nav/issue/2698), [#2707](https://github.com/Uninett/nav/pull/2707))
- Add proper documentation index page for all howto guides ([#2716](https://github.com/Uninett/nav/pull/2716))


### Developer-centric additions

- Add tests for overview of alert profiles page  ([#2741](https://github.com/Uninett/nav/pull/2741))
- Add make rule for cleaning `doc` directory ([#2717](https://github.com/Uninett/nav/pull/2717))
- Add an snmpd service container for SNMPv3 comms testing ([#2697](https://github.com/Uninett/nav/pull/2697))

## Fixed

- Improve validation of maintenance form input in order to avoid unintentional crash reports ([#2757](https://github.com/Uninett/nav/pull/2757))
- Handle invalid alert profile ID form input without crashing ([#2756](https://github.com/Uninett/nav/pull/2756))
- Prevent crash errors in esoteric situations where multiple dashboards have been erroneously marked as a user's default dashboard ([#2680](https://github.com/Uninett/nav/pull/2680))
- Fix broken `navoidverify` command on Linux ([#2737](https://github.com/Uninett/nav/pull/2737))
- Several regressions related to input validation in Alert Profiles were fixed:
  - Fix regression that prevented filter groups from being deleted from an alert profile ([#2729](https://github.com/Uninett/nav/pull/2729))
  - Fix regression that prevented activation/deactivation of alert profiles ([#2732](https://github.com/Uninett/nav/pull/2732))
  - Fix form validation with "equal" and "in" operators for adding expression with group to filter ([#2750](https://github.com/Uninett/nav/pull/2750))
  - Add more expression operator tests for alert profiles and fix cleaning in `ExpressionForm` ([#2752](https://github.com/Uninett/nav/pull/2752))

### Developer-centric fixes

- Restructure alert profile tests ([#2739](https://github.com/Uninett/nav/pull/2739))

## Changed

- Allow write-enabled SNMP profiles to be used for reading when device has no read-only SNMP profiles ([#2735](https://github.com/Uninett/nav/issues/2735), [#2751](https://github.com/Uninett/nav/pull/2751))
- Improved howto guide for setting up remote user authentication using `mod_auth_oidc` ([#2708](https://github.com/Uninett/nav/pull/2708))

### Developer-centric changes

- Refactored web authentication code in preparation for future changes to authentication flow ([#2706](https://github.com/Uninett/nav/pull/2706))

## Removed

### Developer-centric removals

- Remove remaining uses of `Netbox.snmp_version` ([#2522](https://github.com/Uninett/nav/issues/2522))
- Remove unused function `snmp_parameter_factory` ([#2753](https://github.com/Uninett/nav/pull/2753))
- Remove deprecated Netbox SNMP properties ([#2754](https://github.com/Uninett/nav/pull/2754), [#2761](https://github.com/Uninett/nav/pull/2761))



## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-8) before upgrading.

Happy NAVing everyone!

