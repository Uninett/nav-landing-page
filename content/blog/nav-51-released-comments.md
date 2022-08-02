---
title: 'NAV 5.1 released'
date: 2020-11-26T15:48:00.000+01:00
draft: false
url: /2020/11/nav-51-released.html
---

#### after the update from 5.0.8 servicemon and event...
[MirkoB](https://www.blogger.com/profile/03698053043217481801 "noreply@blogger.com") - <time datetime="2020-11-30T11:20:02.441+01:00">Nov 1, 2020</time>

after the update from 5.0.8 servicemon and eventengine failed to start.  
  
the logfiles they were trying to open were created (and owned) by root, so unavailable in the new version that doesn't run as root.  
  
I changed the owner of those files and the problem was solved.
<hr />
#### Indeed, MirkoB, this probably stems from issue #20...
[Uninett NAV](https://www.blogger.com/profile/07140215260093050858 "noreply@blogger.com") - <time datetime="2020-11-30T11:28:56.911+01:00">Nov 1, 2020</time>

Indeed, MirkoB, this probably stems from issue #2078 - NAV 5.0 and previous versions would unnecessarily and inadvertently run most NAV daemons as the root user, even though only pping and snmptrapd would require root level privileges at startup time.
<hr />
