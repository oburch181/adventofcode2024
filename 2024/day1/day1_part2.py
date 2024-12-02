import numpy as np

def calc_list_sim(list1, list2):
    sum = 0
    for i in list1:
        sum+=list(list2).count(i) * i

    return sum

if __name__=="__main__":
    #Test case
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4 ,3 ,5 ,3 ,9 ,3]

    oot = calc_list_sim(list1, list2)
    print(oot)

    #process my input HUGE PAIN
    with open("input_day.txt") as f:
        s = f.read()

    s_list = s.split()
    s_list = [int(item) for item in s_list]
    evens = np.array(s_list[::2])
    odds = np.array(s_list[1::2])
    
    ans = calc_list_sim(evens, odds)
    print(ans)