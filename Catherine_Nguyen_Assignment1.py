#Author- Gabriel Marquez, Matthew Payne, Catherine Nguyen
#Date- 01/28/2016
#Name as1v2
#Additional instuction
#Import libraries
from bs4 import BeautifulSoup
import urllib2
import requests
import ssl
#Get website url file url
url = raw_input("Enter URL: ")

File = urllib2.urlopen(url)
Html = File.read()
File.close()
soup = BeautifulSoup(Html, "html.parser")

#soup = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
for links in soup.find_all('a'):
    a = links.get('href')
    c = 'http'
    d = a[0:3]
    if c == d:
        pass
    b = requests.head(a)
    #c = ''
    #c = b.status_code
    #d = c[1:]
    #print b.status_code
    c = 'http'
    d = a[0:3]
    if c == d:
        pass

    elif  b.status_code >= 300 and b.status_code < 400:
        while b.status_code != 200:
            redi = urllib2.build_opener(urllib2.HTTPRedirectHandler)
            request = redi.open(a)
            a = request.url
            b = requests.head(a)
            #print b.status_code
            
        a1 = '.pdf'
        b1 = a[-4:]
        if a1 == b1:
            #print (b)
            print (a)
            pdf = urllib2.urlopen(a)
            bytez = pdf.headers["Content-Length"]
            print (bytez + ' bytes')
            #print 'whle loop'
            #print a
            
    elif b.status_code == 200:
        a1 = '.pdf'
        b1 = a[-4:]
        if a1 == b1:
            #print (b)
            print (a)
            pdf = urllib2.urlopen(a)
            bytez = pdf.headers["Content-Length"]
            print (bytez + ' bytes')
        
    else:
        pass
        
    





