def pingpong_r(n, r=1, i=1, sign=1):
    if n == r:
        return i
    else:
        return pingpong_r(n, r + 1, i + sign, switch_sign(r + 1))


def switch_sign(r: int):
    if not r % 7:
        return -1
    elif r > 10:
        while r % 10 != 7 and int(r / 10) != 7:
            r = int(r / 10)
            if r == 0:
                return 1
        return -1
    return 1

if __name__ == '__main__':
    print(pingpong_r(8))
    print(pingpong_r(22))
    print(pingpong_r(68))
    print(pingpong_r(100))
