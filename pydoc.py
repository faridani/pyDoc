# -*- coding: utf-8 -*-

# script by @siah 

import urllib2

DOCID = "1vhPW2O35duAQWuF78b306_5gsPBjq7Jiygdt9U-iIdc" 

googfile = "https://docs.google.com/document/d/" + DOCID +"/export?format=txt&id=" + DOCID




def download(url, localfile):
	# this is downloaded from the internet. I did not write this part ;)
	import urllib
	webFile = urllib.urlopen(url)
	localFile = open(localfile, 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()

download(googfile, "test.py")

import codecs
f = codecs.open("test.py", "r", "utf-8")
text = f.read()
from unidecode import unidecode
text = unidecode(text) # this line takes care of smart qoutes and other garbage that google doc adds

localFile = open('py.py', 'w')
localFile.write(text)
