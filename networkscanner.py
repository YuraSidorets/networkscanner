import socket
import time

socket.setdefaulttimeout(0.25)

def gethostbyName(target):
    try:
        return socket.gethostbyname(target)
    except:
        pass

def portscan(port,t_IP):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      print(port, 'is open')
      con.close()
   except:
      pass

def splitrange(range):
    return range.split('-')

def splitIP(ip):
    return ip.split('.')

def iterateIPs(iprange):
    IPs = splitrange(iprange)
    startIP = splitIP(IPs[0])
    endIP = IPs[1]

    IPpart1 = int(startIP[0])
    IPpart2 = int(startIP[1])
    IPpart3 = int(startIP[2])
    IPpart4 = int(startIP[3])
    stop = False
    for x in range(IPpart1,256):
        if stop :
            break
        for y in range(IPpart2,256):
            if stop :
                break
            for z in range(IPpart3,256):
                if stop :
                    break
                for q in range(IPpart4,256):
                    ip = [x,y,z,q]
                    ipstr = '.'.join([str(x) for x in ip])
                    if ipstr == endIP:
                        stop = True
                        break
                    t_IP = gethostbyName(ipstr)
                    print ('Starting scan on host: ', t_IP)
                    portscan(21,t_IP)
                    portscan(22,t_IP)
                    portscan(80,t_IP)
                    portscan(443,t_IP)
                    portscan(8080,t_IP)                    
                    
target = input('Enter the host range to scan (0.0.0.0-255.255.255.255): ')
startTime = time.time()

iterateIPs(target)  

print('Time taken:', time.time() - startTime)