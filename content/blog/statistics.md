---
title: 'Statistics'
date: 2014-02-26T03:53:00.000+01:00
draft: false
url: /blog/2014/02/statistics/
tags: 
- regular
---

One of the goals we had when we moved from Cricket to Graphite for statistics was to integrate the graphs more with NAV, instead of having to navigate to another webpage to get the information you wanted.

## Graphs are important

For most NAV users, graphs are a very important source of information, and it is important that they are available where needed and configurable to convey the correct information.

The main source of graphs for an ip device is now the IP Device Info tool. For an IP device there are two types of graphs available - System metrics and Port metrics.

## System metrics

System metrics display graphs regarding cpu, memory and other system related metrics.

![Screenshot of tabs in NAV's system metrics. Ping tab is opened, and is showing a ping packet loss graph](/image/blog/tumblr_inline_n1lmbzvdrw1sww2qo.png "System metrics")

## Port metrics

Port metrics display graphs regarding the interfaces of the IP device.

![Screenshot of port metrics. Displays the graph called 'Port details'. It shows in- and out-going traffic on some port, measured in bits per second.](/image/blog/tumblr_inline_n1llspazav1sww2qo.png "Port metrics")

## Detailed interface view

The detailed interface view display all related graphs for that interface in addition to detailed information regarding the interface.

![Screenshot of detailed interface view. Displays 4 activity graphs.](/image/blog/tumblr_inline_n1llt023l51sww2qo.png "Detailed interface view")

## Graph controls

Each graph has individual controls for choosing timeframe. In addition there are global controls available for selecting timeframes for all graphs on a page.

## Graphs on the dashboard

If the graph you are looking at is of special importance you can easily put it on your dashboard by clicking the “Add to dashboard” button. When the graph is on the dashboard you can set a custom title and refresh interval for it.

![Screenshot of a graph that was added to the user's dashboard. It shows a ping packet round trip time graph.](/image/blog/tumblr_inline_n1lmkclf2a1sww2qo.png "Graphs on the dashboard")

## Custom graphs

If you want to dive deeper and get even more out of the integration, you have the ability to create your own graphs using the Graphite interface. These graphs may then be placed on your dashboard and will refresh themselves automatically.

![Screenshot of a custom made graph. The graph is called 'The 3 ip devices with highest max cpu'.](/image/blog/tumblr_inline_n1lmc9sgjx1sww2qo.png "Custom graphs")

## Test it yourself!

If you want to see and try all this out for yourself, we recommend installing the [NAV appliance](https://nav.uninett.no/navappliance).
