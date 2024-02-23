# get_files(d)
# get_dir(d)

def finding(name, d):
    files = get_files(d)

    for file in files:
        if file == name:
            return True
        
    directories = get_dir(d)

    for dir in directories:
        if(finding(name, dir)):
            return True
        
    return False