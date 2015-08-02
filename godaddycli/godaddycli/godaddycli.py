#!/usr/bin/env python
# Copyright 2015 by Wojciech A. Koszek <wojciech@koszek.com>
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
import getpass
from pygodaddy import GoDaddyClient

g_dns_record_types = [ "A", "CNAME", "MX", "TXT", "SRV", "NS", "AAAA" ]
g_debug = False

def dbg(s):
    if g_debug != True:
        return
    print "# debug: " + str(s)

def parse_args(args):
    parser = argparse.ArgumentParser(description="GoDaddy.com CLI")
    parser.add_argument("--user")
    parser.add_argument("--password")
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args(args)
    return args

def godaddycli(username, password):
    client = GoDaddyClient()

    c = client.login(username, password)
    if not c:
            print "couldn't login"
            sys.exit(1)

    for domain_name in client.find_domains():
        for record_type in g_dns_record_types:
            domain_data_all = client.find_dns_records(domain_name, record_type)
            for domain_data in domain_data_all:
                print domain_name, record_type, domain_data.hostname, domain_data.value

def doit(cfg):
    global g_debug

    g_debug = cfg.debug
    home_dir = os.environ["HOME"]

    user = password = cfg_data = None
    cfg_filename = home_dir + "/.godaddyclirc"
    if os.path.isfile(cfg_filename):
        with open(cfg_filename, "r") as f:
            cfg_data = json.load(f)
        f.close()

        valid_fields_count = 0
        if "user" in cfg_data.keys():
            user = cfg_data["user"]
        if "password" in cfg_data.keys():
            password = cfg_data["password"]

    maybe_save = False

    if cfg.user:
        user = cfg.user
    if user is None:
        sys.stdout.write("Enter GoDaddy user    : ")
        user = sys.stdin.readline().strip("\n")
        maybe_save = True

    if cfg.password:
        password = cfg.password
    if password is None:
        password = getpass.getpass("Enter GoDaddy password: ")
        maybe_save = True

    dbg("user: " + user)
    dbg("pass: " + password)
    dbg("home: " + home_dir)

    will_save = False
    if maybe_save:
        sys.stdout.write("Do you want to save your password in " +
            cfg_filename + "? Enter 'yes' or 'no': ")
        while True:
            yes_or_no = sys.stdin.readline().strip("\n")
            if yes_or_no != "yes" and yes_or_no != "no":
                print "Only 'yes' or 'no' supported"
                continue
            if yes_or_no == "yes":
                will_save = True
            break

    if will_save:
        data_to_save = {
            "user"      : user,
            "password"  : password
        };
        with open(cfg_filename, "w") as f:
            js = json.dump(data_to_save, f)
        f.close()

    godaddycli(user, password)

def main():
    cfg = parse_args(sys.argv[1:])
    doit(cfg)

if __name__ == "__main__":
    sys.exit(main())