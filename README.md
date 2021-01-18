## proxygraber
Proxy collector and parser

usage: proxygrab 
proxygrab [options]... 
This program  isn’t designed for production use. It’s advised to use your own proxies 
or purchase a service which provides an API. These are merely free ones that are retrieved 
from sites and should only be used for development or testing purposes. Proxy Scrape is a library aimed
at providing an efficient an easy means of retrieving proxies for web-scraping purposes. The proxies retrieved are available
from sites providing free proxies. 
 -o   --output   :mention output filename. default they are set to random number. if mentioned name exist
 				  output filename will have a random number in tail.
 -t   --type     :type of proxy, options [ http , https, socks4, socks5, all ]. default value is all
 -v   --verbose  :print all proxies on screen.
 -h   --help     :show document about proxygraber, user manual.
 -V   --version  :print version number and exit.
 examples: 
	
  'proxygrab -o filename'
	
	"proxygrab -v -o filename"
  
	"proxygrab -o filename -t http,https -v"
  
#How to install in Linux and mac 

run the *install.py*, it will install and copy the files to env path.

"proxygrab" 
will start the script, if you want to give arguments them do 'proxygrab -t http'


