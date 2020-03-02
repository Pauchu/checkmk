#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# small mock server simulating a jolokia server. Not very sophisticated
# but enough to get several checks to display something

from __future__ import print_function
import SocketServer
import SimpleHTTPServer
import urlparse

PORT = 8080


class FakeHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse.urlparse(self.path)
        params = [par for par in parsedParams.path.split('/') if par]

        print(params)

        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.end_headers()

        if len(params) > 1:
            self.wfile.write('{"value": 1}')
        else:
            self.wfile.write('{"value": {"info":'\
                 '{"version": "1.0", "product": "Fake_Product"}, "agent": "Fake_Agent"}}')

        self.wfile.close()


class FakeTCPServer(SocketServer.TCPServer):
    allow_reuse_address = True


httpd = FakeTCPServer(("", 8080), FakeHandler)
httpd.serve_forever()
