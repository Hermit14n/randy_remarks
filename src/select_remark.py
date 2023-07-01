import os
import numpy as np
def remark()->str:

    path = "../remarks/"
    dir_list = os.listdir(path)
    if len(dir_list) > 0:
        index = np.random.randint(0, high=len(dir_list))
    else:
        raise ValueError("Your remarks directory is empty, ensure remarks directory has mp3s, dammit")
    return path + dir_list[index]
