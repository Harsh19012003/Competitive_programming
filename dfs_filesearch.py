# listdir(dir) -> list of items(files or folders or both) present in dir

def file_search(name, dir):
    items = listdir(dir)

    
    for item in items:
        if item.type() == file:
            if item == name:
                return item
    
        return file_search(name, item)

    
file_search(name="zeus", dir="something")