#!/bin/python
#encoding = utf-8

import urllib2, socket
import sys, re


try:
    import requests
except:
    print "No se encontraron los componentes necesarios. Instale para seguir adelante\n"
    sys.exit()

wordlist = sys.argv[1]
socket.setdefaulttimeout(5)
sys.tracebacklimit = 0

print "\n################################################"
print "# _______________________________________________#"
print "# Escrito por 0x4171341                          #"
print "# Herramienta para el uso de proxys              #"
print "##################################################\n\n"

print '------------------------------------------------'
print 'Uso: Uso correcto python proxy.py <proxylist.txt>'
print 'Formado IP:Sitio'
print 'Proxys'
print '------------------------------------------------'

# leer lista de proxys



proxyList = open(wordlist, 'r').readlines()

print "**Leyendo Proxys**"
print "....."

len(proxyList)
            
def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009022111 Gentoo Firefox/3.0.6')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://createssh.com')
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
             return e.code
    except Exception:
             return 1

for item in proxyList:
    if is_bad_proxy(item):
	print "chequeando su conexion :(", item
    else:
        print "Chequeando su conexion :D", item


