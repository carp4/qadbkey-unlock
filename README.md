# Quectel RM5XX ADBKEY Unlock script

This is a modification of Ryan Bradley's script to support RM5XX Series modems. It also works on the EM120K-GL modem and possibly others.

### How To Use

To use this script, you must have the following:

* `Python >= 3`
* The result of AT+QADBKEY? for your module.


Once you have obtained the prerequisites, run the script with the following command:

```sh
$ sudo python3 qadbkey-unlock2.py -k <key>
```

### Original Contributors

* [hornetfighter515](https://github.com/hornetfighter515) — Basic script structure and debugging.
* [Ryan Bradley](https://github.com/rbradley0) – Tweaking and debugging.
