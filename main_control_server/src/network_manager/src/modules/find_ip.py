import socket

def get_network_manager_ip():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Connect to an external server to get the local IP address
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
    finally:
        sock.close()

    # Assuming task_manager runs on the same local network, use local_ip to determine its IP address
    # This is a placeholder for the actual logic to discover the task_manager IP
    network_manager_ip = local_ip  # Replace this with the actual discovery mechanism

    return network_manager_ip

network_manager_ip = get_network_manager_ip()
print(f" Network Manager IP: { network_manager_ip}")