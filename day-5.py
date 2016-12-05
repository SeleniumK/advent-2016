from hashlib import md5


def get_password_in_order(salt):
    password = []

    i = 0
    while len(password) < 8:
        h = md5(salt + str(i)).hexdigest()
        if h.startswith("00000"):
            password.append(h[5])
        i += 1
    return password


def get_password_positional(salt):
    password = ["_"] * 8
    i = 0
    n = 0
    while n < 8:
        h = md5(salt + str(i)).hexdigest()
        position = int(h[5], 16)
        val = h[6]
        if h.startswith("00000"):
            if position in range(8) and password[position] == "_":
                password[position] = val
                n += 1
                print("".join(password))
        i += 1
    return password



if __name__ == "__main__":
    salt = "ugkcyxxp"
    # part 1
    # print("".join(get_password_in_order(salt)))

    # part 2
    print("".join(get_password_positional(salt)))
