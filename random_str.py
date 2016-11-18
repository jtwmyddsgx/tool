# coding: utf-8
from random import Random

def random_str(random_length=16):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


if __name__ == "__main__":
    nums = input("请输入位数后回车:")
    lines = input("请输入行数后回车:")
    with open('random_str.txt', 'w') as rs:
        for i in range(int(lines)):
            rs.write(random_str(int(nums)) + '\n')
