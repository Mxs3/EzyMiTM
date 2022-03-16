from netifaces import interfaces

ifaces = interfaces()

for iface in ifaces:
    print("INTERFACE: " + iface + "\n")
