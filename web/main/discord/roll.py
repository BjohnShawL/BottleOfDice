import re
from random import randint

pattern = re.compile(' (?![+-])')


def process_command(arg_string: str, is_sum: bool) -> list[str]:
    results = []
    arg_list = re.split(pattern, arg_string)
    for roll in arg_list:
        res = create_roll(roll, is_sum)
        results.append(res)
    return results


def apply_modifier(mod: str, res: list[int]) -> str:
    modified_rolls = []
    mod_sign, mod_num, *_ = re.split('([\d]+)', mod)
    for roll in res:
        if mod_sign == '+':
            modified = roll + int(mod_num)
            response = f"{modified} -> ({roll}{mod_sign}{mod_num})"
            modified_rolls.append(response)
        elif mod_sign == '-':
            modified = roll - int(mod_num)
            response = f"{modified} -> ({roll}{mod_sign}{mod_num})"
            modified_rolls.append(response)
    return " \n".join([str(v) for v in modified_rolls])


def create_roll(roll_args, is_sum):
    roll_results = []
    modifier = True
    try:
        roll_sections = roll_args.split(' ')
        if len(roll_sections) < 2:
            modifier = False
        dice = roll_sections[0]
        if modifier:
            modifier = "".join(roll_sections[1:])
        num, sides = [int(val) for val in re.split('[dD]', dice)]
        if num == '' or num == '0':
            num = 1
        if not isinstance(num, int):
            num = int(num)

        for _ in range(num):
            r = randint(1, sides)
            roll_results.append(r)

        if is_sum:
            roll_results = [sum(roll_results)]
        roll_results = apply_modifier(modifier, roll_results) if modifier else " \n".join(
            [str(v) for v in roll_results])

    except (AssertionError, ValueError):
        return "Bad form, old chap"
    return roll_results
