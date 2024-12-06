import numpy as np

def part1(rules, updates):
    mid_sum = 0

    for update in updates:
        good_update = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    good_update = False
                    break
        if good_update:
            mid_sum+=update[int(len(update)/2)]
    return mid_sum

def part2(rules,updates):
    rules = np.array(rules)
    mid_sum = 0
    for update in updates:
        mask = [True if i[0] in update and i[1] in update else False for i in rules]
        good_update = check_follows_rules(rules[mask], update)
        if not good_update:
            update = fixupdate(rules[mask], update)
        if not good_update:
            mid_sum+=update[int(len(update)/2)]
    return mid_sum


def check_follows_rules(rules, update):
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def fixupdate(rules, update):
    get_outta_here=False
    while get_outta_here==False:
        for rule in rules:
            if update.index(rule[0]) > update.index(rule[1]):
                update.remove(rule[1])
                update.insert(update.index(rule[0])+1, rule[1])
            good = check_follows_rules(rules, update)
            if good:
                get_outta_here = True
                break
    return update



if __name__=="__main__":
    #with open("./2024/day5/test.txt") as f:
    with open("./2024/day5/input.txt") as f:
        pages = f.read()

    rules = []
    updates = []

    [rules.append([int(y) for y in x.split("|")]) if "|" in x else updates.append([int(y) for y in x.split(",")]) for x in pages.split()]

    correct_mids = part1(rules, updates)
    print(correct_mids)

    correct_mids = part2(rules, updates)
    print(correct_mids)
    