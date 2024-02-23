def generate_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    n = int(input("Enter a number (n): "))
    divisible_numbers = generate_divisible_by_3_and_4(n)
    print("Numbers divisible by 3 and 4 between 0 and", n, ":")
    for num in divisible_numbers:
        print(num)

if __name__ == "__main__":
    main()
