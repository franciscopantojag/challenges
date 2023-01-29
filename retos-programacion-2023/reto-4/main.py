def is_even(num: 'int'):
    return num % 2 == 0


def is_fib(num: 'int'):
    fib_seq = [0, 1]

    while (fib_seq[-1] < num):
        next_fib = fib_seq[-2] + fib_seq[-1]
        fib_seq.append(next_fib)

    return num in fib_seq


def is_prime(num: 'int'):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def build_num_info(num: 'int'):
    prime_info = 'es primo' if is_prime(num) else 'no es primo'
    fib_info = 'es fibonacci' if is_fib(num) else 'no es fibonacci'
    even_info = 'es par' if is_even(num) else 'es impar'
    return f'{num} {prime_info}, {fib_info} y {even_info}'


TESTING_NUM = 2


def main():
    print(build_num_info(TESTING_NUM))


if __name__ == '__main__':
    main()
