# Windows Forensics Tools

Collection of windows forensics tools

## sqlite3 cache db forensics with python3

````
****************************************************************
           _ _ _       _____                    _           
 ___  __ _| (_) |_ ___|___ / _ __ ___  __ _  __| | ___ _ __ 
/ __|/ _` | | | __/ _ \ |_ \| '__/ _ \/ _` |/ _` |/ _ \ '__|
\__ \ (_| | | | ||  __/___) | | |  __/ (_| | (_| |  __/ |   
|___/\__, |_|_|\__\___|____/|_|  \___|\__,_|\__,_|\___|_|   
        |_|                                                 

****************************************************************
````
The tool leverages sqlite3 for searching and reading *.db

### How to use

1. Pull the repo
2. Locate %AppData%\Local\ConnectedDevicesPlatform\<UserProfile>\ActivitiesCache.db
3. Run sqlite3reader.py -h
4. Use SCAM MODE for looking for dbs. 
5. Use -f and/or --search to search for specific columns

    ````
    usage: sqlite3reader [-h] -f FILE [-s SEARCH] [-v]

    Reading sqlite db

    options:
        -h, --help            show this help message and exit
        -f FILE, --file FILE  PATH to db file. Use --dir to SCAN MODE for *.db
        --dir DIR             SCAN MODE for *.db file, ex. %APPDATA%. Default location: C:\Users
        -s SEARCH, --search SEARCH
                                Looking for db/table/view/column, match in name. Default: *cache*. If SCAN MODE searches for db name
        -d, --decode          Decode true/false
        -v, --verbose         Verbose true/false
 
    ````   
Powered by CyberTechTalk https://github.com/cybertechtalk
Copyright of Andriej Sazanowicz, 2023
