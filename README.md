# Quectel RM5XX ADBKEY Unlock script

This is a modification of Ryan Bradley's script to support RM5XX Series modems. It works for the RM520N-GL, RM502Q-AE, RM500Q-AE, EM120K-GL, and others.
For more information, see [Getting ADB Access](https://github.com/natecarlson/quectel-rgmii-configuration-notes#getting-adb-access).
This will allow you to replace the Quectel Forums step of the guide with an easier and faster method.

Modified by [carp4](https://github.com/carp4) to allow AT+QADBKEY? to be entered directly and result displayed for RM5XX series modems.

Modified by [iamromulan](https://github.com/iamromulan) to remove the sudo reqirement and query the user to input the AT+QADBKEY? response from the modem.

### How To Use
* To use this script, simply go to the following URL:
https://onecompiler.com/python/3znepjcsq

* Then replace the 12345678 with your responce from AT+QADBKEY? and click run
Your adb unlock key command will be generated under output


Alternatively, download and run the script from an environment that supports python3 and crypt with the following command:

```sh
$ python3 qadbkey-unlock2.py
```

Example:

```sh
user@linuxcomputer:~$ python3 qadbkey-unlock2.py
Enter the AT+QADBKEY? response: 12345678
AT+QADBKEY="0jXKXQwSwMxYoeg"

```

### Original Contributors

* [hornetfighter515](https://github.com/hornetfighter515) — Basic script structure and debugging.
* [Ryan Bradley](https://github.com/rbradley0) – Tweaking and debugging.
* [igem](https://xnux.eu/devices/feature/qadbkey-unlock.c) – Original source code.