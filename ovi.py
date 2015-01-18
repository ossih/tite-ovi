#!/bin/python2
# -*- coding: utf-8 -*-

# 2014-05-26 pilixi (initial)
# 2014-09-30 pilixi (added function after closing time)

import sys
import time
import socket
from espeak import espeak

# Jos on lanit, ota kommentti pois seuraavasta niin tämä ei vine
#sys.exit()

jumalauta='JUMALAUTA' in sys.argv

def writeStatus(status):
    with open('/tmp/ovi.status','w') as f:
       f.write(status)

def readStatus():
    with open('/tmp/ovi.status','r') as f:
        status=f.readlines()[0]
    return status

espeak.set_voice('fi')
espeak.set_parameter(espeak.Parameter.Rate,80)
espeak.set_parameter(espeak.Parameter.Pitch,0)

socket.setdefaulttimeout(2)
def fetchStatus():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('10.0.0.50',5000))
    status=sock.recv(1)
    sock.close()
    return status

status=fetchStatus()

if status=='0' and readStatus()=='1':
    espeak.synth('kiitoos')

do_break=False

if status=='1' and not jumalauta:
    espeak.synth('oovii kiinnii')
    for i in range(55):
        status=fetchStatus()
        if status=='0':
            espeak.synth('kiitoos')
            break
        time.sleep(1)

if jumalauta:
    for i in range(11):
        status=fetchStatus()
        if status=='1':
            espeak.synth('oovii kiinnii')
            time.sleep(5)
            for j in range(50-5*i):
                status=fetchStatus()
                if status=='0':
                    espeak.synth('kiitoos')
                    do_break=True
                    break
                time.sleep(1)
        if do_break:
            break
        time.sleep(5)

writeStatus(status)
time.sleep(5)

