---
title: 'NAV 4.9 released'
date: 2019-02-14T12:02:00.000+01:00
draft: false
url: /blog/2019/02/nav-49-released/
---

During a two-week whirlwind, three releases have been made in the new 4.9 series of NAV.

As the primary objective of the 4.9 release series was to move to some newer (non-outdated) versions of NAV's dependencies, especially Django (with which we still have a way to go), lots of little regressions snuck up on us in the 4.9.0 and 4.9.1 releases. Thankfully, our ever watchful users diligently reported their problems back to us.

Copyright changes
-----------------

NAV 4.9 introduced a previously announced license change. NAV is now licensed under the GNU General Public License v3. This change was primarily needed in order to be compatible with severale Apache 2.0-licensed libraries that we want to utilize in future NAV versions.

Changes
-------

Let's look at some of the functional changes introduced by these three releases:

### Version 4.9.2

(released 14 Feb 2019)

#### User-visible features and improvements:

*   [#1837](https://github.com/UNINETT/nav/issues/1837/) (Save config to non volatile memory in portadmin for dell switches)
*   [#1853](https://github.com/UNINETT/nav/issues/1853/) (The navuser command should have an option to verify a user's passord)

#### Fixed GitHub issues in this release:

*   [#1784](https://github.com/UNINETT/nav/issues/1784/) (Breadcrumb missing from /useradmin/tokens/)
*   [#1834](https://github.com/UNINETT/nav/issues/1834/) (AlertEngine fails to send email if EMAIL\_PORT is present in nav.conf)
*   [#1839](https://github.com/UNINETT/nav/issues/1839/) (The interfaces API endpoint crashes when using the last\_used filter)
*   [#1841](https://github.com/UNINETT/nav/issues/1841/) (Useradmin Token listing crashes on NAV 4.9.1 if any tokens are created with no endpoint list)
*   [#1842](https://github.com/UNINETT/nav/issues/1842/) (Netmap layer 3 graph API endpoint crashes on NAV 4.9.1)
*   [#1844](https://github.com/UNINETT/nav/issues/1844/) (PortAdmin crashes with TypeError if an ifaliasformat is configured)
*   [#1846](https://github.com/UNINETT/nav/issues/1846/) (IPAM fails under NAV 4.9.1 if any Organization object has non-ASCII characters in description)
*   [#1847](https://github.com/UNINETT/nav/issues/1847/) ("Rooms with active alerts" widget fails under NAV 4.9.1)
*   [#1848](https://github.com/UNINETT/nav/issues/1848/) (Stateless alerts are shown in status widget even when checkbox is left unchecked)
*   [#1851](https://github.com/UNINETT/nav/issues/1851/) (Fix searching for other things than ip addresses in portadmin)
*   [#1852](https://github.com/UNINETT/nav/issues/1852/) (Empty NAVbar search results in ValueError crash)

### Version 4.9.1

(released 07 Feb 2019)

#### Fixed GitHub issues in this release:

*   [#1820](https://github.com/UNINETT/nav/issues/1820/) (ipdevpoll will not schedule jobs under NAV 4.9.0)
*   [#1822](https://github.com/UNINETT/nav/issues/1822/) (Command line argument support for nav daemon startup config)
*   [#1823](https://github.com/UNINETT/nav/issues/1823/) (Old switch port layout screen is blank in NAV 4.9.0)
*   [#1824](https://github.com/UNINETT/nav/issues/1824/) (navdump crashes when dumping service table)
*   [#1825](https://github.com/UNINETT/nav/issues/1825/) (Alertprofiles crashes when attempting to delete matchfield)
*   [#1826](https://github.com/UNINETT/nav/issues/1826/) (Device history crashes when attempting to browse the history of an IP Device)
*   [#1827](https://github.com/UNINETT/nav/issues/1827/) (Any l2trace search will crash with a Django FieldError)
*   [#1828](https://github.com/UNINETT/nav/issues/1828/) (PDU dashboard widget crashes under NAV 4.9.0)
*   [#1829](https://github.com/UNINETT/nav/issues/1829/) (Any toolbox descriptor file containing superfluous equal signs will be silently ignored by the web interface)
*   [#1830](https://github.com/UNINETT/nav/issues/1830/) (MAC address prefix filters are horribly slow in arp and cam API endpoints)
*   [#1831](https://github.com/UNINETT/nav/issues/1831/) (Threshold monitor crashes if rule returns Graphite error)

### Version 4.9.0

(released 31 Jan 2019)

#### User-visible features and improvements:

*   [#1423](https://github.com/UNINETT/nav/issues/1423/) (Add API endpoint for accounts and account groups)
*   [#1509](https://github.com/UNINETT/nav/issues/1509/) (Add active alerts tab for port details page)
*   [#1646](https://github.com/UNINETT/nav/issues/1646/) (Add event/alert details page)
*   [#1615](https://github.com/UNINETT/nav/issues/1615/) (Room view - want device/interface count)
*   [#1624](https://github.com/UNINETT/nav/issues/1624/) (Add support for Dell DNOS-SWITCHING-MIB)
*   [#1659](https://github.com/UNINETT/nav/issues/1659/) (Add an interface browser tool)
*   [#1662](https://github.com/UNINETT/nav/issues/1662/) (Business reports, device availability - filter for maintenance)
*   [#1667](https://github.com/UNINETT/nav/issues/1667/) (More interface information for linkState alerts in status tool/widget)
*   [#1705](https://github.com/UNINETT/nav/issues/1705/) (Enable use of api endpoint without specifying version)
*   [#1706](https://github.com/UNINETT/nav/issues/1706/) (Audit log when users operates as other user)
*   [#1739](https://github.com/UNINETT/nav/issues/1739/) (PortAdmin - users should not be able to set trunk on port)
*   [#1758](https://github.com/UNINETT/nav/issues/1758/) (Writable vlan and prefix endpoints)
*   [#1761](https://github.com/UNINETT/nav/issues/1761/) (API netbox endpoint: filter on type\_\_name)
*   [#1791](https://github.com/UNINETT/nav/issues/1791/) (Implement IT-WATCHDOGS-V4-MIB and GEIST-V4-MIB)
*   [#1807](https://github.com/UNINETT/nav/issues/1807/) (Implement support for Powertek PDU inlet status)
*   [#1817](https://github.com/UNINETT/nav/issues/1817/) (Add hook to customize tabs in ipdevinfo and info/room)

#### Fixed GitHub issues in this release:

*   [#1683](https://github.com/UNINETT/nav/issues/1683/) (Avoid "magic" Django bootstrapping in nav.models)
*   [#1703](https://github.com/UNINETT/nav/issues/1703/) (Upgrade Django Rest Framework)
*   [#1709](https://github.com/UNINETT/nav/issues/1709/) (Rename verb for changing interface admin status)
*   [#1728](https://github.com/UNINETT/nav/issues/1728/) (Upgrade python-ldap)
*   [#1744](https://github.com/UNINETT/nav/issues/1744/) (Replace automake toolchain with setuptools)
*   [#1752](https://github.com/UNINETT/nav/issues/1752/) (No warnings for Django 1.8)
*   [#1786](https://github.com/UNINETT/nav/issues/1786/) (Make middlewares work correctly on Django 1.10+)
*   [#1796](https://github.com/UNINETT/nav/issues/1796/) (A crashing search provider will crash the entire search ui)
*   [#1798](https://github.com/UNINETT/nav/issues/1798/) (Environment sensor rack API crashes on missing sensors)
*   [#1799](https://github.com/UNINETT/nav/issues/1799/) (Portadmin errors out if making changes after using browser back button)
*   [#1800](https://github.com/UNINETT/nav/issues/1800/) (Alert profile listing "Remove selected" button needn't be visible when there are no profiles to select.)
*   [#1801](https://github.com/UNINETT/nav/issues/1801/) (Network Explorer MAC search always crashes)
*   [#1802](https://github.com/UNINETT/nav/issues/1802/) (Saving a threshold rule without a target crashes with a KeyError)
*   [#1803](https://github.com/UNINETT/nav/issues/1803/) (ipdevpoll should be able to perform reverse DNS lookups using /etc/hosts file)
*   [#1804](https://github.com/UNINETT/nav/issues/1804/) (Unrecognized neighbors report crashes with 'bogus escape (end of line)')
*   [#1814](https://github.com/UNINETT/nav/issues/1814/) (Change the NAV license from GPLv2 to GPLv3)
*   [#1819](https://github.com/UNINETT/nav/issues/1819/) (/prefix/usage API endpoint crashes instead of returning 404 on non-existent prefixes)

Release notes
-------------

We always advise you to have a look at [NAV's accompanying release notes](https://nav.uninett.no/doc/4.9/release-notes.html#nav-4-9) when upgrading.

Happy NAVing everyone!