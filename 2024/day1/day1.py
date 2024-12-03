import numpy as np

def calc_list_dist(list1, list2):
    list_diff = np.abs(np.sort(np.array(list1)) - np.sort(np.array(list2)))
    return np.sum(list_diff)

if __name__=="__main__":
    #Test case
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4 ,3 ,5 ,3 ,9 ,3]

    oot = calc_list_dist(list1, list2)
    print(oot)

    #process my input HUGE PAIN
    with open("./2024/day1/input_day.txt") as f:
        s = f.read()

    s_list = s.split()
    s_list = [int(item) for item in s_list]
    evens = np.array(s_list[::2])
    odds = np.array(s_list[1::2])
    
    ans = calc_list_dist(evens, odds)
    print(ans)