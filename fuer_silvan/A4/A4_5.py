#!/usr/bin/env python3

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    if octet.isdigit():
        val = int(octet)
        if 0 <= val <= 255:
            return True
        else:
            return False
    else:
        return False


def is_valid_IPv4(ip):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not is_valid_IPv4_octet(octet):
            return False
    return True


def is_valid_IPv6_hextet(hextet):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    try:
        int(hextet, 16)
        val = int(hextet, 16)
        if 0 <= val <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False




def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    hextets = ip.split(":")
    if len(hextets) != 8:
        return False
    for hextet in hextets:
        if not is_valid_IPv6_hextet(hextet):
            return False
    return True



def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if is_valid_IPv4(ip):
        return True
    elif is_valid_IPv6(ip):
        return True
    else:
        return False


# You should look at task/test.py and extend the test suite we provided!

