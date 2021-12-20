# find number by half-division method
def random_predict(number: int, a: int = 0, b: int = 100):
    count=0
    median = (a + b)//2

    if number == median or number == a or number == b:
        count += 1
    elif number > median:
        count += 1 + random_predict(number,  median, b)
    elif number < median:
        count += 1 + random_predict(number,  a, median)
    return count


