from App.ui import print_welcome_message, print_results
from App.calculator import *
from App.logger import save_results_to_file

def main():
    print_welcome_message()
    
    while True:
        try:
            ip_dec = input("$:-Enter IP-Address for conversion in BIN-code ==> ")
            if not ip_dec: continue
                
            mask_to_bin = input("$:-Enter Subnet mask ==> ")
            if not mask_to_bin: continue


            ip_bin_result = dec_to_bin(ip_dec)
            mask_bin_result = subnet_mask_to_bin(mask_to_bin)
            zero_count = count_zeros(mask_bin_result)
            
            hosts_count = (2 ** zero_count) - 2
            and_result = logical_and_with_dots(ip_bin_result, mask_bin_result)
            net_addr = bin_to_dec(and_result)
            
            first_ip = increment_last_digit(net_addr)
            last_ip = last_ip_address(net_addr, hosts_count)
            broadcast_ip = broadcast_ip_address(net_addr, hosts_count)


            report_data = {
                'ip_dec': ip_dec, 'ip_bin': ip_bin_result,
                'mask_dec': mask_to_bin, 'mask_bin': mask_bin_result,
                'zeros': zero_count, 'hosts': hosts_count,
                'and_result': and_result, 'net_addr': net_addr,
                'first_ip': first_ip, 'last_ip': last_ip, 'broadcast_ip': broadcast_ip
            }


            print_results(report_data)
            save_results_to_file("outputdata.txt", report_data)

        except KeyboardInterrupt:
            print("\nExiting program. Goodbye!")
            break
        except Exception as e:
            print(f"\nERROR: {e}. TRY AGAIN\n")

if __name__ == "__main__":
    main()
