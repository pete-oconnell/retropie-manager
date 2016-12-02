import time
import urllib2
import config


response = urllib2.urlopen(config.retroURL).read()
if int(response) == 1:
	print('there is something waiting')
else:
	print('nope....nothing')

time.sleep(config.sleepTime)

