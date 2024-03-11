---
title: 'NAV 5.9.0 released'
date: 2024-03-11T11:46:00.000+01:00
draft: false
tags:
- release
---

The first feature release of the 5.9 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for Debian 10 (Buster) and 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Added

- Added option to enable secure cookies in new web security section of `webfront.conf` ([#2194](https://github.com/Uninett/nav/issue/2194), [#2815](https://github.com/Uninett/nav/pull/2815))
- Made `mod_auth_mellon` (SAML) work for logins ([#2740](https://github.com/Uninett/nav/pull/2740))
  - Also added howto for setting up `mod_auth_mellon` for Feide authentication.

## Fixed

- Cycle session IDs on login/logout to protect against potential session fixation attacks ([#2804](https://github.com/Uninett/nav/issues/2804), [#2813](https://github.com/Uninett/nav/pull/2813), [#2836](https://github.com/Uninett/nav/pull/2836), [#2835](https://github.com/Uninett/nav/pull/2835))
- Flush sessions on logout ([#2828](https://github.com/Uninett/nav/pull/2828))
- Prevent clickjacking attacks on NAV by disallowing putting NAV site in document frames ([#2816](https://github.com/Uninett/nav/pull/2816), [#2817](https://github.com/Uninett/nav/pull/2817))
- Cleaned up overview/intro docs ([#2827](https://github.com/Uninett/nav/pull/2827))
- Various cleanups of the test suites:
  - Remove `FakeSession` redundancy ([#2841](https://github.com/Uninett/nav/issues/2841), [#2842](https://github.com/Uninett/nav/pull/2842))
  - Fixed activeipcollector `get_timestamp` function implementation and its broken timezone-naive test ([#2831](https://github.com/Uninett/nav/pull/2831))
  - Fixed broken statemon tests ([#2832](https://github.com/Uninett/nav/pull/2832))
  - Fixed warnings during integration tests ([#2847](https://github.com/Uninett/nav/issues/2847), [#2858](https://github.com/Uninett/nav/pull/2858))
  - Preserve 500-errors in webcrawler tests ([#2861](https://github.com/Uninett/nav/pull/2861))
- Removed nonsensical pydantic requirement ([#2867](https://github.com/Uninett/nav/pull/2867))
- Removed warnings when building docs ([#2856](https://github.com/Uninett/nav/pull/2856))

## Changed

- Modernize installation of NAV scripts/binaries using `pyproject.toml` ([#2676](https://github.com/Uninett/nav/issues/2676), [#2679](https://github.com/Uninett/nav/pull/2679))
- Changed the documentation theme from "Bootstrap" to "Read The Docs", as the Bootstrap theme was no longer being maintained.  This also avoids unnecessary JavaScript libraries in the docs ([#2805](https://github.com/Uninett/nav/issues/2805), [#2825](https://github.com/Uninett/nav/pull/2825), [#2824](https://github.com/Uninett/nav/pull/2824), [#2834](https://github.com/Uninett/nav/issues/2834), [#2837](https://github.com/Uninett/nav/pull/2837), [#2833](https://github.com/Uninett/nav/issues/2833), [#2853](https://github.com/Uninett/nav/pull/2853), [#2868](https://github.com/Uninett/nav/pull/2868))
- Various changes needed to move NAV closer to being fully compatible with Python 3.11:
  - Replaced all uses of `pkg_resources` with `importlib` ([#2791](https://github.com/Uninett/nav/issues/2791), [#2798](https://github.com/Uninett/nav/pull/2798), [#2799](https://github.com/Uninett/nav/pull/2799))
  - Upgraded Twisted to a version that supports Python 3.11 ([#2792](https://github.com/Uninett/nav/issues/2792), [#2796](https://github.com/Uninett/nav/pull/2796))
  - Upgraded psycopg to 2.9.9 ([#2793](https://github.com/Uninett/nav/issues/2793), [#2795](https://github.com/Uninett/nav/pull/2795))
  - Dropped code that was there to support Django's older than 3.2 ([#2823](https://github.com/Uninett/nav/pull/2823))
  - Upgraded `python-ldap` from 3.4.0->3.4.4 ([#2830](https://github.com/Uninett/nav/pull/2830))
  - Enabled running test suite on Python 3.10 by default ([#2838](https://github.com/Uninett/nav/pull/2838))
  - Stopped running test suite on Python 3.8 by default ([#2851](https://github.com/Uninett/nav/pull/2851))
  - Fixed invalid/deprecated backslash escapes in MIB dump files, as warned about in newer Python versions ([#2846](https://github.com/Uninett/nav/pull/2846), [#2848](https://github.com/Uninett/nav/pull/2848))
  - Fixed deprecation warning for Django 4.0 in test suite ([#2844](https://github.com/Uninett/nav/pull/2844))
  - Removed an adaption to Pythons older than 3.7 ([#2840](https://github.com/Uninett/nav/pull/2840))
  - Install Node/NPM in docker dev environment ([#2855](https://github.com/Uninett/nav/pull/2855))
  - Vendor the PickleSerializer ([#2866](https://github.com/Uninett/nav/pull/2866))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-9) before upgrading.

Happy NAVing everyone!

