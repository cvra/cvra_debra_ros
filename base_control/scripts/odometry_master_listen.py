#!/usr/bin/env python2
from cvra_rpc.message import *

def odometry_raw_cb(args):
    print("Odometry raw values")
    print(args)

TARGET = ('0.0.0.0', 20000)
callbacks = {'odometry_raw': odometry_raw_cb}

RequestHandler = create_request_handler(callbacks)
server = socketserver.UDPServer(TARGET, RequestHandler)
server.serve_forever()
