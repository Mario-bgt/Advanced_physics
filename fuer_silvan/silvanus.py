#!/usr/bin/env python3

#IPv4 between 0-255, 4 numbers split by three dots
#IPv6 between 0-FFF, (lenght needs to be checked, total not)8 "numbers" split by seven :
def is_valid_IPv4_octet(octet):
    if octet.isdigit():
        if 0 <= int(octet) <= 255:
            return True
    return False

def is_valid_IPv4(ip):
    if len(ip.split(".")) != 4:
        return False
    for n in ip.split("."):
        if is_valid_IPv4_octet(n) != True:
            return False
    return True

def is_valid_IPv6_hextet(hextet):
    for i in hextet:
        try:
            int(hextet, 16)
            if 0 <= int(hextet, 16) <= 65535:
                return True
        except ValueError:
            return False

def is_valid_IPv6(ip):
    for n in ip.split(":"):
        if is_valid_IPv6_hextet(n) != True:
            return False
    return True

def is_valid_IP(ip):
    if is_valid_IPv4(ip) == True or is_valid_IPv6(ip) == True:
        return True
    else:
        return False

print(is_valid_IPv4("222.0.12.34"))
print(is_valid_IPv6_hextet("ABCD"))
print(is_valid_IPv6_hextet("EFGH"))
print(is_valid_IPv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(is_valid_IPv6("2001:0B8:85A3:0000:0000:8A2E:0370:7334"))