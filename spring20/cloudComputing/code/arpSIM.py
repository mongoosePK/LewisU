from randmac import RandMac
from random import getrandbits
import random
from ipaddress import IPv4Address

#gotta seed it
random.seed()
#random address generators
def makev4Address():
    bits = getrandbits(32) # generates an integer with 32 random bits
    addr = IPv4Address(bits) 
    return str(addr)

def makeMACaddress(mac):
    return RandMac(f'{mac}', True)
# make some randome addresses for our sender and reciever
ip1 = makev4Address()
ip2 = makev4Address()
protoMAC = '00:00:00:00:00:00'
mac1 = makeMACaddress(protoMAC)
mac2 = makeMACaddress(protoMAC)
SYN1 = random.randint(100,999)
SYN2 = random.randint(100,999)

print(f'Source broadcasting ARP request.')
print(f'Source MAC addr: {mac1}\nSource IPv4 addr: {ip1}')
print(f'Target MAC addr: {protoMAC}\nTarget IPv4 addr: {ip2}')
print(f'Source SYN: {SYN1}\n\n')

print(f'Target at {ip2} recieves ARP request.')
print(f'Target recieves and Acknowledges {SYN1+1}. Sending Target SYN: {SYN2}')
print(f'Source MAC addr: {mac1}\nSource IPv4 addr: {ip1}')
print(f'Target MAC addr: {mac2}\nTarget IPv4 addr: {ip2}')
print(f'Source recieves and acknowledges. ACK: {SYN2+1}')
print(f'Target recieves ACK: {SYN2+1}. 3-way handshake complete, FULL DUPLEX SYNCHRONIZED')