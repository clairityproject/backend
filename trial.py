from data.models import Latest, Node, Met, Dylos, Alphasense
for n in Node.objects.all():
    print n
    l, cre = Latest.objects.get_or_create(node_id=n.node_id)
    l.name = n.name
    l.latitude = n.latitude
    l.longitude = n.longitude
    l.indoor = n.indoor
    l.save()
    print l

    try:
        m = Met.objects.filter(node_id=n.node_id).latest('added_on')
        if m:
            l.rh = m.rh
            l.temperature = m.temperature
            l.save()

    except:
        print "MET for node ",n.node_id, " failed"

    try:
        d = Dylos.objects.filter(node_id=n.node_id).latest('added_on')

        if d:
            l.dylos_bin_1 = d.dylos_bin_1
            l.dylos_bin_2 = d.dylos_bin_2
            l.dylos_bin_3 = d.dylos_bin_3
            l.dylos_bin_4 = d.dylos_bin_4
            l.save()

    except:
        print "DYlos ", n.node_id , " fauled " 
    try:
         al = Alphasense.objects.filter(node_id=n.node_id).latest('added_on')

         if al:
             l.alphasense_1 = al.alphasense_1
             l.alphasense_2 = al.alphasense_2
             l.alphasense_3 = al.alphasense_3
             l.alphasense_4 = al.alphasense_4
             l.alphasense_5 = al.alphasense_5
             l.alphasense_6 = al.alphasense_6
             l.alphasense_7 = al.alphasense_7
             l.alphasense_8 = al.alphasense_8
             l.save()
    except:
         print "alphasense " , n.node_id, "failed"
