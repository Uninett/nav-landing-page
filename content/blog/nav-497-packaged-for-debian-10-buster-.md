---
title: 'NAV 4.9.7 packaged for Debian 10 (Buster)'
date: 2019-07-31T11:21:00.001+02:00
draft: false
url: /2019/07/nav-497-packaged-for-debian-10-buster.html
---

Hi everyone,  
  
this is a two-fold announcement:  
  
1\. We have, as of today, published a _NAV 4.9.7_ package for _Debian 10_ (Buster) in our regular APT repository. [Please see the updated instructions for use of the APT repository.](https://nav.uninett.no/install-instructions/#debian)  
  
2\. As previously mentioned, we are now discontinuing support for the Debian 8 (Jessie) line of NAV packages. There will be no new updates for this outdated platform from our side.  
  
  
There is, however, one _caveat_ to using the NAV package on Debian 10: If you want to serve both the NAV web UI and Graphite-web from the same server, you cannot achieve this on Debian 10 using the regular Apache + mod\_wsgi method for both applications.  
  
Debian 10 ships with a graphite-web package that runs on Python 3, while NAV 4.9 does not support Python 3 (we expect the next feature release to run on Python 3). mod\_wsgi cannot be made to serve both Python versions on the same Apache server - you will have to select a Python-version specific mod\_wsgi package.  
  
~~For this reason, the virtual appliance has not yet been updated to Debian 10.~~  
  
For our production deployments, we serve up NAV and Graphite-web using a uWSGI application server, and use Apache + **mod\_uwsgi** as a front to provide TLS and serving of static file resources. This works fine on Debian 10, as each uWSGI application instance is an independent process.  
  
UPDATE: The [NAV virtual appliance](https://github.com/Uninett/navappliance) has now been updated to run on Debian 10, using uWSGI to run Graphite-web under Python 3, separately from NAV (which still runs in mod\_wsgi, at the moment). [The documentation has been updated](https://nav.uninett.no/doc/4.9/howto/installing-graphite-on-debian.html#on-debian-10-buster).