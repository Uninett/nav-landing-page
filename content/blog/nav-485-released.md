---
title: 'NAV 4.8.5 released'
date: 2018-06-22T08:06:00.000+02:00
draft: false
url: /blog/2018/06/nav-485-released/
---

The fifth maintenance release of the 4.8 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). New packages for Debian 8/9 (Jessie/Stretch) are published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

### Changes

Fixed GitHub issues in this release:

*   [#1688](https://github.com/UNINETT/nav/issues/1688/) (Report crashes when using %, \* or non-ASCII characters in filter values)
*   [#1693](https://github.com/UNINETT/nav/issues/1693/) (Changing password from "User and API Administration" leads to KeyError)
*   [#1702](https://github.com/UNINETT/nav/issues/1702/) (Adding log entries with non-ascii characters crashes page)
*   [#1711](https://github.com/UNINETT/nav/issues/1711/) (Regression: Report crashes when attempting to sort a column filtered on a non-ASCII value)
*   [#1719](https://github.com/UNINETT/nav/issues/1719/) ('navdump -a' puts status messages into the output files)
*   [#1721](https://github.com/UNINETT/nav/issues/1721/) (Widget spinner visible when opening tool-menu)
*   [#1729](https://github.com/UNINETT/nav/issues/1729/) (Room search "CSV download" CR in "last active" field)
*   [#1734](https://github.com/UNINETT/nav/issues/1734/) (l2trace crashes when searching for invalid IP addresses)
*   [#1735](https://github.com/UNINETT/nav/issues/1735/) (HTTP errors from Graphite shouldn't crash NAV's Graphite render proxy)

### Copyright changes

Third party copyright owners of NAV code, like The Norwegian University of Science and Technology, and the University of Tromsø, have signed over their copyright for their code contributions to Uninett. NAV 4.8 is still licensed under GPLv2-only, but will be relicensed under GPLv3 in the upcoming 4.9 series. This should have no impact on end users; as a company with public ownership, Uninett will always strive to keep NAV under a free and open source license.

Happy NAVing everyone!