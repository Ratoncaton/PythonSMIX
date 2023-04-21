
def user_inp():
    return int(input("Introdueix un nombre:\n"))

def multi_looper(user, a):
    print("{} * {} = {}".format(a, user, a*user))


def main():
    user = user_inp()
    for a in range(1, 11):
        multi_looper(user, a)

if __name__ == "__main__":
    main()