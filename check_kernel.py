#!/usr/bin/env python3

# 
# Guillaume Subiron, Sysnove, 2014
#
# Description :
#
# This plugin checks if we're running the newest installed kernel.
# Works on Debian.
#
# Copyright 2013 Guillaume Subiron <guillaume@sysnove.fr>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the http://www.wtfpl.net/ file for more details.
#

import os

from distutils.version import LooseVersion

STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3

def main():
    """ This program is used to check the kernel version. """

    files = (f[8:] for f in os.listdir("/boot") if f.startswith("vmlinuz-"))
    latest = sorted(files, key=lambda x: LooseVersion(x), reverse=True)[0]
    current = LooseVersion(os.uname().release)

    if latest > current:
        print("KERNEL WARNING - Running kernel %s but newer kernel available: %s;" % (current, latest))
        return STATE_WARNING
    else:
        print("OK - Running kernel: %s;" % current)
        return STATE_OK

if __name__ == "__main__":
    main()