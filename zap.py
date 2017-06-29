#!/usr/bin/env python
import os
import subprocess
import time
from pprint import pprint
from zapv2 import ZAPv2


print('Starting ZAP ...')
subprocess.Popen(['/usr/share/zaproxy/zap.sh','-daemon','-config api.key=12121'],stdout=open(os.devnull,'w'))
print('Waiting for ZAP to load, 10 seconds ...')
time.sleep(10)
# Here the target is defined and an instance of ZAP is created.
target = 'http://www.cyware.com/'
zap = ZAPv2()

apikey=12121
# Start access to the target
print('Accessing target %s' % target)
zap.urlopen(target)
time.sleep(2)

# start the spider crawl 
print('Spidering target %s' % target)
zap.spider.scan(target,apikey)


# Progress of spider
time.sleep(2)
print('Status %s' % zap.spider.status)
while (int(zap.spider.status) < 100):
   print('Spider progress %: ' + zap.spider.status)

   time.sleep(400)

print('Spider completed')

# Give the passive scanner a chance to finish
time.sleep(5)

# The active scanning starts
print('Scanning target %s' % target)
zap.ascan.scan(target)
while (int(zap.ascan.status) < 100):
   print('Scan progress %: ' + zap.ascan.status)

   time.sleep(600)

print('Scan completed')

# Report the results
print('Hosts: ' + ', '.join(zap.core.hosts))
print('Alerts: ')
pprint(zap.core.alerts())

