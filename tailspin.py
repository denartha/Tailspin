#!/usr/bin/env python

import re
import requests
import sys

url = sys.argv[1]
attempts = int(sys.argv[2])
count = 0


print "URL is " + url

m = re.search(r'(?P<url1>\w+\W+\w+\W+\w+\W+\w+\W+\w+\=)(?P<num>\d+)', url)

base_url = m.group(1)
iter = int(m.group(2))

while (count <= attempts):
	print "Count is " + str(count)
	new_url = "http://" + base_url + str(iter)
	print "New URL is " + new_url
	r = requests.get(new_url)
	print r
	iter = iter + 1
	count = count + 1

print "Done!"
