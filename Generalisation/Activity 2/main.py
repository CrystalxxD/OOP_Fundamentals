from fast_food import Cashier, DriveThruCashier, Cook, HeadCook, Cleaner

def main():
    # Create employees
    employees = [
        Cashier("Sarah Miller", "EMP001", 12.50, 8.0, 3),
        DriveThruCashier("Tom Wilson", "EMP002", 13.00, 6.0, 5, "DT-47"),
        Cook("Jamal Brown", "EMP003", 15.00, 8.0, "Grill"),
        HeadCook("Maria Garcia", "EMP004", 18.50, 10.0, "Fryer", "Hot Foods"),
        Cleaner("Alice Johnson", "EMP005", 11.50, 4.0, "Restrooms")
    ]

    # Test cashier
    print("\n=== Testing Cashier ===")
    cashier = employees[0]
    print(cashier.clock_in())
    print(cashier.process_order(8.99))
    print(cashier.process_order(12.49))
    print(cashier.clock_out())
    print(cashier.display_stats())
    print(f"Total pay: ${cashier.get_pay():.2f}")

    # Test drive-thru cashier
    print("\n=== Testing Drive-Thru Cashier ===")
    dt_cashier = employees[1]
    print(dt_cashier.clock_in())
    print(dt_cashier.take_drive_thru_order("blue sedan"))
    print(dt_cashier.process_order(15.99))
    print(dt_cashier.take_drive_thru_order("red truck"))
    print(dt_cashier.clock_out())
    print(dt_cashier.display_stats())

    # Test cook
    print("\n=== Testing Cook ===")
    cook = employees[2]
    print(cook.clock_in())
    print(cook.prepare_meal("Big Burger"))
    print(cook.prepare_meal("Chicken Sandwich"))
    print(cook.clock_out())
    print(cook.display_stats())

    # Test head cook
    print("\n=== Testing Head Cook ===")
    head_cook = employees[3]
    print(head_cook.clock_in())
    print(head_cook.add_staff(cook))  # Adding the regular cook as staff
    print(head_cook.prepare_meal("Fish Fillet"))
    print(head_cook.conduct_inspection())
    print(head_cook.clock_out())
    print(f"Staff supervised: {len(head_cook.staff_supervised)}")

    # Test cleaner
    print("\n=== Testing Cleaner ===")
    cleaner = employees[4]
    print(cleaner.clock_in())
    print(cleaner.clean_area("Men's restroom"))
    print(cleaner.restock_supplies("paper towels"))
    print(cleaner.clock_out())
    print(f"Areas cleaned: {cleaner.areas_cleaned}")

if __name__ == "__main__":
    main()