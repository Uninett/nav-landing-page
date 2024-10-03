---
title: 'NAV 5.11.0 released'
date: 2024-10-03T15:19:00.000+02:00
draft: false
tags:
- release
---

The first feature release of the 5.11 series of NAV is now out!

The source code is available for download at [GitHub](https://github.com/UNINETT/nav/releases).

New packages for 11 (Bullseye) are available in our [APT
repository](https://nav.uninett.no/install-instructions/#debian) as usual.  We
haven't started building packages for Debian 12 (Bookworm) yet, as NAV does not
yet support running under Python 3.11.

Please be extra aware of config file changes. Look out for `*.dpkg-dist` files
in `/etc/nav` and make sure to update your running config.

## Removed

- Dropped support for Python 3.7 ([#2790](https://github.com/Uninett/nav/issues/2790))

## Added

- Post lifecycle event when power supplies or fans are removed ([#2982](https://github.com/Uninett/nav/issues/2982))
- Post lifecycle event when a module or chassis is deleted via the status or device history tools ([#2983](https://github.com/Uninett/nav/issues/2983))
- Database model for representing Organizationally Unique Identifiers (OUI) to identify vendors for MAC addresses
- Script for populating database with OUIs and corresponding vendors from IEEE ([#2945](https://github.com/Uninett/nav/issues/2945))
- Module for generating JWTs ([#2948](https://github.com/Uninett/nav/issues/2948))
- Documentation for configuring and using JWT tokens in NAV API ([#2618](https://github.com/Uninett/nav/issues/2618))

## Changed

- Upgraded dependencies after dropping support for Python 3.7 ([#2790](https://github.com/Uninett/nav/issues/2790))
- Changed Sphinx version to 7.4.7 ([#2826](https://github.com/Uninett/nav/issues/2826))
- Changed required PostgreSQL version to 13 ([#2892](https://github.com/Uninett/nav/issues/2892))
- Moved the test suite's web crawler complexity away from the test discovery phase to the test phase itself.  This reduces the number of generated test cases from `N` to 2 (where `N` is the number of reachable NAV pages) ([#2966](https://github.com/Uninett/nav/issues/2966))
- Link to the doc for using docker for development from the README and mention what ports are used when using docker for development ([#2978](https://github.com/Uninett/nav/issues/2978))
- Many user-facing forms of the web user interface have been refactored in order to remove a dependency that keeps NAV incompatible with Python 3.11.  This should not affect looks or functionality.  This work is still ongoing in the master branch and we hope it will be complete by NAV version 5.12.

## Fixed

- Correctly delete an IP Device's existing `function` value when empty field value is submitted in the IP Device IP Device edit form ([#2269](https://github.com/Uninett/nav/issues/2269))
- Fixed crash bug when reordering filters within a filter group in Alert Profiles ([#2979](https://github.com/Uninett/nav/issues/2979))
- Fixed IPAM API crash bug that caused unnecessary error reports sent as e-mail to site admins ([#2989](https://github.com/Uninett/nav/issues/2989))
- Fixed bad tooltip grammar in ipdevinfo "degraded aggregate link" badge
- Make the test suite easier to run under MacOS
- Skip tests when 3rd party requirements are missing, instead of outright failing

## Security

- Ensure that CSRF token info is preserved when refactoring crispy forms to non-crispy equivalents. This means that `flat_form.html` and `_form_content.html` templates will include CSRF token info if form method is set to `POST`. ([#3056](https://github.com/Uninett/nav/issues/3056))
 
## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-11) before upgrading.

Happy NAVing everyone!

