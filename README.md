# ActivitiesCache.db Python3 Reader

The tool leverages sqlite3 for reading ActivitiesCache.db

## How to use

1. Pull the repo
2. Locate %AppData%\Local\ConnectedDevicesPlatform\\<UserProfile>\\ActivitiesCache.db
3. Run sqlite3reader.py -h

    ````
    usage: sqlite3reader [-h] -f FILE [-s SEARCH] [-v]

    Reading sqlite db

    options:
        -h, --help            show this help message and exit
        -f FILE, --file FILE  Path to db file
        -s SEARCH, --search SEARCH
                                Search for table/view/column in database, match in name
        -d, --decode          Decode true/false
        -v, --verbose         Verbose true/false
    ````
    Powered by CyberTechTalk https://github.com/cybertechtalk