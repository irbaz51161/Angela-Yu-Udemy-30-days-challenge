def main():
    def prime_no(num):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            print(f"Yes {num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
        
    number = int(input("Enter the number: "))
    prime_no(num=number)

main()