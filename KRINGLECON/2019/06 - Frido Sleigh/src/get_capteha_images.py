# get_capteha_images.py

import requests
import base64

uuids = []
base64s = []

for i in range(1):
	req1 = 'https://fridosleigh.com/api/capteha/request'
	res1 = requests.post(req1)
	print(res1.headers['Set-Cookie'].split(';')[0])
	res1 = eval(res1.content.decode('utf-8').replace('true', "True"))
	uuids += [i['uuid'] for i in res1['images']]
	base64s += [i['base64'].encode('utf-8') for i in res1['images']]

counter = 0
for b64 in base64s:
	counter += 1
	with open("unknown_images/%s.png" % counter, "wb") as image:
		image.write(base64.b64decode(b64))