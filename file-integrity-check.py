import os
import argparse
import glob
import csv
import datetime

from shared.common import *

print("\n***********************************************************************")
print(r""" ___       _                  _ _          ____ _               _    
|_ _|_ __ | |_ ___  __ _ _ __(_) |_ _   _ / ___| |__   ___  ___| | __
 | || '_ \| __/ _ \/ _` | '__| | __| | | | |   | '_ \ / _ \/ __| |/ /
 | || | | | ||  __/ (_| | |  | | |_| |_| | |___| | | |  __/ (__|   < 
|___|_| |_|\__\___|\__, |_|  |_|\__|\__, |\____|_| |_|\___|\___|_|\_\
                   |___/            |___/                            
""")
print("\n***********************************************************************")
print("\n*** Copyright of Andriej Sazanowicz, 2023                        ******")
print("\n*** https://www.techtalk.andriejsazanowicz.com                   ******")
print("\n***********************************************************************")

# Initialize parser
parser = argparse.ArgumentParser(
    prog='A file integrity checker',
    description='Check if file been changed againts MD5 and SHA256 hash stored in csv',
    epilog='Powered by CyberTechTalk https://github.com/cybertechtalk'
)


# Required arguments
parser.add_argument("-f", "--files", nargs='+', required=True, help="File PATH pattern. Ex. <dir>/**/*.txt, **/*file*.*")
parser.add_argument("-m", "--mode", choices=['r', 'w'], required=True, help="-r: read mode; -w: write mode")
parser.add_argument("-o", "--output", type=str, required=True, help="PATH to store hasges. Ex. db.csv")
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose true/false")

# Read arguments from command line
args = parser.parse_args()

files_on_disk = []
files_in_db = [] 

class File:
    def __init__(self, file_name, sum, datetime, login):
        self.file_name = file_name
        self.sum = sum
        self.datetime = datetime
        self.login = login

def printif(message, condition=args.verbose):
    if condition:
        print(message)

for arg in vars(args): 
    printif(f'{CBEIGE}{arg, getattr(args, arg)}{CEND}')
printif('-----------------------')


if args.files == []:
    print(f'{CRED}No files found in {args.files}{CEND}')
else:
    printif(f'{CBOLD}{CBEIGE}Files found:{CEND}')
    for f in args.files: printif(f'{CBEIGE}{f}{CEND}')
    printif('-----------------------')

#Creating integrity source
for f in args.files:
    sum = hexdigest_sha256(f, args.verbose)
    files_on_disk.append(
        File(f, 
            sum, 
            str(datetime.datetime.fromtimestamp(os.stat(f).st_mtime if os.stat(f).st_mtime else os.stat(f).st_ctime)), 
            os.stat(f).st_uid)
        )

def read_db():
    if not os.path.exists(args.output):
        print(f'{CRED}File does not exists: {args.output}{CEND}')
        update_db()
    else:
        with open(args.output, 'r') as db:
            files_in_db = list(csv.reader(db, delimiter=','))
        printif(f'{CBEIGE}{CBOLD}---- SELECT FROM {args.output} -----{CEND}')
        if args.verbose:
            for f in files_in_db:
                print(f'{CBEIGE}{f}{CEND}')
        printif(f'{CBEIGE}{CBOLD}------- SELECT END --------{CEND}')
        return files_in_db

def update_db():
    if os.path.exists(args.output):
        print(f'{CRED}Removing old: {args.output}{CEND}')
        os.remove(args.output)
    
    with open(args.output, 'w') as db:
        print(f'{CGREEN}Creating new {args.output}{CEND}')
        writer = csv.writer(db)
        for f in files_on_disk: 
            writer.writerow([f.file_name, f.sum, f.datetime, f.login])
        exit()

def print_file(f, msg, color):
    print(f'{color}{msg}: {f.file_name, f.sum, f.datetime, f.login}{CEND}')


match args.mode:
    case "r":
        files_in_db = list(map(lambda x: File(x[0], x[1], x[2], x[3]), read_db()))
    case "w":
        update_db()
    case _: 
        print(f'Unsupported mode {args.mode}')
        exit()


db_name_list = list(map(lambda x: x.file_name, files_in_db))
dsk_name_list = list(map(lambda x: x.file_name, files_on_disk))
for dsk in files_on_disk:
    if dsk.file_name not in db_name_list: print_file(dsk, 'NEW FILE', CGREEN)
for db in files_in_db:
    if db.file_name not in dsk_name_list: print_file(db, 'DELETED FILE', CRED)

for dsk in files_on_disk:
    if dsk.file_name in db_name_list and dsk.sum != list(filter(lambda x: x.file_name == dsk.file_name, files_in_db))[0].sum: 
        print_file(dsk, "MODIFIED", CYELLOW)
