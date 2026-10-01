def save_results_to_file(filename: str, data: dict):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"---->Your IP-Address in BIN-code:\n        {data['ip_bin']} = {data['ip_dec']}\n")
        file.write(f"---->Your subnet mask in BIN-code:\n        {data['mask_bin']} = {data['mask_dec']}\n")
        file.write(f"------------>How many zeros in the subnet mask BIN-code:\n                {data['zeros']}\n")
        file.write(f"-------------------->Number of IP addresses in the network:\n                        {data['hosts']}\n")
        file.write(f"---------------------------->Result of logical multiplication:\n                                {data['and_result']}\n")
        file.write(f"---------------------------->It's Your Network address:\n                        {data['net_addr']}\n")
        file.write(f"-------------------->First address in network:\n                {data['first_ip']}\n")
        file.write(f"------------>Last ip address:\n        {data['last_ip']}\n")
        file.write(f"---->Broadcast ip address:\n{data['broadcast_ip']}\n")
        file.write("\n")