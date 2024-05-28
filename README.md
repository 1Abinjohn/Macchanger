# MAC Address Changer

This Python script allows you to change the MAC address of a network interface on Linux systems.

## Description

This script provides a simple command-line interface to change the MAC address of a specified network interface on a Linux system. It utilizes the `ifconfig` command to bring down the interface, change its MAC address, and bring it back up.

## Features

- Change the MAC address of a specified network interface.
- Print the current MAC address before and after the change.
- Provide feedback on whether the MAC address change was successful.

## Usage

### Prerequisites

- Python 3.x
- Linux operating system

### Usage

1. Clone or download the `mac.py` script to your local machine.
2. Open a terminal window and navigate to the directory where Mac_changer.py` is located.
3. Run the script with the following command:

    ```bash
    sudo python3 mac.py -i <interface> -n <new_mac_address>
    ```

    Replace `<interface>` with the name of the network interface (e.g., eth0) and `<new_mac_address>` with the desired MAC address.

4. Follow the on-screen prompts and review the output to verify the MAC address change.

## Example

```bash
sudo python3 mac.py -i eth0 -n 00:11:22:33:44:55
