#!/usr/bin/env python3
"""
File: qadbkey-unlock2.py
Modified by carp4 to allow AT+QADBKEY? to be entered directly and result displayed for RM5XX series modems.
Modified by iamromulan to remove the sudo reqirement and query the user to input the AT+QADBKEY? response from the modem.
Authors: hornetfighter515, FatherlyFox
Year: 2021
Version: 2.1
Credits: Original by igem, https://xnux.eu/devices/feature/qadbkey-unlock.c, https://xnux.eu/devices/feature/modem-pp.html
Description: Works to assist in unlocking ADB access for the PinePhone.
P.S. Thankyou for making a functional script hornetfighter515 ❤
"""
import hashlib
import logging
import sys

# crypt(3) truncates an MD5-crypt salt to 8 characters. Quectel's key
# derivation uses the modem serial number as the salt, so a longer serial is
# truncated too - and that also fixes where the wanted key sits in the hash.
SALT_LEN = 8

ITOA64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def _to64(value, count):
    """Little-endian base64 encoding used by crypt(3)'s md5crypt."""
    out = ""
    while count > 0:
        count -= 1
        out += ITOA64[value & 0x3F]
        value >>= 6
    return out


def md5_crypt(password, setting):
    """
    Pure-Python crypt(3) for the "$1$" (md5crypt) scheme.

    Byte-compatible with glibc crypt(), which Python exposed as crypt.crypt()
    until the crypt module was deprecated in 3.11 and removed in 3.13.

    @param password: cleartext password (encoded as UTF-8)
    @param setting: crypt setting string, either "$1$<salt>$" or "<salt>"
    """
    salt = setting[3:] if setting.startswith("$1$") else setting
    salt = salt.split("$")[0][:SALT_LEN]

    pw = password.encode("utf-8")
    s = salt.encode("utf-8")

    ctx = hashlib.md5(pw + b"$1$" + s)
    ctx1 = hashlib.md5(pw + s + pw).digest()

    pl = len(pw)
    while pl > 0:
        ctx.update(ctx1[: min(16, pl)])
        pl -= 16

    i = len(pw)
    while i:
        ctx.update(b"\x00" if i & 1 else pw[:1])
        i >>= 1

    final = ctx.digest()

    for i in range(1000):
        ctx1 = hashlib.md5()
        ctx1.update(pw if i & 1 else final)
        if i % 3:
            ctx1.update(s)
        if i % 7:
            ctx1.update(pw)
        ctx1.update(final if i & 1 else pw)
        final = ctx1.digest()

    rearranged = (
        _to64((final[0] << 16) | (final[6] << 8) | final[12], 4)
        + _to64((final[1] << 16) | (final[7] << 8) | final[13], 4)
        + _to64((final[2] << 16) | (final[8] << 8) | final[14], 4)
        + _to64((final[3] << 16) | (final[9] << 8) | final[15], 4)
        + _to64((final[4] << 16) | (final[10] << 8) | final[5], 4)
        + _to64(final[11], 2)
    )

    return "$1${0}${1}".format(salt, rearranged)


def generateUnlockKey(sn):
    """
    @param sn: the serial number to generate an unlock key for
    """
    salt = "$1${0}$".format(sn)
    c = md5_crypt("SH_adb_quectel", salt)
    return c[12:27]


# Expected output of crypt(3) on glibc, used by --self-test so the pure-Python
# implementation can be re-checked on a system that no longer has the crypt
# module. Verified against Perl's crypt() when this was written.
SELF_TEST_HASHES = [
    ("SH_adb_quectel", "$1$12345678$", "$1$12345678$0jXKXQwSwMxYoegx0S.I.1"),
    ("SH_adb_quectel", "$1$abcdefgh$", "$1$abcdefgh$GUZL0dW1aVoC2q7SnkfRk0"),
    ("SH_adb_quectel", "$1$a$", "$1$a$SUOKJvDmnZKGBd.NEj5l//"),
    ("pässwörd", "$1$salt123$", "$1$salt123$JYajdpIW9OFY0jjUk92Rj/"),
    ("", "$1$$", "$1$$qRPK7m23GJusamGpoGLby/"),
]

SELF_TEST_KEYS = [
    # serial from AT+QADBKEY? -> AT+QADBKEY unlock key
    ("12345678", "0jXKXQwSwMxYoeg"),  # the example in the README
    ("a", "mnZKGBd.NEj5l//"),  # serial shorter than the 8 character salt
    ("ABC1234567890", "AnravKmhRwK70wH"),  # serial longer than the salt
]


def selfTest():
    failures = 0
    for password, setting, expected in SELF_TEST_HASHES:
        got = md5_crypt(password, setting)
        if got != expected:
            failures += 1
            logging.error("md5_crypt(%r, %r): got %s, want %s",
                          password, setting, got, expected)
    for sn, expected in SELF_TEST_KEYS:
        got = generateUnlockKey(sn)
        if got != expected:
            failures += 1
            logging.error("generateUnlockKey(%r): got %s, want %s",
                          sn, got, expected)
    if failures:
        logging.error("%d of %d self-test vectors failed",
                      failures, len(SELF_TEST_HASHES) + len(SELF_TEST_KEYS))
        return False
    print("self-test OK ({0} vectors)".format(
        len(SELF_TEST_HASHES) + len(SELF_TEST_KEYS)))
    return True


def main():
    key = input("Enter the AT+QADBKEY? response: ")
    c = generateUnlockKey(key)
    print('AT+QADBKEY="{0}"'.format(c))


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    if "--self-test" in sys.argv[1:]:
        sys.exit(0 if selfTest() else 1)
    main()
