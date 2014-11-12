#!/bin/sh
KEY=$(gpg -a --gen-random 1 51)
sed -i "s,^SECRET_KEY.*,SECRET_KEY = '${KEY}'," nav_landing_page/settings.py
