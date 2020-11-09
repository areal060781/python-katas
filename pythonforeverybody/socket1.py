'''
Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly formatted or non-existent URL.
'''
import socket
import re

try:
    #url = 'http://data.pr4e.org/romeo.txt'
    url = input('Enter - ')
    y = re.findall('http[s]?://(.*)', url)
    host, page = y[0].split('/')
    print(host)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    strcmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'

    if len(strcmd) <= 0:
        raise Exception('This is not a page web')
except Exception as e:
    print(e)
else:
    print(strcmd)

    cmd = strcmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
