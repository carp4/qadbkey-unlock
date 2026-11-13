# Quectel RM5XX ADBKEY Unlock script

This is a modification of Ryan Bradley's script to support RM5XX Series modems. It works for the RM520N-GL, RM502Q-AE, RM500Q-AE, EM120K-GL, and others.
For more information, see [Unlocking ADB](https://github.com/iamromulan/cellular-modem-wiki/blob/main/quectel/sdxlemur/sdxlemur_m.2_to_eth.md#unlocking-adb).
This will allow you to replace the Quectel Forums step of the guide with an easier and faster method.

Modified by [carp4](https://github.com/carp4) to allow AT+QADBKEY? to be entered directly and result displayed for RM5XX series modems.

Modified by [iamromulan](https://github.com/iamromulan) to remove the sudo reqirement and query the user to input the AT+QADBKEY? response from the modem.

### How To Use
* To use this script, simply go to the following URL:
https://onecompiler.com/python/4592mhb32

* Then replace the 12345678 with your responce from AT+QADBKEY? and click run

Your adb unlock key command will be generated under output


Alternatively, download and run the script with any Python 3 interpreter. It only uses the standard library and no longer needs the `crypt` module (removed from Python 3.13), so it runs on Linux, macOS, Windows, Termux and so on:

```sh
$ python3 /path/to/qadbkey-unlock2.py
```

You can check the key derivation still works on your interpreter with the built-in self test (it compares against MD5-crypt vectors known to match glibc `crypt()`):

```sh
$ python3 qadbkey-unlock2.py --self-test
self-test OK (8 vectors)
```

Example:
* In this example the script exists in the users home directory 
```sh
user@linuxcomputer:~$ python3 qadbkey-unlock2.py
Enter the AT+QADBKEY? response: 12345678
AT+QADBKEY="0jXKXQwSwMxYoeg"

```

### Original Contributors

* [hornetfighter515](https://github.com/hornetfighter515) — Basic script structure and debugging.
* [Ryan Bradley](https://github.com/rbradley0) – Tweaking and debugging.
* [igem](https://xnux.eu/devices/feature/qadbkey-unlock.c) – Original source code.