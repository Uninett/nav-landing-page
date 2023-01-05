---
title: 'Removal of Jabber (XMPP) support from NAV'
date: 2019-06-19T11:41:00.000+02:00
draft: false
url: /2019/06/removal-of-jabber-xmpp-support-from-nav.html
---

  
For the past 10 years or so, NAV has supported Jabber (via the XMPP protocol) as one of its possible notification dispatch methods. XMPP support is implemented through the `xmpppy` library, which seems to be unmaintained, and is not compatible with Python 3. As we no longer have customers who rely on NAV notifications via XMPP, we will no longer put resources into supporting it, and will be removing it as part of NAV's transition to Python 3.  
  
If you are someone who actually depends on XMPP notifications from your NAV, I would urge you to consider contributing a replacement implementation.  
  
The only Python-based XMPP implementation currently listed on [https://xmpp.org/](https://xmpp.org/) seems to be this one: [https://lab.louiz.org/poezio/slixmpp](https://lab.louiz.org/poezio/slixmpp) .  
  
  
The still-open pull request that removes the current implementation can be seen here: [https://github.com/Uninett/nav/pull/1889](https://github.com/Uninett/nav/pull/1889) .