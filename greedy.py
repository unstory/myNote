#coding=utf8

'贪心算法求最大收入'

class MoonCake(object):
    def __init__(self, store, total):
        self.store = store  # 存量
        self.total = total  # 总价
        self.price = self.total / self.store  # 单价

def main():
    mooncake_1 = MoonCake(15, 75)
    mooncake_2 = MoonCake(25, 50)
    mooncake_3 = MoonCake(15, 60)
    demand = 25  # 需求25，求最大收入


    mooncake_list = [mooncake_1, mooncake_2, mooncake_3]
    mooncake_list = sorted(mooncake_list, key=lambda x: x.price, reverse=True)
    income = 0
    for moon_cake in mooncake_list:
        if moon_cake.store > demand:
            income += demand * moon_cake.price
            moon_cake.store = moon_cake.store - demand
            demand = 0
            break
        else:
            income += moon_cake.total
            demand -= moon_cake.store
    print("max income is:", income)

if __name__ == "__main__":
    main()
