---
title: 'NAV 5.19.2 security release'
date: 2026-10-19T10:16:49+02:00
draft: false
tags:
- release
---

The second maintenance release of the 5.19 series of NAV is now out, with
security fixes for three vulnerabilities in the report system.  We advise you
upgrade *as soon as possible*.

The source code is available for download at [GitHub](https://github.com/Uninett/nav/releases).

New packages for Debian 12 (Bookworm) and 13 (Trixie) are available in our [APT repository](https://nav.uninett.no/install-instructions/#debian).

## Security

- Fixed a SQL injection vulnerability in the report subsystem, where filter and sort fields from a report URL reached the SQL query unescaped. These fields are now quoted as column names; see the release notes for the behaviour change this implies. ([GHSA-vq8x-6j3p-qqj2](https://github.com/Uninett/nav/security/advisories/GHSA-vq8x-6j3p-qqj2))
- Fixed a denial-of-service vulnerability in the report subsystem, where a report name in the URL was compiled as a regular expression; a crafted name could raise an error or consume excessive CPU. The name is now matched literally. ([GHSA-c365-jj25-8rh9](https://github.com/Uninett/nav/security/advisories/GHSA-c365-jj25-8rh9))
- Fixed cross-site scripting vulnerabilities in the report subsystem. Report cell data, including request-supplied extra column names, reached the browser unescaped, and request-supplied `uri_`/`url_` parameters could inject `javascript:` links. Cell data is now HTML-escaped, and report links and extra columns are taken only from report configuration. See the release notes for the behaviour change this implies. ([GHSA-8gqp-wvmf-4hjj](https://github.com/Uninett/nav/security/advisories/GHSA-8gqp-wvmf-4hjj))

## Fixed

- Made SeedDB show a more readable error message when checking connectivity of management profiles that have no connectivity check ([#3275](https://github.com/Uninett/nav/issues/3275))
- Sensor graphs in the room sensors tab and in the sensor dashboard widget now show their axes and range slider correctly when the page loads. ([#3409](https://github.com/Uninett/nav/issues/3409))
- Fixed the audit log recording a copied IP device as an edit of the original, instead of as a newly created device" ([#4017](https://github.com/Uninett/nav/issues/4017))
- Fixed dashboards being allowed to have empty or whitespace-only names. Existing dashboards with blank names are renamed to "New dashboard" on upgrade. ([#4061](https://github.com/Uninett/nav/issues/4061))
- Fixed widgets rendering blank when they fail to load ([#4164](https://github.com/Uninett/nav/issues/4164))
- Fixed status widget showing blank when the default admin user was locked/deactivated ([#4165](https://github.com/Uninett/nav/issues/4165))
- Fixed showing insecure password banner on accounts from REMOTE USER when password is empty ([#4172](https://github.com/Uninett/nav/issues/4172))
- Dashboard widgets using ajax to refresh no longer refresh twice as often after being edited and saved. ([#4199](https://github.com/Uninett/nav/issues/4199))

## Release notes

We always advise you to have a look at [NAV's accompanying release notes](https://nav.readthedocs.io/en/latest/release-notes.html#nav-5-19) before upgrading.

Happy NAVing everyone!
