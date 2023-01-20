---
title: 'Why I love Whisper'
date: 2014-03-05T07:02:00.000+01:00
draft: false
url: /blog/2014/03/why-i-love-whisper/
tags: 
- regular
---

We have just built a new, modern server room at UNINETT, with robust power distribution and cooling systems, and of course, we want to monitor the server room environment using NAV.

For NAV, we are brushing up its support for collecting sensor readings from UPSes, and we are implementing support for the Comet web probes that have been deployed to take temperature readings in the new server room.

This is when I happened upon NAV’s implementation of the UPS-MIB (RFC 1628), where the precision of a couple of objects is off by a factor of 10. **No way** our UPS is putting out _50 Amperes_ of electric current! [The fix for the NAV code was quick](https://github.com/Uninett/nav/commit/fb32bda5a81f1c6bab96d7516c58c1df1bb80928), but the graph doesn’t look very nice after the change:

![Graph of temperature readings from UPSes where the precision is off. Output current graph drops suddenly at the end.](/image/blog/tumblr_inline_n1yuefrgtu1swzy6x.png "Graph of temperature readings")

This is where Whisper, the storage format used by Graphite, shines, compared to RRD, in my humble opinion. This was all fixable with some one-line command trickery:

```shell
whisper-fetch.py upsOutputCurrent.wsp \
| perl -lane \
    'print @F[0] . ":" . @F[1]/10.0 if @F[1] > 15.0' \
| xargs whisper-update.py upsOutputCurrent.wsp
```

1.  The whisper-fetch command pulls out all the data points from the underlying Whisper file.
2.  The perl command filters any data point with a value above 15.0, divides the value by 10.0 and outputs an updated data point.
3.  The xargs+whisper-update combination updates the Whisper file with all the modified datapoints output by the perl command.

The result:

![Graph of temperature readings from UPSes with better precision. There are no sudden drops in the graph.](/image/blog/tumblr_inline_n1yuvf0boh1swzy6x.png "Graph of temperature readings with better precision")

Brilliantly simple :-)
