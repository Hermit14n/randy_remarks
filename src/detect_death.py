
def did_you_die_though(path, last_death_index):
    try:
        f = open(path, 'r', errors='ignore')
    except FileNotFoundError:
        print('No log file')
        return False, 0
    lines = f.readlines()
    lines = lines[last_death_index+1:]
    for i, line in enumerate(lines):
        if ' killed SkinThatSmokeWagon' in line:
            return True, i+last_death_index+1
    return False, i+last_death_index


