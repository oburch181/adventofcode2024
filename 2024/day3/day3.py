import re

def part1(input_string):
    x = re.findall("""mul\\(\\d{1,3},\\d{1,3}\\)""", input_string)
    sum = 0

    for i in x:
        num_list = i.strip("mul()").split(",")
        sum += int(num_list[0]) * int(num_list[1])

    return sum

def part2(input_string):
    input_string = input_string.replace('\n',"")
    cleaned_string = re.sub("""(don't\\(\\)).*?(do\\(\\))""", "", input_string)
    match_obj = re.search("""don't()""", cleaned_string)
    if match_obj:
        cleaned_string = cleaned_string[:match_obj.span()[0]]
    return part1(cleaned_string)





if __name__=="__main__":
    with open("./2024/day3/input_day3.txt") as f:
        corrupted_str = f.read()

    part1_sum = part1(corrupted_str)
    print(part1_sum)

    part2_sum = part2(corrupted_str)
    print(part2_sum)