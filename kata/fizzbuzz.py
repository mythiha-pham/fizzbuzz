def fizzbuzz_stage1(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz_stage2(n):
    fizz_count = 0
    buzz_count = 0

    if n % 3 == 0:
        fizz_count += 1
    if n % 5 == 0:
        buzz_count += 1

    fizz_count += str(n).count('3')
    buzz_count += str(n).count('5')

    result = "Fizz" * fizz_count + "Buzz" * buzz_count
    return result if result else str(n)

def fizzbuzz(n, stage=1):
    if stage == 1:
        return fizzbuzz_stage1(n)
    elif stage == 2:
        return fizzbuzz_stage2(n)
    else:
        raise ValueError("Invalid stage. Choose either 1 or 2.")