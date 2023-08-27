#!/usr/bin/env python3
"""
File: qadbkey-unlock2.py
Modified by carp4 to allow AT+QADBKEY? to be entered directly and result displayed for RM5XX series modems
Authors: hornetfighter515, FatherlyFox
Year: 2021
Version: 2.0
Credits: Original by igem, https://xnux.eu/devices/feature/qadbkey-unlock.c, https://xnux.eu/devices/feature/modem-pp.html
Description: Works to assist in unlocking ADB access for the PinePhone.
P.S. Thankyou for making a functional script hornetfighter515 ❤
"""
import logging, os, argparse

def generateUnlockKey(sn):
    """
    @param sn: the serial number to generate an unlock key for
    """
    salt = "$1${0}$".format(sn)
    c = crypt("SH_adb_quectel", salt)
    return c[12:27]

def main():
    if os.geteuid() != 0:
        logging.error('This script must be run as a superuser, preferrably using \'sudo\'')
        exit(1)
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('-k', '--key', '--adb_key', required=True, help='Specify the adbkey, e.g. AT+QADBKEY?', type=str)     
        args = parser.parse_args()
        c = generateUnlockKey(args.key)
        print('AT+QADBKEY="{0}"'.format(c))

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    try:
        from crypt import crypt
        main()
    except ImportError as e:
        logging.error(e)
