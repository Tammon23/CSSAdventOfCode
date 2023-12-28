import hashlib

# file = "example_input.txt"
file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        secret = f.read().strip()

    i = 0
    while True:
        res = hashlib.md5(f"{secret}{i}".encode('utf-8')).hexdigest()
        if res.startswith("000000"):
            print(i)
            break

        i += 1

