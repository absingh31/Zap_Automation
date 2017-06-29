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


