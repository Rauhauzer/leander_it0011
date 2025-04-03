import csv

def load_exchange_rates(filename):
     exchange_rates = {}
     try:
         with open(filename, mode='r', newline='', encoding='utf-8') as file:
             reader = csv.reader(file)
             next(reader)
             for row in reader:
                 if len(row) == 3:
                     code, name, rate = row
                     exchange_rates[code] = float(rate)
     except FileNotFoundError:
         print("Error: File not found.")
     except Exception as e:
         print(f"An error occurred: {e}")
     return exchange_rates

def convert_currency(amount, currency, rates):
     if currency in rates:
         return amount * rates[currency]
     else:
         print("Error: Currency not found.")
         return None

def main():
     filename = '/LabAct4B/currency.csv'
     rates = load_exchange_rates(filename)

     if not rates:
         print("No exchange rates loaded. Exiting.")
         return

     try:
         amount = float(input("How much dollar do you have? "))
         currency = input("What currency do you want to have? ").upper()
         converted_amount = convert_currency(amount, currency, rates)

         if converted_amount is not None:
             print(f"\nDollar: {amount} USD")
             print(f"{currency}: {converted_amount}")
     except ValueError:
         print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
     main()