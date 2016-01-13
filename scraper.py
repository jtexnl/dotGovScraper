import urllib2
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import csv
import httplib
import requests_cache
import time

linkSet = ['http://gsa.gov']
outputFile= open('scraperOutput.csv', 'w+')
output_writer=csv.writer(outputFile, lineterminator='\n')
output_writer.writerow(['url'])
requests_cache.install_cache('test_cache', backend='sqlite')

counter = 0
for i in linkSet:
	request = urllib2.Request(i)
	try:
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response)
		for a in soup.findAll('a'):
			try:
				if '.gov' in a['href']:
					if counter % 1000 == 0 and not counter == 0:
						time.sleep(180)
					if a['href'] not in linkSet:
						if not str(a['href']).startswith("mailto"):
							linkSet.append(a['href'])
							outputLink = str(a['href'])
							output_writer.writerow([outputLink])
							counter += 1
							print("processed link %i" %(counter))
						else:
							continue
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
print('scan complete')
