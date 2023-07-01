import shutil
import numpy as np

def clean_up_and_exit(path):
    original = path
    tag = np.random.random()
    tag = str(tag).split('.')[1]
    target = 'C:/Users/paulc/Documents/randy_remarks_logs/' + 'console_log_' + tag

    shutil.move(original, target)