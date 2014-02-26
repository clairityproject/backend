from data.models import Node, IP, Location, DataPoint
import json
import urllib2
from itertools import count
import random
import datetime

DATAPOINTS_PER_NODE = 100

# random date generator
def random_date():
    start = datetime.datetime(2014,1,1,1,1,1)
    stop = datetime.datetime.now()
    return start + datetime.timedelta(seconds=random.randint(0,int((stop-start).total_seconds())))



# counter to be used for node numbers
c = count()

# create nodes
for query in ["center","house"]:
    data = json.loads("".join(urllib2.urlopen("http://whereis.mit.edu/search?type=query&q="+query+"&output=json").readlines()))

    for d in data:
        # create locations
        loc= Location(name=d['name'], latitude=d['lat_wgs84'], longitude=d['long_wgs84'])
        loc.save()
        # create node
        node_num = c.next()
        # create node's IP address
        ip = IP(node_number=node_num, address="18.10.13."+str(node_num))
        ip.save()
        # save node
        node = Node(location=loc, number=node_num, ip=ip)
        node.save()

# create random datapoints for each node

nodes = Node.objects.all()

for node in nodes:
    for x in xrange(DATAPOINTS_PER_NODE):
        DataPoint(node=node, 
                temperature=random.uniform(-3,80), 
                rh=random.uniform(12,50), 
                dylos_bin_1=random.randint(0,100),
                dylos_bin_2=random.randint(0,100),
                dylos_bin_3=random.randint(0,100),
                dylos_bin_4=random.randint(0,100),
                alphasense_1=random.uniform(100.0,1500.0),
                alphasense_2=random.uniform(100.0,1500.0),
                alphasense_3=random.uniform(100.0,1500.0),
                alphasense_4=random.uniform(100.0,1500.0),
                alphasense_5=random.uniform(100.0,1500.0),
                alphasense_6=random.uniform(100.0,1500.0),
                alphasense_7=random.uniform(100.0,1500.0),
                alphasense_8=random.uniform(100.0,1500.0)).save()
