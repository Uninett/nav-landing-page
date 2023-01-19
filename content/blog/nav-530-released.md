---
title: 'NAV 5.3.0 released'
date: 2022-02-22T18:49:00.001+01:00
draft: false
url: /blog/2022/02/nav-530-released/
---

The initial maintenance release of the 5.3 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

On January 1st 2022, Uninett, NSD and Unit (all entities owned by the Norwegian government) were merged into the new governmental agency _Sikt - Norwegian Agency for Shared Services in Education and Research_. This marks the first release of NAV under the new organization name.

A new package for Debian 10 (Buster) is available in our [APT repository](https://nav.uninett.no/install-instructions/#debian) as usual. We are currently working on building a package for Debian 11 (Bullseye).

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files in `/etc/nav` and make sure to update your running config.

The virtual appliance will be updated shortly.

## User-visible features and improvements

The main reason for this new feature release is to ensure NAV is compatible with Python 3.9 (which is the default Python version on the current Debian stable distro, Bullseye). Features that were already lurking in the pipeline are:

*   [#2245](https://github.com/Uninett/nav/issues/2245) (Link to room details page from SeedDB room edit page)
*   [#2274](https://github.com/Uninett/nav/issues/2274) (Hidden attributes for devices)
    *   [#2323](https://github.com/Uninett/nav/pull/2323) (Completely hide all attributes starting with "\_\_")
*   [#2309](https://github.com/Uninett/nav/issues/2309) (Support a report.conf.d/ style config directory for reports)
*   [#2311](https://github.com/Uninett/nav/issues/2311) (Wishlist: Info about locations visible via /report/location)

## Other fixed GitHub issues in this release

*   [#2280](https://github.com/Uninett/nav/issues/2280) (Only ethernetCsmacd interfaces are shown in the room viewer)
*   [#2310](https://github.com/Uninett/nav/issues/2310) (\[BUG\] snmptrapd plugins crash when posting events in NAV 5.2)
*   [#2315](https://github.com/Uninett/nav/pull/2315) (Properly upgrade to Django 2.2)
*   [#2316](https://github.com/Uninett/nav/pull/2316) (Upgrade dependencies that will need a newer version to run on Django 3.2 or later)
*   [#2317](https://github.com/Uninett/nav/pull/2317) (Upgrade Django to 3.2)
*   [#2321](https://github.com/Uninett/nav/pull/2321) (Also list local conf reports in report widget)
*   [#2324](https://github.com/Uninett/nav/issues/2324) (\[BUG\] Example severity rules distributed with NAV 5.2.1 do not actually work)
*   [#2328](https://github.com/Uninett/nav/pull/2328) (Remove "no access" message from login page during normal login)
*   [#2329](https://github.com/Uninett/nav/pull/2329) (Upgrade to dnspython 2.1)
*   [#2341](https://github.com/Uninett/nav/issues/2341) (Warn when database config isn't readable)
*   [#2352](https://github.com/Uninett/nav/pull/2352) (Fix Python 3.9 compatibility)
*   [#2353](https://github.com/Uninett/nav/pull/2353) (Document the name change from Uninett to Sikt)
*   [#2355](https://github.com/Uninett/nav/pull/2355) (Add Sikt to About page, copyrights and graphical profile)

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/5.3.x/release-notes.html#nav-5-3) before upgrading.

Happy NAVing everyone!
