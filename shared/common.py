import hashlib

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

def insensitive_for_glob(string_file):
    return ''.join(['[' + c.lower() + c.upper() + ']' if c.isalpha() else c for c in string_file])

def hexdigest_sha256(file, condition=True):
    with open(file,"rb") as f:
        bytes = f.read() 
        readable_hash = hashlib.sha256(bytes).hexdigest()
        if condition: print(f'{file}|sha256> {CBLUE}{readable_hash}{CEND}')
        return readable_hash
    
def hexdigest_md5(file, condition=True):
    with open(file,"rb") as f:
        bytes = f.read() 
        readable_hash = hashlib.md5(bytes).hexdigest()
        if condition: print(f'{file}|md5> {CBLUE}{readable_hash}{CEND}')
        return readable_hash