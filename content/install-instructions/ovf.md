---
title: Installation instructions for Virtual Appliance
---

We've built virtual appliances in OVF format for those who want to get quickly started with NAV.
Most popular virtualization environments can import this appliance (Though you may need to use VMWare's OVFTool to import it properly into VMWare).

The appliances are usually built on 64-bit stable versions of Debian GNU/Linux, with NAV installed from the packages available at our APT repository (see the Debian section above). This also means that NAV is easily upgradeable using Debian's *aptitude* or *apt-get* tools.

### Downloading the appliance files

[NAV virtual appliance downloads](https://nav.uninett.no/static/appliance)

Stable releases are found in the *stable/* directory, beta testing releases in the *beta*/ directory (duh!).

### Configuration steps after booting the appliance

  * Log in as **root** and change the root password from ```navrocks``` to something else (using the *passwd* command)
  * Edit ```/etc/aliases``` to add a decent email address to forward *root*'s email to. Then run the *newaliases* command.
  * Fix the network configuration (```/etc/network/interfaces```) and restart the networking service using ```/etc/init.d/networking restart```
  * Add networks that shall be allowed to talk to the appliance in ```/etc/hosts.allow``` (both clients to the NAV web interface and network equipment that send SNMP traps)
  * Set a proper hostname/domain name in the following files: ```/etc/hosts```, ```/etc/resolv.conf```, ```/etc/mailname``` and ```/etc/exim4/update-exim4.conf.conf```

### Links

  * OVF - [http://en.wikipedia.org/wiki/Open_Virtual_Machine_Format](http://en.wikipedia.org/wiki/Open_Virtual_Machine_Format)
  * VMWare OVFTool - [http://www.vmware.com/support/developer/ovf/](http://www.vmware.com/support/developer/ovf/)
  * Debian GNU/Linux - [http://www.debian.org/](http://www.debian.org/)
  * [The appliance is built using Packer](https://github.com/UNINETT/navappliance), controlled by shell-based build scripts.
