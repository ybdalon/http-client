# -*- coding: utf-8 -*-
import sys, os

def convt_IPs(ipRange):
    ''' A+range+B, range like this: 1-100
    ipRange IPV6 format: a100::1-100:1234 or a100::1-100
    ipRange IPV4 format: 100.1.1.10-200 or 100.1.2-200.0'''
    IPs=[]
    temp=ipRange.split('-')
    if ipRange.find(':')!=-1:      #IPV6
        splitS=(':')
        A=temp[0][:temp[0].rfind(splitS)+1]
        firstN=temp[0][temp[0].rfind(splitS)+1:]
        if temp[1].find(splitS)!=-1:
            B=temp[1][temp[1].find(splitS):]
            endN=temp[1][:temp[1].find(splitS)]
        else:
            B=''
            endN=temp[1]
        firstint=int(firstN, 16)
        endint=int(endN, 16)
        for i in range(firstint, endint+1):
            IPs.append(A+hex(i)[2:]+B)
        return IPs
    elif ipRange.find('.')!=-1:    #IPV4
        splitS=('.')
        A=temp[0][:temp[0].rfind(splitS)+1]
        firstN=temp[0][temp[0].rfind(splitS)+1:]
        if temp[1].find(splitS)!=-1:
            B=temp[1][temp[1].find(splitS):]
            endN=temp[1][:temp[1].find(splitS)]
        else:
            B=''
            endN=temp[1]
        for i in range(int(firstN), int(endN)+1):
            IPs.append(A+str(i)+B)
        return IPs

def add_client_sip(IPs, interface='eth0'):
    if sys.platform.find('win')!=-1:
        for ip in IPs:
            if ip.find(':')==-1:
                os.system("netsh int ip add address %s %s 255.255.255.0"%(interface, ip))
                print "netsh int ip add address %s %s 255.255.255.0"%(interface, ip)
            else:
                os.system("netsh int ipv6 add address %s %s/64"%(interface, ip))
                print "netsh int ipv6 add address %s %s/64"%(interface, ip)
    elif sys.platform=='linux2':
        i=1
        for ip in IPs:
            if ip.find(':')==-1:
                os.system("ifconfig %s:%d %s/24"%(interface, i, ip))
                print "ifconfig %s:%d %s/24"%(interface, i, ip)
                i+=1
            else:
                os.system("ifconfig %s add %s/64"%(interface, ip))
                print "ifconfig %s add %s/64"%(interface, ip)
    else:
        print "unknow system platform!"
        return 0
    print "add those IPs successful"
    return 1

def delete_client_sip(IPs, interface='eth0'):
    if sys.platform.find('win')!=-1:
        for ip in IPs:
            if ip.find(':')==-1:
                os.system("netsh int ip delete address %s %s"%(interface, ip))
            else:
                os.system("netsh int ipv6 delete address %s %s"%(interface, ip))
    if sys.platform=='linux2':
        for ip in IPs:
            if ip.find(':')==-1:
                os.system("ip addr del %s dev %s"%(ip, interface))
            else:
                os.system("ifconfig %s del %s/64"%(interface, ip))
    print "delete those IPs successful!"