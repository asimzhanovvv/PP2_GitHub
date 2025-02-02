list_of_numbers = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"

def filter_prime(numbers_str):

    numbers = list(int(num) for num in list_of_numbers.split())
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    

    return list(filter(is_prime, numbers))

prime_numbers = filter_prime(list_of_numbers)
print(prime_numbers)