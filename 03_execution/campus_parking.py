PRICE_PER_HOUR = 2.0
def calculate_estimated_parking_cost(hours_estimated):
    estimated_price = hours_estimated * PRICE_PER_HOUR
    return estimated_price

def main():
    # a variable for parked hours
    hours_estimated = input("How many hours will you be parked?: ")
    while (not hours_estimated.isnumeric()):
        print(f"[{hours_estimated}] is not a valid input")
        hours_estimated = input("Enter a valid input\nHow many hours will you be parked?: ")
    # convert hours estimated to float
    hours_estimated = float(hours_estimated)
    estimated_price = calculate_estimated_parking_cost(hours_estimated)
    # print the price nicely
    print(f"price: ${estimated_price}")

# call me
main()