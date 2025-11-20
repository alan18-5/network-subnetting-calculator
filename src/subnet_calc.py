"""Subnetting CLI tool

Usage:
    python -m src.subnet_calc 192.168.1.0/24 --subnets 4
    python -m src.subnet_calc 10.0.0.0/8 --hosts 500
"""
import argparse
from math import ceil, log2
from typing import List, Tuple
from src.utils import (
    ip_to_int, int_to_ip,
    prefix_to_mask, network_range,
    hosts_from_prefix, prefix_for_hosts
)


def parse_network(s: str) -> Tuple[int, int]:
    if '/' not in s:
        raise argparse.ArgumentTypeError('Network must be like 192.168.0.0/24')
    ip_str, pfx = s.split('/')
    ip_i = ip_to_int(ip_str)
    prefix = int(pfx)
    if prefix < 0 or prefix > 32:
        raise argparse.ArgumentTypeError('Prefix must be 0..32')
    return ip_i, prefix


def calc_by_subnets(network_ip: int, prefix: int, subnets: int) -> List[dict]:
    if subnets <= 0:
        raise ValueError('subnets must be > 0')
    add_bits = ceil(log2(subnets))
    new_prefix = prefix + add_bits
    if new_prefix > 32:
        raise ValueError('Too many subnets for given network')

    subnet_size = 1 << (32 - new_prefix)
    result = []
    base_net = network_ip & prefix_to_mask(prefix)

    for i in range(subnets):
        net = base_net + i * subnet_size
        broadcast = net + subnet_size - 1
        usable = max(0, subnet_size - 2)
        result.append({
            'index': i,
            'network': int_to_ip(net),
            'broadcast': int_to_ip(broadcast),
            'first_host': int_to_ip(net + 1) if usable else 'N/A',
            'last_host': int_to_ip(broadcast - 1) if usable else 'N/A',
            'prefix': new_prefix,
            'usable_hosts': usable,
        })
    return result


def calc_by_hosts(network_ip: int, prefix: int, hosts: int) -> List[dict]:
    new_prefix = prefix_for_hosts(hosts)
    if new_prefix < prefix:
        raise ValueError('Requested hosts require a larger network than provided')

    total_subnets = 1 << (new_prefix - prefix)
    subnet_size = 1 << (32 - new_prefix)
    result = []
    base_net = network_ip & prefix_to_mask(prefix)

    for i in range(total_subnets):
        net = base_net + i * subnet_size
        broadcast = net + subnet_size - 1
        usable = max(0, subnet_size - 2)
        result.append({
            'index': i,
            'network': int_to_ip(net),
            'broadcast': int_to_ip(broadcast),
            'first_host': int_to_ip(net + 1) if usable else 'N/A',
            'last_host': int_to_ip(broadcast - 1) if usable else 'N/A',
            'prefix': new_prefix,
            'usable_hosts': usable,
        })
    return result


def print_subnets(items):
    line = '=' * 72
    print(line)
    for it in items:
        print(f"Subnet #{it['index']}: {it['network']}/{it['prefix']}")
        print(f"  Network:   {it['network']}")
        print(f"  Broadcast: {it['broadcast']}")
        print(f"  First:     {it['first_host']}")
        print(f"  Last:      {it['last_host']}")
        print(f"  Usable:    {it['usable_hosts']}")
        print(line)


def main():
    parser = argparse.ArgumentParser(description='Hacker-style Subnetting CLI')
    parser.add_argument('network', type=parse_network, help='Network in form A.B.C.D/P')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--subnets', type=int, help='Number of subnets to divide into')
    group.add_argument('--hosts', type=int, help='Number of usable hosts required per subnet')

    args = parser.parse_args()
    net_ip, prefix = args.network

    if args.subnets:
        items = calc_by_subnets(net_ip, prefix, args.subnets)
    else:
        items = calc_by_hosts(net_ip, prefix, args.hosts)

    print_subnets(items)


if __name__ == '__main__':
    main()
