import urllib2
import json
import iptools
import sys

ip = sys.argv[1]
city = sys.argv[2]

while(True):

	response = urllib2.urlopen('http://ip-api.com/json/' + ip)
	data = json.load(response)

	print data['query'] + ' - City: ' + data['city'] + ' - Provider: ' + data['org'] + ' - Company: ' + data['as']

	if data['city'] == city:
		with open('ips.txt', 'a') as ipsFile:
			ipsFile.write(ip)

	ip = iptools.ipv4.ip2long(ip) + 1
	ip = str(iptools.ipv4.long2ip(ip))

# Usage: sudo pip install iptools
# python trackip.py ip city
# Example: python trackip.py 11.12.13.14 'Los Angeles'
