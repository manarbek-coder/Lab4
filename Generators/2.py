def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    n = int(input("Enter a number (n): "))
    even_numbers = generate_even_numbers(n)
    result = ','.join(map(str, even_numbers))
    print("Even numbers between 0 and", n, ":", result)

if __name__ == "__main__":
    main()
