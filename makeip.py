# coding:utf-8
import random

times = 1  # 每个ip段生成ip的个数
ipd_dict = {}  # 存放ip段的字典
ip_result = []  # 最后得到的结果
ip_list = []

# 先下载所需要的ip段 存放于当前路径下的ip_resource.txt 编码为utf-8
with open("ip_resource.txt", "r", encoding="utf-8") as iptext:
    for i in iptext.readlines(): # 去除移动联通 运营商的ip
        if "移动" in i or "联通" in i:
            pass
        else:
            x = i.split()
            if x[0] == x[1]:
                continue
            ip_list.append(i)
for i in ip_list:
    x = i.split()
    ipd_dict[x[0]] = x[1]
for k, v in ipd_dict.items():
    k_split = k.split(".")
    v_split = v.split(".")
    ip12 = k_split[0] + "." + k_split[1] + "."
    ip3 = int(k_split[2])
    ip3_limit = int(v_split[2])
    ip4 = int(k_split[3])
    ip4_limit = int(v_split[3])
    if ip3_limit == 255:
        ip3_limit -= 2
    if ip3_limit <= 2:
        ip3_limit += 1
    if ip4_limit == 255:
        ip4_limit -= 2
    if ip4_limit <= 2:
        ip4_limit += 1

    if (ip3 > ip3_limit):
        ip1 = k_split[0] + "."
        ip2 = int(k_split[1])
        ip2_limit = int(v_split[1])
        for i in range(times):
            ip2_random = random.randint(ip2, ip2_limit)
            ip3_random = random.randint(0, ip3_limit)
            ip4_random = random.randint(2, ip4_limit)
            ip_get = ip1 + str(ip2_random) + "." + str(ip3_random) + "." + str(ip4_random)
            ip_result.append(ip_get)
    else:
        for i in range(times):
            ip3_random = random.randint(ip3, ip3_limit)
            ip4_random = random.randint(2, ip4_limit)
            ip_get = ip12 + str(ip3_random) + "." + str(ip4_random)
            ip_result.append(ip_get)

ip_result = list(set(ip_result))
random.shuffle(ip_result)  # 打乱顺序
with open("ip_result.txt", "w", encoding="utf-8") as result:
    for i in ip_result:
        result.write(i + "\n")
print("共生成" + str(len(ip_result)) + "个ip！")



