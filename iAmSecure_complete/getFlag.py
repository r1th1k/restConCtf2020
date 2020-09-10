#!/usr/bin/env python3 

import requests
import base64

with open("getFlag", "r") as file:
	content = file.readlines()
	for lines in content:
		print(base64.b64decode(lines))
		resp = requests.get("https://ecstatic-wing-249de5.netlify.app"+lines)
		print(resp.status_code)