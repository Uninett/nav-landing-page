---
title: 'NAV 5.1 released'
date: 2020-11-26T15:48:00.000+01:00
draft: false
url: /blog/2020/11/nav-51-released/
tags:
- release
---

The initial feature release of the 5.1 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. Packages for Debian 9 (Stretch) have been discontinued.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## User-visible features and improvements

*   [#2021](https://github.com/Uninett/nav/issues/2021) (Add SeedDB action to clone netboxes and rooms )
*   [#2051](https://github.com/Uninett/nav/issues/2051) (Link to affected devices in Management profile)
*   [#2128](https://github.com/Uninett/nav/pull/2128) (Add device filtering options to ipdevpoll and pping, to enable support for horizontal scaling and distributed monitoring)
*   [#2175](https://github.com/Uninett/nav/pull/2175) (Implement NAPALM management profiles and connectivity)
*   [#2185](https://github.com/Uninett/nav/pull/2185) (Modernize the type dumping script and make it available as an installable script for end user use)
*   [#2204](https://github.com/Uninett/nav/pull/2204) (Add support for configuring Juniper switch ports in PortAdmin)
    *   [#2173](https://github.com/Uninett/nav/pull/2173) (Clean up PortAdmin ManagementHandler interface)
    *   [#2112](https://github.com/Uninett/nav/pull/2112) (Refactor PortAdmin's SNMP back-end classes and factories)
    *   [#2115](https://github.com/Uninett/nav/pull/2115) (Refactor portadmin configuration parsing bits)
    *   [#2121](https://github.com/Uninett/nav/pull/2121) (Use nav.config.NAVConfigParser for PortAdmin configuration)
    *   [#2205](https://github.com/Uninett/nav/pull/2205) (Adapt Portadmin UI workflow to meet needs of multiple backend protocols)

## Fixed GitHub issues in this release

*   [#2078](https://github.com/Uninett/nav/issues/2078) (\[BUG\] NAV daemons are unnecessarily run as root)
*   [#2103](https://github.com/Uninett/nav/pull/2103) (Support Django 2.2)
*   [#2139](https://github.com/Uninett/nav/issues/2139) (\[BUG\] fanState and psuState e-mail alerts say "no message template is defined")
*   [#2141](https://github.com/Uninett/nav/pull/2141) (Work around lack of entity names when collecting sensors from Arista devices)
*   [#2174](https://github.com/Uninett/nav/issues/2174) (\[BUG\] PortAdmin never issues a "write mem" operation when editing trunks)
*   [#2190](https://github.com/Uninett/nav/issues/2190) (\[BUG\] Regression - mysql service check does not work)
*   [#2197](https://github.com/Uninett/nav/issues/2197) (\[BUG\] Bottom part of room images are obscured by image caption)
*   [#2198](https://github.com/Uninett/nav/issues/2198) (\[BUG\] CSV export from Netbox interfaces in Room view produce wrong filename and content.)
*   [#2199](https://github.com/Uninett/nav/issues/2199) (Make servicemon HttpChecker use the port number from the URL, if present)
*   [#2207](https://github.com/Uninett/nav/pull/2207) (Netbox reference is not passed to customization template for the ipdevinfo "What if" tab)
*   [#2213](https://github.com/Uninett/nav/issues/2213) (\[BUG\] NAV does not import room position)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/5.1/release-notes.html#nav-5-1) when upgrading.

Happy NAVing everyone!
