# ActivitiesCache.db Python3 Reader

The tool leverages sqlite3 for reading ActivitiesCache.db

## How to use

1. Pull the repo
2. Locate %AppData%\Local\ConnectedDevicesPlatform\<UserProfile>\ActivitiesCache.db
3. Run sqlite3reader.py -h

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