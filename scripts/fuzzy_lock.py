#!/usr/bin/env python3
""" lock or/and suspend """
import sys
sys.path.append("/home/pol/apps/miniconda3/lib/python3.5/site-packages")
from subprocess import Popen, DEVNULL, check_output, CalledProcessError
import time
import click

@click.command()
@click.option("-t", default = 'lock')
def run(**kwargs):
    """ lock or/and suspend """
    cmd = kwargs.pop('t', 'lock').strip().lower()
    if cmd == 'suspend':
        Popen(('systemctl', 'suspend'), stdout=DEVNULL, stderr=DEVNULL)
    elif cmd != 'lock':
        return

    Popen(('i3lock','-c', '#000000'), stdout=DEVNULL, stderr=DEVNULL)
    if cmd == 'lock':
        for _ in range(60):
            time.sleep(1)
            try:
                check_output(('pgrep', 'i3lock'))
            except CalledProcessError:
                return
    check_output(('xset', 'dpms', 'force', 'off'))

if __name__ == '__main__':
    run()
