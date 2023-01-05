---
title: 'NAV 4.6.2 released'
date: 2017-03-16T12:07:00.000+01:00
draft: false
url: /2017/03/nav-462-released.html
---

The second maintenance release of the 4.6 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual. Issues can be viewed and reported in the [NAV issue list](https://github.com/UNINETT/nav/issues).

The virtual appliance will be updated shortly.

### Changes

Fixed issues in this release:

*   [#1326](https://github.com/UNINETT/nav/issues/1326/) (ipdevpoll -n option may be unable to match single IP addresses in environments without DNS names)
*   [#1344](https://github.com/UNINETT/nav/issues/1344/) (Location is mandatory field when adding a room, but not when bulk importing)
*   [#1433](https://github.com/UNINETT/nav/issues/1433/) (Users with non-set passwords may crash the login page)
*   [#1437](https://github.com/UNINETT/nav/issues/1437/) (Eventengine's modulestate plugin will not handle alerts on modules that have duplicates)
*   [#1454](https://github.com/UNINETT/nav/issues/1454/) (Alert message HTML templates break on events that have no associated alert type)
*   [#1455](https://github.com/UNINETT/nav/issues/1455/) (Alert profiles with vendor-based filters seems to crash the Alertengine completely)
*   [#1460](https://github.com/UNINETT/nav/issues/1460/) ("arp" API endpoint produces server error when mixing ip and ordering=netbox)
*   [#1464](https://github.com/UNINETT/nav/issues/1464/) (Selecting page size in reports eliminates search parameters)
*   [#1471](https://github.com/UNINETT/nav/issues/1471/) (Fallback to default set of sensor-collecting MIBs does not work)
*   [#1471](https://github.com/UNINETT/nav/issues/1471/) (revision library stuff should be renamed to cache)
*   [#1476](https://github.com/UNINETT/nav/issues/1476/) (OverflowError when searching for IPv6 prefix in the navbar)
*   [#1477](https://github.com/UNINETT/nav/issues/1477/) (The Prefix details page should only list GW and GSW devices under the router ports list)
*   [#1478](https://github.com/UNINETT/nav/issues/1478/) (l2trace hardcodes internal URLs)
*   [#1479](https://github.com/UNINETT/nav/issues/1479/) (Change prefix links to new prefix details page)
*   [#1480](https://github.com/UNINETT/nav/issues/1480/) (ipdevpoll sensors plugin should verify enterprise IDs using live queries, not db lookups)
*   [#1481](https://github.com/UNINETT/nav/issues/1481/) (Organization column is empty in room deviceinfo page)
*   [#1484](https://github.com/UNINETT/nav/issues/1484/) (cant save status filter when filter has special characters)
*   [#1485](https://github.com/UNINETT/nav/issues/1485/) (AlertProfiles crashes with a UnicodeEncodeError when attempting to save a profile with non-ASCII characters in its name)

Happy NAVing everyone!