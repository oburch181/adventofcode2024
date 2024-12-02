import numpy as np


def safe_reports(filename):
    with open(filename) as f:
         lines = f.readlines()

    count = 0
    for line in lines:
        tmp = line.strip().split()
        tmp = np.array([int(item) for item in tmp])
        
        asc_flag = True
        desc_flag = True
        
        for i in range(1,len(tmp)):
            if tmp[i]> tmp[i-1]:
                desc_flag = False
            else:
                asc_flag = False

        diffs = np.abs(tmp[1:] - tmp[:-1])

        if np.max(diffs) <= 3 and np.min(diffs) > 0:
            diffs_flag = True
        else:
            diffs_flag = False

        if (asc_flag or desc_flag) and diffs_flag:
            count += 1

    
    return count        


if __name__=="__main__":
    num_safe = safe_reports("input_day2.txt")
    print(num_safe)