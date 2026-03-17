# Currency Converter Program
#Keeping history
history = []
# Exchange rates (example values)
rates = {
    "USD": {"USD": 1, "EUR": 0.92, "CAD": 1.25},
    "EUR": {"USD": 1.09, "EUR": 1, "CAD": 1.36},
    "CAD": {"USD": 0.80, "EUR": 0.74, "CAD": 1}
}

# Take input from user
while True:
    paisa = float(input("Enter the amount: "))
    source = input("Source currency (USD/EUR/CAD): ").upper()
    target = input("Target currency (USD/EUR/CAD): ").upper()

    # Conversion
    if source in rates and target in rates[source]:
        converted = paisa * rates[source][target]
        print(f"{paisa} {source} is equal to {converted:.2f} {target}")

        history.append(converted)
    else:
        print("Invalid currency entered.")

    choice = input("Do you want to convert again? (yes/no): ").lower()
    if choice != "yes":
        break


print("\nConversion History:")
for item in history:
    print(item)    