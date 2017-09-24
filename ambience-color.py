#!/usr/bin/python3
import time
import colorsys
import subprocess
import random
import sys, argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--random', action='store_true', help='Change color randomly')
group.add_argument('-t', '--time', action='store_true', help='Change color based on time')
group.add_argument('-i', '--incremental', nargs='?', const=1, type=int, help='Loop through each color incrementally')
group.add_argument('-m', '--manual', type=float, help='Set the ambience color manually')
parser.add_argument('-n', '--nighttime', nargs=2, default=[22,8], metavar=('start, duration'), type=int, help='Color stays at red during night time')
parser.add_argument('-e', '--interval', default=15, type=int, help='Set the color updating interval in minutes')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
args = parser.parse_args()
hue = 0.0

def hsvToWeb(h,s,v):
    rgb = colorsys.hsv_to_rgb(h,s,v)
    web = "#" + format(int(rgb[0]*255), '02x') + format(int(rgb[1]*255), '02x') + format(int(rgb[2]*255), '02x')
    return web

def changeColor(hue):
    cmd1 = "dconf write /desktop/jolla/theme/color/highlight '{0}'".format(hsvToWeb(hue,0.5,1.0))
    cmd2 = "dconf write /desktop/jolla/theme/color/secondaryHighlight '{0}'".format(hsvToWeb(hue,0.5,0.8))
    subprocess.call(cmd1.split(), shell=False)
    subprocess.call(cmd2.split(), shell=False)
    if args.verbose:
        print("Colors changed {0} ".format(hsvToWeb(hue,1.0,1.0)), end="")


def randomColor():
    hue = random.random()
    changeColor(hue)

def timeColor():
    hrs = time.localtime().tm_hour + float(time.localtime().tm_min) / 60
    start = args.nighttime[0]
    duration = args.nighttime[1]
    offset = 24.0 - start
    hue = max(0.0,((hrs % start + offset - duration) / (24 - duration)))
    changeColor(hue)

def incrementalColor(step):
    hue = (hue + step) % 1.0

def timeSync(interval):
    timeNow = time.localtime()
    timeSeconds = ((timeNow.tm_hour * 60) + timeNow.tm_min * 60) + timeNow.tm_sec
    update = 60 - (timeSeconds % (60*interval))
    if args.verbose:
        print('Update in {0} seconds'.format(update), end="")
    return update

def main():
    if args.manual:
        changeColor(args.manual)
    else:
        print('Loop mode started, interval: {0}'.format(args.interval))
        if args.verbose and args.nighttime and args.time:
            print("Night time start: {0}, duration: {1}".format(args.nighttime[0], args.nighttime[1]))

        while True:
            if args.verbose:
                hours = time.localtime().tm_hour
                minutes = time.localtime().tm_min
                if hours < 10:
                    hours = "0" + str(hours)
                if minutes < 10:
                    minutes = "0" + str(minutes)
                print('[{0}:{1}] '.format(hours, minutes), end="")

            if args.random:
                randomColor()
            elif args.time:
                timeColor()
            elif args.incremental:
                incrementalColor(args.incremental)
            else:
                randomColor()
            sleepTimer = timeSync(args.interval)
            print()
            time.sleep(sleepTimer)

main()
