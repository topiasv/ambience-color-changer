#!/usr/bin/python
import time
import colorsys
import subprocess
import random
import sys, argparse

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--random', action='store_true', help='Change color randomly')
group.add_argument('-t', '--time', action='store_true', help='Change color based on time')
group.add_argument('-i', '--incremental', action='store_true', help='Loop through each color incrementally')
group.add_argument()
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('color', type=str, help='Set the ambience color manually')
args = parser.parse_args()

main(sys.argv[1:])

hrs = 0.0

def main():
    while True:


def

def randomColor():
    hue = random.randrange(0.0,1.0)
    changeColor(hue)

def timeColor():
    hrs = time.localtime().tm_hour + float(time.localtime().tm_min) / 60
    hue = hrs / 24
    changeColor(hue)

def incrementalColor(step):
    hue = (hue + step) % 1.0

while True:
    #print(hrs)
    #hrs = time.localtime().tm_hour + float(time.localtime().tm_min) / 60
    hrs = random.randrange(0,24) + (float(random.randrange(0,59)) / 60)
    hue = hrs / 24
    rgb1 = colorsys.hsv_to_rgb(hue,0.5,1)
    rgb2 = colorsys.hsv_to_rgb(hue,0.5,0.8)
    web1 = "" + format(int(rgb1[0]*255), '02x') + format(int(rgb1[1]*255), '02x') + format(int(rgb1[2]*255), '02x')
    web2 = "" + format(int(rgb2[0]*255), '02x') + format(int(rgb2[1]*255), '02x') + format(int(rgb2[2]*255), '02x')
    cmd1 = "dconf write /desktop/jolla/theme/color/highlight '#%s'" % web1
    cmd2 = "dconf write /desktop/jolla/theme/color/secondaryHighlight '#%s'" % web2
    #print(hrs,hue,rgb,web)
    subprocess.call(cmd1.split(), shell=False)
    subprocess.call(cmd2.split(), shell=False)
    #print(cmd1)
    print("colors changed %s" % hrs)
    time.sleep(60*15)
    #hrs = (hrs + 5.0 / 60) % 24

def changeColor(hue):
    rgb1 = colorsys.hsv_to_rgb(hue,0.5,1)
    rgb2 = colorsys.hsv_to_rgb(hue,0.5,0.8)
    web1 = "" + format(int(rgb1[0]*255), '02x') + format(int(rgb1[1]*255), '02x') + format(int(rgb1[2]*255), '02x')
    web2 = "" + format(int(rgb2[0]*255), '02x') + format(int(rgb2[1]*255), '02x') + format(int(rgb2[2]*255), '02x')
    cmd1 = "dconf write /desktop/jolla/theme/color/highlight '#%s'" % web1
    cmd2 = "dconf write /desktop/jolla/theme/color/secondaryHighlight '#%s'" % web2
    subprocess.call(cmd1.split(), shell=False)
    subprocess.call(cmd2.split(), shell=False)
    print("colors changed %s" % hrs)
