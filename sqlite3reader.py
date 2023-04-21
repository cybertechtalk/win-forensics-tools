import os
import argparse
import sqlite3
import base64
import json

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'
CEND    = '\033[0m'
CBOLD   = '\033[1m'

print("\n****************************************************************")
print(r"""           _ _ _       _____                    _           
 ___  __ _| (_) |_ ___|___ / _ __ ___  __ _  __| | ___ _ __ 
/ __|/ _` | | | __/ _ \ |_ \| '__/ _ \/ _` |/ _` |/ _ \ '__|
\__ \ (_| | | | ||  __/___) | | |  __/ (_| | (_| |  __/ |   
|___/\__, |_|_|\__\___|____/|_|  \___|\__,_|\__,_|\___|_|   
        |_|                                                 """)
print("\n****************************************************************")
print("\n* Copyright of Andriej Sazanowicz, 2023                        *")
print("\n* https://www.techtalk.andriejsazanowicz.com                   *")
print("\n****************************************************************")

# Initialize parser
parser = argparse.ArgumentParser(
    prog='sqlite3reader',
    description='Reading sqlite db',
    epilog='Powered by CyberTechTalk https://github.com/cybertechtalk'
)
 
# Required arguments
parser.add_argument("-f", "--file", type=str, required=True, help="Path to db file")
parser.add_argument("-s", "--search", type=str, required=False, help="Search for table/view/column in database, match in name")
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose true/false")
 
# Read arguments from command line
args = parser.parse_args()

if not os.path.exists(args.file):
    print("File doesn't exists: % s" % args.file)
    exit()
if not args.file.endswith('.db'):
    print("Not *.db file: % s" % args.file)
    exit()

# Create a SQL connection to our SQLite database
con = sqlite3.connect(args.file)

# creating cursor
cur = con.cursor()

class Entity:
    def __init__(self, entity, table, column):
        self.entity = entity
        self.table = table
        self.column = column
data = []

def printif(message, condition=args.verbose):
    if condition:
        print(message)

def show_desc(dbname, entity):
# reading all entities names
    entity_list = [a[0] for a in cur.execute(f"SELECT name FROM {dbname} WHERE type = '{entity}'")]
    for etty in entity_list:
        printif(f'{CYELLOW}[**] {entity} | {etty} {CEND}')
        columns = cur.execute('SELECT * FROM '+ etty)
        for col in columns.description:
            printif(f'  {CBEIGE}[***] {etty} | {col[0]} {CEND}')
            data.append(Entity(entity, etty, col[0]))

def show_content(entity, column):
    values = cur.execute('SELECT ' + column + ' FROM '+ entity)
    for val in values:
        if val[0]:
            try:
                data = json.loads(val[0].decode())
                content = data[0]['content']
                print(f'    {data} {CBEIGE}|base64decode> {CBOLD}{CBLUE}{base64.b64decode(content).decode()} {CEND}')
            except (UnicodeDecodeError, AttributeError):
                print(f'    {val[0]} {CBEIGE}|base64decode> {CBOLD}{CBLUE}{base64.b64decode(val[0]).decode()} {CEND}')

printif(f'{CBOLD}{CGREEN}[*] Load db content ...{CEND}')
show_desc('sqlite_master', 'table')
show_desc('sqlite_master', 'view')
printif("\n")

search = args.search
if search:
    clipboard_payloads = []
    print(f'{CBOLD}{CGREEN}[*] Searching for "{search}" {CEND}')
    for rec in data:
        if search in rec.column.lower():
            clipboard_payloads.append(rec)
            print(f' {CGREEN} [**] {rec.entity} {rec.table}.{rec.column} {CEND}')
            show_content(rec.table, rec.column)
    
# Be sure to close the connection
con.close()