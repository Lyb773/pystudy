def verify_hkid(idstr):
    #verift HKID number
    if len(idstr) != 8:
        return False
    #check first letter
    code1 = ord(idstr[0])
    if (code1 < 65 or code1 > 90):
        return False
    #check the remain letter(exclude the num in ()) , must be int
    for i in range(1,7):
        code2 = ord(idstr[i])
        if (code2 < 48 or code2 > 57):
            return False
    #transform A-Z to 1-26
    cmap = []
    for i in range(1,27):
        cmap.append(i)
    num1 = cmap[code1 - 65]
    #first digit
    fstchecksum = num1 * 8
    #2nd~7th digit
    weight = [7, 6, 5, 4, 3, 2]
    partchecksum = 0
    for i in range(1,7):
        partchecksum += weight[i-1] * int(idstr[i])
    #checksum
    checksum = fstchecksum + partchecksum
    #check digit = 8th digit
    chdigit = 11 - (checksum % 11)
    lastdigit = idstr[7]
    if lastdigit == str(chdigit):
        return True
    elif str(chdigit) == '10' and lastdigit == 'A':
        return True
    else:
        return False

def main():
    str = input("Input HKID card number(include number in () ): ")
    print(verify_hkid(str))

if __name__ == "__main__":
    main()
