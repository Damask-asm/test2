def add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return None

def multiply(a, b):
    try:
        return int(a) * int(b)
    except ValueError:
        return None

if __name__ == "__main__":
    print("Hello, World!")


