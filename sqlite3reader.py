import os
import argparse
import sqlite3

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
parser.add_argument("-f", "--file", type=str, required=True, help = "Path to db file")
 
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

# reading all table names
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# here is you table list
print(table_list)

# Be sure to close the connection
con.close()