import socket

hostname =socket.gethostname()
ip = socket.gethostbyname(hostname)

print("The name of your computer is: " + hostname)
print("This is your ip: " + ip)