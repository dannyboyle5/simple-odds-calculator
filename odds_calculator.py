def at_least_once(): 
    p = float(input("Enter probability odds: ")) / 100
    n = int(input("Enter number of events: "))
    result_at_least_once = 1 - (1 - p) ** n
    result_at_least_once = result_at_least_once * 100
    print(f"Probability of atleast one success: {result_at_least_once:.3f}%")

def at_least_twice(): 
    p = float(input("Enter probability odds: ")) / 100
    n = int(input("Enter number of events: "))
    result_at_least_twice = 1 - (1 - p) ** n - (n * p * (1 - p) ** (n - 1))
    result_at_least_twice = result_at_least_twice * 100
    print(f"Probability of atleast two successes: {result_at_least_twice:.3f}%")
    
def probability_to_odds(): 
    n = float(input("input numerator: "))
    d = float(input("Enter demoninator: "))
    p = n / d
    resulting_odds = (p / (1 - p))
    print(f"Probability {p * 100:.3f}%")
    print(f"resulting odds: {resulting_odds:g}:1")

""" BINOMIAL FUNCTION"""
def factorial(x):
    result = 1
    for i in range (1, x + 1):
        result *= i
    return result

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def exactly_k():
    p = float(input("Enter probability odds: ")) / 100
    n = int(input("Enter number of events: "))
    k = int(input("Enter number of successes: "))
    result_of_exactly_k = combination(n, k) * p ** k * (1 - p) ** (n - k)
    result_of_exactly_k = result_of_exactly_k * 100
    print(f"Probablity of exactly {k} successes: {result_of_exactly_k:.3f}%")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Probability of at least once")
        print("2. Probability of at least twice")
        print("3. Convert fraction to odds")
        print("4. Probability of k successes")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            at_least_once()
        elif choice == "2":
            at_least_twice()
        elif choice == "3":
            probability_to_odds()
        elif choice == "4":
            exactly_k()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()