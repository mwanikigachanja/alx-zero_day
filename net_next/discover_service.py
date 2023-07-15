import socket

# Define the list of servers
servers = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

# Discover active services on servers
for server in servers:
    try:
        services = []
        for port in range(1, 100):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((server, port))
            if result == 0:
                service_name = socket.getservbyport(port)
                services.append((service_name, port))
            sock.close()
        print(f"Services on {server}: {services}")
    except socket.gaierror:
        print(f"Error occurred while connecting to {server}")

