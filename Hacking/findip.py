import socket

hostname = 'infosys.com'
ip_address = socket.gethostbyname(hostname)
print(f'The IP address of {hostname} is {ip_address}')
