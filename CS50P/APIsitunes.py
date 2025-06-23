import json
import sys
import requests

if len(sys.argv)!= 2:
    sys.exit()

#use requests to get info from the online server using APIs
data = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# put that data in json format name it music
music = data.json()

#loop through the data in the "results" part in json data
for result in music["results"]:
    #print out the result in "trackname" part
    print(result["trackName"])


