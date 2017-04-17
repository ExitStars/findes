#!/usr/bin/env python
#-*-coding:utf-8-*-
from argparse import ArgumentParser
from os import name, system, walk, path

bold, underline, endcolor = "\033[1m", "\033[4m", "\033[0m"
green, blue, yellow, red = "\033[92m", "\033[94m", "\033[93m", "\033[91m"

def logo():
    system("clear")
    print "--==["+bold+blue+"nickname"+endcolor+"] [ ExitStars"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/ExitStars"
    print "--==["+bold+green+"software"+endcolor+"] [ Findes / Searcher"
    print "-"*50

def scan(fwt, fdic, ftype):
    for root, dic, folds in walk(fdic, topdown=False):
        for fold in folds:
            foldName = path.basename(fold)
            foldPath = path.join(root, fold)
            if "p" in ftype:
                if fwt in foldPath:
                    print bold+yellow+"[p] "+endcolor+foldPath
            if "c" in ftype:
                try:
                    read = open(foldPath, "r").read()
                    if fwt in read:
                        print bold+yellow+"[f] "+endcolor+foldPath
                except Exception as e:
                    print bold+red+"[-] "+endcolor, e

def main():
    if name != "posix": print "Just Linux!", quit()
    parser = ArgumentParser(usage = bold+yellow+"Usage:\n\t"+green+"es@coderlab "+blue+"~ $"+endcolor+" findes -a 'aranacak kelime' -d 'dizin' -t 'tarama türü'")
    parser.add_argument("-a", type=str, help="Aranacak Kelime")
    parser.add_argument("-d", type=str, help="Aranacak Dizin")
    parser.add_argument("-t", type=str, help="Arama Türü")
    flags = parser.parse_args()

    logo()
    if flags.a == None or flags.d == None or flags.t == None: print parser.usage
    else:
        scan(flags.a, flags.d, flags.t)

if __name__ == '__main__':
    main()
