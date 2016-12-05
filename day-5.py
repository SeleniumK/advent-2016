from hashlib import md5


def get_password(salt):
    password = []

    i = 0
    while len(password) < 8:
        h = md5(salt + str(i)).hexdigest()
        if h.startswith("00000"):
            password.append(h[5])
        i += 1
    return password


if __name__ == "__main__":
    salt = "ugkcyxxp"
    print("".join(get_password(salt)))
