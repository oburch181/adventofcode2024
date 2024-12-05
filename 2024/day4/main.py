import re
import numpy as np

def get_diags(array):
    diags = [array[::1,:].diagonal(i) for i in range(-array.shape[0]+1, array.shape[1])]
    diags_list = ["".join(n.tolist()) for n in diags]
    return diags_list


def find_xmas_part1(input_list):
    out_list = []
    for i in input_list:
        tmp_list = list(i)
        if '\n' in tmp_list[-1]:
            tmp_list.pop(-1)
        out_list.append(tmp_list)

    np_list = np.array(out_list)
    master_list = []

    for i in range(4):
        master_list = master_list + ["".join(n.tolist()) for n in np.rot90(np_list, i)]
        master_list = master_list + get_diags(np.rot90(np_list, i))
    
    text_string = (" ").join(master_list)
    all_xmas = re.findall("XMAS", text_string)
    return len(all_xmas)

def find_xmas_part2(input_list):
    out_list = []
    for i in input_list:
        tmp_list = list(i)
        if '\n' in tmp_list[-1]:
            tmp_list.pop(-1)
        out_list.append(tmp_list)

    out_array = np.array(out_list)
    count = 0
    for j in range(out_array.shape[1]-2):
        for i in range(out_array.shape[0]-2):
            conv = out_array[j:j+3,i:i+3]
            mas_count = 0
            for r in range(4):
                if np.array_equal(np.linalg.diagonal(np.rot90(conv,r)), np.array(['M','A','S'])):
                    mas_count+=1
            if mas_count==2:
                count+=1
    return count
            

if __name__=="__main__":
    with open("./2024/day4/input_day4.txt") as f:
    #with open("./2024/day4/test.txt") as f:
        text = f.readlines()

    part1_total = find_xmas_part1(text)
    print(part1_total)

    part2_total = find_xmas_part2(text)
    print(part2_total)