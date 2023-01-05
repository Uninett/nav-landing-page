---
title: 'NAV 4.8.2 released'
date: 2017-12-07T10:17:00.000+01:00
draft: true
url: /2017/12/nav-482-released.html
---

#### Hi folks, thanks for your great work! We're n...
[Unknown](https://www.blogger.com/profile/09313008807267880819 "noreply@blogger.com") - <time datetime="2017-12-08T09:43:25.050+01:00">Dec 5, 2017</time>

Hi folks,  
  
thanks for your great work! We're new NAV-Users an we'd like to upgrade from 4.7.3 to 4.8.2. Is there an official upgrade-path or do we have to do an migration?  
  
Thanks in advance!  
  
Best regards,  
Matthias
<hr />
#### Hi Matthias, If you installed via the Debian pac...
[Morten Brekkevold](https://www.blogger.com/profile/14248445833838632651 "noreply@blogger.com") - <time datetime="2017-12-08T10:29:32.042+01:00">Dec 5, 2017</time>

Hi Matthias,  
  
If you installed via the Debian package, then you just upgrade the package via normal apt-get commands.  
  
If you installed from source, you mostly follow the same instructions for installation - just remember to use \`navsyncdb\` to upgrade your database schema.
<hr />
#### Hi Morten, thank you very much - yes, we used the...
[Unknown](https://www.blogger.com/profile/09313008807267880819 "noreply@blogger.com") - <time datetime="2017-12-08T12:39:58.559+01:00">Dec 5, 2017</time>

Hi Morten,  
  
thank you very much - yes, we used the Debian packages, made an apt-get update and apt-ge upgrade and now 4.8.2 runs like a charm!  
  
Thank you!  
  
Best regards,  
Matthias
<hr />
