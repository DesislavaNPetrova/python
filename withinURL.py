### Create virtualenv:

mkdir my-project-folder && cd$_
vritualenv --python python3 my-venv
source my-venv/bin/activate

###

# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_defaul_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="()http[s]?://.*"',html)