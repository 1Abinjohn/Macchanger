#!/usr/bin/env python

"""
Author: ABIN-JOHN
"""

import subprocess
import optparse
import re


def print_logo():
    logo = """
 ,__                                       .           
 /  `         ____   __.    ___  `   ___  _/_   ,    . 
 |__  .---'  (     .'   \ .'   ` | .'   `  |    |    ` 
 |           `--.  |    | |      | |----'  |    |    | 
 |          \___.'  `._.'  `._.' / `.___,  \__/  `---|.
 /                                               \___/ 
 
    """
    print(logo)


def argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Use the argument to select Interface")
    parser.add_option("-n", "--newmac", dest="new_mac", help="Use the argument to change the MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify the interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[+] Please specify the MAC address, use --help for more info")
    return options


def changemac(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def getmac(interface):
    result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_adder_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

    if mac_adder_search:
        return mac_adder_search.group(0)
    else:
        print("[-] Could not read MAC address")
        return None


print_logo()

options = argument()
currentmac = getmac(options.interface)
if currentmac:
    print("Current MAC Address = " + str(currentmac))

    changemac(options.interface, options.new_mac)

    currentmac = getmac(options.interface)

    if currentmac == options.new_mac:
        print("[+] MAC address was successfully changed to " + currentmac)
    else:
        print("[-] MAC address did not get changed")
else:
    print("[-] Failed to retrieve current MAC address, aborting MAC address change")
