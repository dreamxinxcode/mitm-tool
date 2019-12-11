import netifaces
import socket
import fcntl
import struct 
import ipaddress

# get current interface
current_interface = netifaces.gateways()['default'][netifaces.AF_INET][1]

# get IP of current interface
interface_ip = netifaces.ifaddresses(current_interface)[netifaces.AF_INET][0]['addr']

# determine netmask
net = ipaddress.ip_network(interface_ip)
netmask = net.netmask