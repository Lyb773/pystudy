def zhaoqian(money):
    loop=True
    # 面值列表 单位：元
    cate=[
          500,
          100,
          50,
          10,
          5,
          1,
    ]

    currency = int(money)
    while loop:
        if currency <= 0:
            loop=False
        else:
            for spec in range(6):
                amount = currency//cate[spec]
                currency = currency - amount*cate[spec]
                if not amount < 1:
                    print(str(cate[spec]) + ',', str(amount) + ';',end='')

def main():
    ask=int(input(">"))
    zhaoqian(ask)

if __name__ == '__main__':
    main()
