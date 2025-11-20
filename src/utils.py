"""Utility functions for IP/prefix arithmetic."""
from typing import Tuple

def ip_to_int(ip: str) -> int:
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError(f"Invalid IPv4 address: {ip}")
    val = 0
    for p in parts:
        n = int(p)
        if n < 0 or n > 255:
            raise ValueError(f"Invalid octet: {p}")
        val = (val << 8) | n
    return val


def int_to_ip(val: int) -> str:
    return '.'.join(str((val >> (8 * i)) & 0xFF) for i in reversed(range(4)))


def prefix_to_mask(prefix: int) -> int:
    if prefix < 0 or prefix > 32:
        raise ValueError("Prefix must be between 0 and 32")
    return (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF


def hosts_from_prefix(prefix: int) -> int:
    if prefix >= 31:
        return 2 if prefix == 31 else 1
    return (1 << (32 - prefix)) - 2


def prefix_for_hosts(hosts: int) -> int:
    """Return smallest prefix that can accommodate `hosts` usable hosts."""
    if hosts <= 0:
        raise ValueError("Hosts must be positive")
    for p in range(32, -1, -1):
        usable = hosts_from_prefix(p)
        if usable >= hosts:
            return p
    raise ValueError("Cannot accommodate that many hosts")


def network_range(network_int: int, prefix: int) -> Tuple[int, int]:
    mask = prefix_to_mask(prefix)
    net = network_int & mask
    broadcast = net | (~mask & 0xFFFFFFFF)
    return net, broadcast
