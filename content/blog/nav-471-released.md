---
title: 'NAV 4.7.1 released'
date: 2017-06-09T16:14:00.002+02:00
draft: false
url: /blog/2017/06/nav-471-released/
---

We apologize for the issues with yesterday's NAV release, which, apparently, our test suite was unable to detect.

We are hereby releasing NAV 4.7.1, which addresses the known issues of yesterday's release.

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases). A new package for Debian Jessie is published in our [APT repository](https://nav.uninett.no/install-instructions/#debian), as usual.

The virtual appliance will be updated shortly.

### Changes

As always, we recommend you read the [release notes](https://nav.uninett.no/doc/4.7/release-notes.html#nav-4-7) for a fuller description of the new features and significant changes.

These bugs have been fixed:

*   [#1524](https://github.com/UNINETT/nav/issues/1524/) (Auditlog is a top-level module, causing all of NAV 4.7.0 to break)
*   [#1528](https://github.com/UNINETT/nav/issues/1528/) (All ipdevpoll jobs, except `dns` and `snmpcheck`, stopped working after upgrade to 4.7.0)
*   [#1527](https://github.com/UNINETT/nav/issues/1527/) (ipdevpoll logs every line twice)

Happy NAVing everyone!