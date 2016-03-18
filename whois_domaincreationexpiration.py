#!/usr/bin/python

import sys
import pythonwhois # http://cryto.net/pythonwhois/index.html
import datetime
#*******************************************************************************
# FUNCTIONS
#*******************************************************************************
def in_unix(input):
  start = datetime.datetime(year=1970,month=1,day=1)
  diff = input - start
  return diff.total_seconds()

#*******************************************************************************
# MAIN
#*******************************************************************************
if __name__ == '__main__':

	if len(sys.argv) != 2:
		print "\nERROR: enter a domain name!\n"
	else:
		domain = sys.argv[1]
		whois_domain = pythonwhois.get_whois(domain) #dictionary

		if 'creation_date' and 'expiration_date' in whois_domain.keys():
			print str(in_unix(whois_domain['creation_date'][0]))+";"+str(in_unix(whois_domain['expiration_date'][0]))+";"+str(sys.argv[1])
		else:
			print "none;none;",sys.argv[1]
sys.exit(0)
