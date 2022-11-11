import time


def abs_value_0(x):
    if x < 0:
        return -x
    return x


if __name__ == '__main__':
    number = int(input("enter a number:"))
    print("Thinking...")
    time.sleep(10.)
    result = abs_value_0(number)
    print("Absolute value is", result)
