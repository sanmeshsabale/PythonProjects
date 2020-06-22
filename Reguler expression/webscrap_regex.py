import re,urllib
import urllib.request
sites="google rediff".split()
print(sites)
for s in sites:
    print("Searching...",s)
u=urllib.request.urlopen("https://www.rediff.com/")
text=u.read()
title=re.findall("<title>.*</title>",str(text),re.I)
print(title[0])
