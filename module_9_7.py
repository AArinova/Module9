
def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        """алгоритм проверки числа на простоту"""
        k = 0
        for i in range(2, number // 2 + 1):
            if (number % i == 0):
                k = k + 1
        if (k <= 0):
            print(f"Число {number} простое.")
        else:
            print(f"Число {number} составное.")
    return wrapper

@is_prime
def sum_three(s1: int, s2: int, s3: int):
    return s1 + s2 + s3


result = sum_three(2, 3, 6)
