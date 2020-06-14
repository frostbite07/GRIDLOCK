from socket import * 
import time 

startTime = time.time()

def portsniffer_gg():
    print("\nScanning for Handshake...")
    time.sleep(8)
    print("\nFound Handshake!\nRunning Brute Force...")
    time.sleep(2)
    return 1

def portsniff():    
    if __name__ == '__main__': 
        target = input('Enter the host to be scanned: ') 
        t_IP = gethostbyname(target) 
        print ('Starting scan on host: ', t_IP) 
        
        for i in range(50, 500): 
            s = socket(AF_INET, SOCK_STREAM) 
    
            conn = s.connect_ex((t_IP, i))
            if(conn == 0) : 
                print ('Port %d: OPEN' % (i,)) 
            s.close() 
    print('Time taken:', time.time() - startTime)