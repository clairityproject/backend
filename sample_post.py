#!/usr/bin/env python

import json
import urllib2
import requests
import time
from datetime import datetime

#url = 'http://ec2-54-187-18-145.us-west-2.compute.amazonaws.com/node/postdata/'
url = 'http://localhost:8000/node/postdata/'
#url = 'http://clairity.mit.edu/node/postdata/'

def send(url, values):
    try:
        print "url : " +url
        r = requests.post(url, data=values)
        try:
            print json.dumps(r.json(), indent=4)
        except:
            print "FAILED \n\n\n\n"
            pass
            #print rk
            #print dir(r)
    except:
        print "sending failed"

def test():
    # dylos
    values = {'node_id' : 3,
            'dylos_bin_1' : 20,
            'dylos_bin_2' : 20,
            'dylos_bin_3' : 20,
            'dylos_bin_4' : 20,
            'reading_time' : datetime.now().isoformat()
            }
    send(url+'dylos/', values)

    values = {'node_id' : 3,
            'dylos_bin_1' : -9999,
            'dylos_bin_2' : -9999,
            'dylos_bin_3' : -9999,
            'dylos_bin_4' : -9999,
            'reading_time' : datetime.now().isoformat()
            }
    send(url+'dylos/', values)

    values = {'node_id' : 3,
            'temperature' : 20.3,
            'rh' : 20.3,
            'reading_time' : datetime.now().isoformat()
            }

    send(url+'met/', values)

    values = {'node_id' : 3,
            'temperature' : -9999,
            'rh' : -9999,
            'reading_time' : datetime.now().isoformat()
            }

    send(url+'met/', values)

    values = {'node_id' : 3,
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
    send(url+'alphasense/', values)

    values = {'node_id' : 3,
            'alphasense_1' : -9999,
            'alphasense_2' : -9999,
            'alphasense_3' : -9999,
            'alphasense_4' : -9999,
            'alphasense_5' : -9999,
            'alphasense_6' : -9999,
            'alphasense_7' : -9999,
            'alphasense_8' : -9999,
            'reading_time' : datetime.now().isoformat()
            }

    send(url+'alphasense/', values)


if __name__ == '__main__':
    test()
