import json
import urllib2
from datetime import datetime

url = 'http://ec2-54-187-18-145.us-west-2.compute.amazonaws.com/node/postdata/'
#url = 'http://localhost:8000/node/postdata/'

values = {'node_id' : 3,
        'temperature' : 20.3,
        'rh' : 20.3,
        'dylos_bin_1' : 20.3,
        'dylos_bin_2' : 20.3,
        'dylos_bin_3' : 20.3,
        'dylos_bin_4' : 20.3,
        'alphasense_1' : 20.3,
        'alphasense_2' : 20.3,
        'alphasense_3' : 20.3,
        'alphasense_4' : 20.3,
        'alphasense_5' : 20.3,
        'alphasense_6' : 20.3,
        'alphasense_7' : 20.3,
        'alphasense_8' : 20.3,
        'reading_time' : datetime.now().isoformat()
        }

##################################################
# Method 2 
# looks cleaner but needs installation of requests
# library
##################################################

import requests
import time

r = requests.post(url, data=values)
print json.dumps(r.json(), indent=4)

