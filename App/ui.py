def print_welcome_message():
    print("=== Cisco Packet Tracer Subnet Calculator Initialized ===")
    print("Press Ctrl+C to exit the program.\n")

def print_results(data: dict):
    print(f"---->Your IP-Address in BIN-code:\n        {data['ip_bin']} = {data['ip_dec']}")
    print(f"---->Your subnet mask in BIN-code:\n        {data['mask_bin']} = {data['mask_dec']}")
    print(f"------------>How many zeros in the subnet mask BIN-code:\n                {data['zeros']}")
    print(f"-------------------->Number of IP addresses in the network:\n                        {data['hosts']}")
    print(f"---------------------------->Result of logical multiplication:\n                                {data['and_result']}")
    print(f"---------------------------->It's Your Network address:\n                        {data['net_addr']}")
    print(f"-------------------->First address in network:\n                {data['first_ip']}")
    print(f"------------>Last ip address:\n        {data['last_ip']}")
    print(f"---->Broadcast ip address:\n{data['broadcast_ip']}\n")