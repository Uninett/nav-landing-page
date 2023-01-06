---
title: 'NAV 4.7.2 released'
date: 2017-09-29T08:20:00.000+02:00
draft: false
url: /blog/2017/09/nav-472-released/
---

The second maintenance release of the 4.7 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

Packages for Debian Stretch are now also published, so the [install instructions](https://nav.uninett.no/install-instructions/#debian) have been updated.

The virtual appliance will be updated shortly.

### Changes

Fixed [issues](https://github.com/UNINETT/nav/issues) in this release:

*   [#1516](https://github.com/UNINETT/nav/issues/1516/) (Default maintenance duration too long)
*   [#1532](https://github.com/UNINETT/nav/issues/1532/) (SeedDB bulk import of organizations and rooms crashes on misformatted attribute lists)
*   [#1535](https://github.com/UNINETT/nav/issues/1535/) (Alert profiles - filtering on location does not include sublocations)
*   [#1546](https://github.com/UNINETT/nav/issues/1546/) (IndexError in portadmin search if ipdevpoll hasn't run yet)
*   [#1553](https://github.com/UNINETT/nav/issues/1553/) (Status widgets crash if filtering on locations with non-ascii characters in the ID)
*   [#1560](https://github.com/UNINETT/nav/issues/1560/) (portadmin may change vlan for incorrect port on non-cisco devices)
*   [#1565](https://github.com/UNINETT/nav/issues/1565/) (geomap does not render rooms)
*   [#1567](https://github.com/UNINETT/nav/issues/1567/) (Moved searchproviderlist to settings)
*   [#1568](https://github.com/UNINETT/nav/issues/1568/) (Fixed deleting non-required schemas in search\_path)
*   [#1571](https://github.com/UNINETT/nav/issues/1571/) (devicehistory - device group history does not work)
*   [#1583](https://github.com/UNINETT/nav/issues/1583/) (Netmap cache crashes on non-ascii strings)

Happy NAVing everyone!