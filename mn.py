#!/usr/bin/env python
# In The Name Of God
# ========================================
# [] File Name : mn.py
#
# [] Creation Date : 15/03/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

"""
mn.py:
    Script for running fat tree topology on mininet
    and connect it into contorller on remote host.
    it can have many remote controllers on remote hosts.
Usage (example uses IP = 192.168.1.2):
    From the command line:
        sudo python mn.py 192.168.1.2
"""
import argparse
from functools import partial

from mininet.net import Mininet
from mininet.net import CLI
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.topolib import TreeTopo


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', dest='depth', default=4, type=int,
                        help='TreeTopo depth')
    parser.add_argument('-b', '--bandwidth', dest='bandwidth', default='10M',
                        type=str, help='Test bandwidth')
    parser.add_argument('ips', metavar='ip',
                        help='ONOS Network Controllers IP Addresses',
                        default=['127.0.0.1'], type=str, nargs='*')
    cli_args = parser.parse_args()

    setLogLevel('info')

    switch = partial(OVSSwitch, protocols='OpenFlow13')

    rcs = []
    for ip in cli_args.ips:
        rcs.append(RemoteController('ONOS-%s' % ip, ip=ip, port=6633))
    net = Mininet(topo=TreeTopo(cli_args.depth, 2),
                  switch=switch, build=False)
    for rc in rcs:
        net.addController(rc)
    net.build()
    net.start()
    # net.iperf(l4Type='UDP', udpBw=cli_args.bandwidth, seconds=1)
    net.pingFull(timeout='1s')
    CLI(net)
    net.stop()
