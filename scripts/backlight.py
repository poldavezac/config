#!/usr/bin/python3
import os
import sys
def xrandrbrightness(argv):
    val  = float(os.popen("xrandr --verbose | grep -m 1 -i brightness | cut -f2 -d ' '").read())

    if len(argv) == 1:
        print(val)
    else:
        if argv[1] in ('inc', '+'):
            val += .1
        elif argv[1] in ('dec', '-'):
            val += -.1
        val = min(1., max(0., val))
        os.system("xrandr --output eDP --brightness %.1f" % val)

def sysclass(argv):
    path    = "/sys/class/backlight/amdgpu_bl0/"

    with open(path+'max_brightness', 'r') as stream:
        maxval = int(stream.readline())
    with open(path+'actual_brightness', 'r') as stream:
        val    = int(stream.readline())

    if len(argv) == 1:
        print(val)
    else:
        if argv[1] in ('inc', '+'):
            val += 10
        elif argv[1] in ('dec', '-'):
            val += -10
        val = min(maxval, max(0, val))

        with open(path+'brightness', 'w') as stream:
            print(val, file = stream)

if __name__ == '__main__':
    sysclass(sys.argv)
