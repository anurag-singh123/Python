import os
import socket

# Define the network range (e.g., 192.168.1.0/24)
network_range = "192.168.1.0/24"

# Split the network range into IP address and subnet mask
ip_address, subnet_mask = network_range.split("/")
subnet_mask = int(subnet_mask)

# Calculate the number of hosts in the subnet
num_hosts = 2 ** (32 - subnet_mask)

# Create a list to store the responding IP addresses
responding_ips = []

# Iterate over the subnet range
for i in range(1, num_hosts + 1):
    # Calculate the current IP address
    current_ip = f"{ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.{i}"

    # Ping the current IP address
    response = os.system(f"ping -c 1 {current_ip}")

    # If the ping is successful, add the IP address to the list
    if response == 0:
        responding_ips.append(current_ip)

# Print the responding IP addresses
print("Responding IP addresses:")
for ip in responding_ips:
    print(f"- {ip}")
