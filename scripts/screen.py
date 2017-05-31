#!/usr/bin/python3
u"stops eDP and starts other screen"
import re
import subprocess

def run():
    u"stops eDP and starts other screen"
    match = re.compile(b'(?P<N>[^ ]*).* connected')
    lines = iter(l for l in subprocess.check_output(b"xrandr").split(b'\n'))
    lines = iter(match.match(l) for l in lines)
    lines = tuple(r.group("N") for r in lines if r is not None)

    subprocess.check_output([b"xrandr", b"--auto"])
    if len(lines) >= 2:
        subprocess.check_output([b"xrandr", b"--output", b"eDP", b"--off"])

        port = next(iter(set(lines) - {'eDP'}))
        subprocess.check_output([b"xrandr", b"--output", port, b"--primary"])

if __name__ == '__main__':
    run()
