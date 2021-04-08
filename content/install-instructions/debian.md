---
title: Installation instructions for Debian
---

### Preparation

To ensure your can always get the latest NAV package directly from our package repository, you should:

  - Ensure HTTPS support for APT is installed on your system
  - Trust the GPG key we use to sign the package archive
  - Add our archive to your list of APT sources

Here's how to do it:

#### Debian 10 (Buster)

    sudo apt-get install -y curl apt-transport-https ca-certificates dirmngr software-properties-common
    curl -fsSL https://nav.uninett.no/debian/gpg | sudo apt-key add -
    sudo add-apt-repository "deb https://nav.uninett.no/debian buster nav"
    sudo apt-get update
    sudo apt-get install nav

### Further instructions

Please read the instructions in [/usr/share/doc/nav/README.Debian](https://raw.githubusercontent.com/Uninett/nav-debian/master/debian/README.Debian) to complete your configuration of NAV on Debian. You may then proceed to our [getting started-guide](https://nav.uninett.no/doc/latest/intro/getting-started.html).

If you need additional help in setting up and configuring Graphite on your NAV server, please refer to the how-to guide ["Installing Graphite for use with NAV on Debian"](https://nav.uninett.no/doc/dev/howto/installing-graphite-on-debian.html).

### Bugs

If you have problems with the *package itself*, please report them at <https://github.com/uninett/nav-debian/issues>. If you want to report bugs in NAV, you can do so at <https://github.com/uninett/nav/issues>.

### Footnotes

The NAV Debian package used to be maintained by Morten Werner Forsbring at <http://pkg-nav.alioth.debian.org/> - the package currently maintained by Uninett is based on his work.

