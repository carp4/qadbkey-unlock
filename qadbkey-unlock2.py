#!/usr/bin/env python3
"""
File: qadbkey-unlock2.py
Modified by carp4 to allow AT+QADBKEY? to be entered directly and result displayed for RM5XX series modems.
Modified by iamromulan to remove the sudo reqirement and query the user to input the AT+QADBKEY? response from the modem.
Authors: hornetfighter515, FatherlyFox
Year: 2021
Version: 2.0
Credits: Original by igem, https://xnux.eu/devices/feature/qadbkey-unlock.c, https://xnux.eu/devices/feature/modem-pp.html
Description: Works to assist in unlocking ADB access for the PinePhone.
P.S. Thankyou for making a functional script hornetfighter515 ❤
"""
import logging
import os
import argparse
import sys

def generateUnlockKey(sn):
    """
    @param sn: the serial number to generate an unlock key for
    """
    salt = "$1${0}$".format(sn)
    c = crypt("SH_adb_quectel", salt)
    return c[12:27]

def main():
        key = input("Enter the AT+QADBKEY? response: ")
        c = generateUnlockKey(key)
        print('AT+QADBKEY="{0}"'.format(c))

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    try:
        from crypt import crypt
        main()
    except ImportError as e:
        logging.error(e)
