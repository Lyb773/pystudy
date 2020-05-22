#print the checksum only
def cksum(idstr):
    code1 = ord(idstr[0])
    cmap = (10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33)
    num1 = cmap[code1 - 65]
    newid = str(num1) + idstr[1:]
    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    out1 = map(lambda pair:pair[1] * int(pair[0]), zip(newid, weight))
    print(tuple(out1))
    checksum = sum(out1)
    print("checksum=%d" % checksum)

def main():
    id1 = "A123456789"
    cksum(id1)

if __name__ == '__main__':
    main()
