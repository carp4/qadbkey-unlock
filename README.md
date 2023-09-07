# Quectel RM5XX ADBKEY Unlock script

This is a modification of Ryan Bradley's script to support RM5XX Series modems. It works for the RM520N-GL, RM502Q-AE, RM500Q-AE, EM120K-GL, and others.
For more information, see [Getting ADB Access](https://github.com/natecarlson/quectel-rgmii-configuration-notes#getting-adb-access).

### How To Use

To use this script, you must have the following:

* `Python >= 3`
* `The result of AT+QADBKEY? for your module.`


Once you have obtained the prerequisites, run the script with the following command:

```sh
$ sudo python3 qadbkey-unlock2.py -k <key>
```

Example:

```sh
user@linux-mint:~/qadbkey-unlock$ sudo python3 qadbkey-unlock2.py -k 37677100
AT+QADBKEY="hD0vaLg4a26u.SM"

```

### Original Contributors

* [hornetfighter515](https://github.com/hornetfighter515) — Basic script structure and debugging.
* [Ryan Bradley](https://github.com/rbradley0) – Tweaking and debugging.
* [igem](https://xnux.eu/devices/feature/qadbkey-unlock.c) – Original source code.