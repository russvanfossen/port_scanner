from socket import *

def scan(host, ports):
    setdefaulttimeout(1)
    conn = socket(AF_INET, SOCK_STREAM)
    hostIP = gethostbyname(host)
    for port in ports:
        try:
            conn.connect((hostIP, port))
        except TimeoutError:
            print(f'Port {port} closed on {host}')
        else:
            print(f'Port {port} open on {host}')
            conn.close()

            

if __name__ == '__main__':

    scan('scanme.nmap.org', [*range(22,23,1)])