#!/usr/bin/python
#
# Author : Jon Zobrist <jon@jonzobrist.com>
# Homepage : http://www.jonzobrist.com
# License : BSD http://en.wikipedia.org/wiki/BSD_license
# Copyright (c) 2012, Jon Zobrist
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Purpose : This script connects to a given server port a BUNCH of times
# Usage : tcpcheck.py HOST PORT CONNECTIONS

import sys
from socket import *
from util import print_debug, tcp_check_bulk
result = -1
if (len(sys.argv) > 1):
    serverHost = sys.argv[1]        # use port from ARGV 1
    serverPort = int(sys.argv[2])        # use port from ARGV 2
    connectTimes = int(sys.argv[3])        # use port from ARGV 3
    result = tcp_check_bulk(serverHost, serverPort, connectTimes)
else:
    print "Usage : tcpcheck.py HOST PORT CONNECTIONS"

sys.exit(result)
