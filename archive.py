import webbrowser
import json
from urllib.request import urlopen

print("Let's take a trip down memory lane.")

site = input("Type a website URL: ")
date = input("Type a year, month and day, like 20160513: ")

print("Good choice, let's see...")

url = "https://archive.org/wayback/available?url=%s&timestamp=%s" % (site, date)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
  old_site = data["archived_snapshots"]["closest"]["url"]
  print("We found one, hold tight!")
  webbrowser.open(old_site)
except:
  print("We couldn't find that one, but let's try again?")