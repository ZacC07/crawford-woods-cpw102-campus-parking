PRICE_PER_HOUR_OF_PARKING_IN_CAMPUS_PARKING_LOT = 2.0
def calculate_estimated_parking_cost(hours_estimated_to_park_in_the_campus_parking_lot,price_per_hour_of_parking_in_campus_parking_lot):
    estimated_price_of_parking_in_campus_parking_lot = hours_estimated_to_park_in_the_campus_parking_lot * 2.00
    return estimated_price_of_parking_in_campus_parking_lot

def main():
    # Create a variable for parked hours
    # A variable is a named space in memory
    hours_estimated_to_park_in_the_campus_parking_lot = float(input("How many hours will you be parked?: "))
    estimated_price_of_parking_in_campus_parking_lot = calculate_estimated_parking_cost(hours_estimated_to_park_in_the_campus_parking_lot,PRICE_PER_HOUR_OF_PARKING_IN_CAMPUS_PARKING_LOT)
    print(f"price: ${estimated_price_of_parking_in_campus_parking_lot}")

# call me
main()