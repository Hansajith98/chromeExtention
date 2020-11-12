from urllib.parse import urlparse,urlencode
import ipaddress
import re

def havingIP(url):
  try:
    ipaddress.ip_address(url)
    ip = 1
  except:
    ip = 0
  return ip