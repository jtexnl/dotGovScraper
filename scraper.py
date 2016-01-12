import urllib2
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import csv
import httplib

linkSet = ['http://gsa.gov']
outputFile= open('scraperOutput.csv', 'w+')
output_writer=csv.writer(outputFile, lineterminator='\n')
output_writer.writerow(['url'])

for i in linkSet:
	print("processing " + i)
	request = urllib2.Request(i)
	try:
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response)
		for a in soup.findAll('a'):
			try:
				if '.gov' in a['href']:
					if a['href'] not in linkSet:
						linkSet.append(a['href'])
						outputLink = str(a['href'])
						output_writer.writerow([outputLink])
			except KeyError:
				continue
	except urllib2.HTTPError, e:
		continue
	except urllib2.URLError, e:
		continue
	except ValueError:
		continue
	except httplib.BadStatusLine, e:
		continue


print linkSet
