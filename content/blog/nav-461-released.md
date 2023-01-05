---
title: 'NAV 4.6.1 released'
date: 2017-01-26T14:06:00.000+01:00
draft: false
url: /2017/01/nav-461-released.html
---

The first maintenance release of the 4.6 series release of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

### Changes

NAV has moved to GitHub. Issues are now tracked at [GitHub](https://github.com/UNINETT/nav/issues). Due to the migration of bug data from Launchpad, reporter and subscriber information has been lost (all bugs appear to be reported by jmbredal).

If you have existing bug reports you still wish to keep an eye on, you can find the migrated issue by searching the Launchpad bug number in our GitHub issue tracker.

Fixed issues in this release:

*   [#320](https://github.com/UNINETT/nav/issues/320/) (Error in IPAM function after upgrade to 4.6)
*   [#321](https://github.com/UNINETT/nav/issues/321/) (Graph widget modifies graph interval to 24 hours, no matter what the URL says)
*   [#891](https://github.com/UNINETT/nav/issues/891/) ("rooms with active alerts"-widget needs event filter)
*   [#892](https://github.com/UNINETT/nav/issues/892/) (cancelled maintenance tasks with no endtime are displayed)
*   [#893](https://github.com/UNINETT/nav/issues/893/) (Long log lines cause logging to stop for ipdevpoll processes in multiprocess mode)
*   [#1022](https://github.com/UNINETT/nav/issues/1022/) (Some dropdowns not sorted in Alert Profiles)
*   [#1024](https://github.com/UNINETT/nav/issues/1024/) (support external links in ups widget)
*   [#1238](https://github.com/UNINETT/nav/issues/1238/) (choose columns in status widget)
*   [#1425](https://github.com/UNINETT/nav/issues/1425/) (Using arrow keys to navigate when there is only a single dashboard moves to a 'undefined' dashboard, resulting in a 404 Not Found)
*   [#1426](https://github.com/UNINETT/nav/issues/1426/) (Left/right arrow keys are captured globally on dashboards, making it impossible to make small edits to widget titles and such)
*   [#1412](https://github.com/UNINETT/nav/issues/1412/) (multiple dashboards should be presented as tabs)

Happy NAVing everyone!