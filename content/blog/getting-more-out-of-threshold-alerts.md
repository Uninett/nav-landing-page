---
title: 'Getting more out of threshold alerts'
date: 2016-06-01T15:38:00.001+02:00
draft: true
url: 
---

Did you know you can edit your NAV alert text templates yourself? No? With a little bit of knowledge of [Django's template language](https://docs.djangoproject.com/en/1.7/topics/templates/), you can customize the contents of the alert messages NAV sends to you e-mail, mobile or other channels.  
  
In your running NAV installation's configuration directory, there is a subdirectory titled alertmsg. In this directory is a hierarchy of Django templates that define the actual message texts used for all the various types of NAV alerts.  

Fixing those useless threshold alerts
-------------------------------------

Let's attempt to modify the contents of threshold alerts that are dispatched via e-mail. Take a look in the alertmsg/thresholdState directory. This directory contains all the templates used for formatting threshold-related alerts.  
To begin with, you'll want to take a look at exceededThreshold-email.txt. It's a bit short, and slightly uninformative:  
  
```
Subject: Threshold exceeded on {{ metric }}  
  
The metric {{ metric }} was measured at {{ measured\_value }} on {{ time }},  
exceeding the configured threshold of {{ alert|safe }}.  

``````
  

```NAV's threshold monitor is quite generic, and can be used to monitor any value stored in the Graphite server NAV is configured to use - it doesn't matter whether the metric came from NAV itself or not.  
  
This is also why the alert text is a bit bland, because NAV doesn't know what any given metric path means.  
  
Except, that's not true.  
  
NAV does have the ability to look at a metric path and attempt to associate it with some object known to NAV. Sensors are an example of a NAV object that corresponds to some metric that is collected and dispatched to Graphite.  
  

Add more text here...
---------------------