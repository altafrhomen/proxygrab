#!/usr/bin/python3

import sys , datetime, time
import os
from proxyscrape import create_collector
import requests

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
    	return False

def get_proxy(target):
	collector = create_collector('my-collector', target)
	proxies = collector.get_proxies()
	return proxies
#doc
doc = """usage: proxygrab 

proxygrab [options]... 
This program  isn’t designed for production use. It’s advised to use your own proxies 
or purchase a service which provides an API. These are merely free ones that are retrieved 
from sites and should only be used for development or testing purposes. Proxy Scrape is a library aimed
at providing an efficient an easy means of retrieving proxies for web-scraping purposes. The proxies retrieved are available
from sites providing free proxies. 

 -o   --output   :mention output filename. default they are set to random number. if mentioned name exist
 				  output filename will have a random number in tail.

 -t   --type     :type of proxy, options [ http , https, socks4, socks5, all ]. default value is http, https

 -v   --verbose  :print all proxies on screen.

 -h   --help     :show document about proxygraber, user manual.

 -V   --version  :print version number and exit.

 examples: 
	proxygrab -o filename
	
	proxygrab -t all

	proxygrab -o filename -t http,https -v

Copyright (c) 2021 altafrhomen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

"""

ver= "1.0"
def exexit():
	sys.exit()
#clear fuction
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

if check_internet():
#default values
	
	data=[ "http", "https", "socks4","socks5"]
	loc= datetime.datetime.now().strftime("%H:%M:%S")
	location=os.getcwd()
	prt=False
	ex=False

	#argument extraction from terminal
	insert=sys.argv
	try:
		if "-t" in insert or "--type" in insert :
			index = (insert.index('-t')+1)
			if 'all' in insert:
				data=allval
			else:
				val=insert[index]
				if ',' in val:
					data=val.split(',')
				else:
					data=val

		if "-o" in insert or '--output' in insert:
			try:
				fileloc = (insert.index('-o')+1)
			except:
				fileloc = (insert.index('--output')+1)
			loc=insert[fileloc]
		
		if "-h" in insert or '--help' in insert:
			print(doc)
			ex=True
	
		if "-v" in insert or "--verbose" in insert:
			prt=True

		if "-V" in insert or "--version" in insert:
			print('Proxygrab version {}'.format(ver))
			ex=True
		
	except:
		pass
	if ex:
		exexit()
	#file writing 
	try:
		filesys = open(loc, "w+")
	except:
		loc="Proxylist"
		filesys = open(loc, "w+")
		
	print('[+] ProxyGrab v1.0')
	#collecting Proxy
	print("[+] Collecting proxies may take some minute.")
	proxies=get_proxy(data)
	print("[+] {} Proxies collected.".format(len(proxies)))
	if prt:
		clear()
	for proxy in proxies:

		host = proxy[0]
		port=proxy[1]
		proxytype=proxy[5]
		source=proxy[6]
		
		#write string print('I have {} {}'.format(a, b))
		varin=('%s:%s    type:%s    source:%s \n'%(host,port,proxytype,source))
		#write to file
		filesys.write(varin)
		if prt:
			print(varin)

	#print(proxies)

	filesys.close()
	time.sleep(0.3)
	print("[+] File completed.")
	#print on screen function
	time.sleep(0.3)
	print("[+] Sequence completed")
else:
	print("[error] No Internet Connection. Check your Connection, Firewall, Configuration, etc ")
	
