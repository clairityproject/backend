# select from db
import MySQLdb
import sys

db=MySQLdb.connect(host="localhost", user="website",passwd="CryShar0", db="cee_website")
#c = db.cursor()
#c2 = db.cursor()
#
## get all dylos
#c.execute("""select id, node_id, dylos_bin_1, dylos_bin_2, dylos_bin_3, dylos_bin_4 from data_dylos""")
#
#for x in c.fetchall():
#    _id, node_id, dylos1, dylos2, dylos3, dylos4 = x
#    c2.execute("update data_dylos set small_particles=%s, big_particles=%s where id=%s", (dylos1 + dylos2 + dylos3, dylos4, _id))
#    sys.stdout.write('.')
#
#print " "
#print "dylos complete"
#print "Press key to continue . . . ."
#sys.stdin.readline()
#print " "
#
c = db.cursor()
c2 = db.cursor()
c3 = db.cursor()

for nnum in xrange(1, 26):
    print nnum
    try:
	    c.execute("select id,node_id,alphasense_1,alphasense_2,alphasense_3,alphasense_4,alphasense_5,alphasense_6,alphasense_7,alphasense_8 from data_alphasense where no is null and node_id=%s", (nnum,))
	    c3.execute("select * from data_sensordetail where node_id=%s", (nnum,))

    except Exception as e:
        print "An error occured"
        print str(e)
        print "stopping alph at node number ", nnum
        sys.exit(1)
    try:
        ______id, _____node_id, no_serial, o3_serial, no2_serial, co_serial, no_electronic_we_zero, no_total_we_zero, no_electronic_aux_zero, no_total_aux_zero, no_electronic_we_sens, no_total_we_sens, o3_electronic_we_zero, o3_total_we_zero, o3_electronic_aux_zero, o3_total_aux_zero, o3_electronic_we_sens, o3_total_we_sens, no2_electronic_we_zero, no2_total_we_zero, no2_electronic_aux_zero, no2_total_aux_zero, no2_electronic_we_sens, no2_total_we_sens, co_electronic_we_zero, co_total_we_zero, co_electronic_aux_zero, co_total_aux_zero, co_electronic_we_sens, co_total_we_sens = c3.fetchone()
    except:
        continue

    for x in c.fetchall():
        _id,node_id,alphasense_1,alphasense_2,alphasense_3,alphasense_4,alphasense_5,alphasense_6,alphasense_7,alphasense_8 = x
        # multiplications by 1000 are conversions from ppm -> ppb
        # no
        no = ((alphasense_1- no_electronic_we_zero) - ((alphasense_2)- no_electronic_aux_zero))/no_total_we_sens
        no = no * 1000
        # o3
        o3 = (((alphasense_3)- o3_electronic_we_zero) - ((alphasense_4)- o3_electronic_aux_zero))/o3_total_we_sens
        o3 = o3 * 1000
        # co
        co = (((alphasense_5)- co_electronic_we_zero) - ((alphasense_6)- co_electronic_aux_zero))/co_total_we_sens
        co = co * 1000
        # no2
        no2 = (((alphasense_7)- no2_electronic_we_zero) - ((alphasense_8)- no2_electronic_aux_zero))/no2_total_we_sens
        no2 = no2 * 1000

        c2.execute("update data_alphasense set no=%s, o3=%s, co=%s, no2=%s where id=%s",(no,o3,co,no2,_id))
        sys.stdout.write('.')

