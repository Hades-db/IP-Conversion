def dec_to_bin(ipdeccode: str) -> str:
    return ".".join(format(int(x), "08b") for x in ipdeccode.split("."))

def subnet_mask_to_bin(masktobin: str) -> str:
    return ".".join(format(int(x), "08b") for x in masktobin.split("."))

def count_zeros(bin_str: str) -> int:
    return bin_str.count('0')

def logical_and_with_dots(bin_str1: str, bin_str2: str) -> str:
    parts1, parts2 = bin_str1.split('.'), bin_str2.split('.')
    if len(parts1) != len(parts2):
        raise ValueError("The number of octets does not match!")
    
    result_parts = []
    for part1, part2 in zip(parts1, parts2):
        if len(part1) != len(part2):
            raise ValueError("String lengths do not match!")
        result_parts.append("".join('1' if b1 == '1' and b2 == '1' else '0' for b1, b2 in zip(part1, part2)))
    return '.'.join(result_parts)

def bin_to_dec(ipbin: str) -> str:
    return ".".join(str(int(x, 2)) for x in ipbin.split("."))

def increment_last_digit(ipdec: str) -> str:
    octets = ipdec.split('.')
    octets[-1] = str(int(octets[-1]) + 1)
    return '.'.join(octets)

def last_ip_address(lastip: str, total_hosts: int) -> str:
    octets = lastip.split('.')
    octets[-1] = str(int(octets[-1]) + total_hosts)
    return '.'.join(octets)

def broadcast_ip_address(lastip: str, total_hosts: int) -> str:
    octets = lastip.split('.')
    octets[-1] = str(int(octets[-1]) + total_hosts + 1)
    return '.'.join(octets)