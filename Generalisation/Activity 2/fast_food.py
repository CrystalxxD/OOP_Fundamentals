class Employee:
    """Base class representing an employee in a fast food restaurant."""
    
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.clocked_in = False
        self.hours_worked = 0.0
    
    def clock_in(self):
        if not self.clocked_in:
            self.clocked_in = True
            return f"{self.name} has clocked in for their shift."
        return f"{self.name} is already clocked in!"
    
    def clock_out(self):
        if self.clocked_in:
            self.clocked_in = False
            self.hours_worked += self.shift_hours
            return f"{self.name} has clocked out after {self.shift_hours} hours."
        return f"{self.name} wasn't clocked in!"
    
    def get_pay(self):
        return self.hours_worked * self.hourly_wage
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (ID: {self.employee_id})"


class Cashier(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, register_number):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.register_number = register_number
        self.transactions_processed = 0
    
    def process_order(self, amount):
        self.transactions_processed += 1
        return f"Order #{self.transactions_processed} processed for ${amount:.2f} at register {self.register_number}"
    
    def display_stats(self):
        return f"Transactions processed today: {self.transactions_processed}"


class DriveThruCashier(Cashier):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, register_number, headset_id):
        super().__init__(name, employee_id, hourly_wage, shift_hours, register_number)
        self.headset_id = headset_id
        self.cars_served = 0
    
    def take_drive_thru_order(self, car_description):
        self.cars_served += 1
        return f"Taking order from {car_description} via headset {self.headset_id}"
    
    def display_stats(self):
        base_stats = super().display_stats()
        return f"{base_stats}\nCars served in drive-thru: {self.cars_served}"


class Cook(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, station):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.station = station
        self.meals_prepared = 0
    
    def prepare_meal(self, meal_name):
        self.meals_prepared += 1
        return f"Preparing {meal_name} at {self.station} station"
    
    def display_stats(self):
        return f"Meals prepared today: {self.meals_prepared} at {self.station} station"


class HeadCook(Cook):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, station, kitchen_section):
        super().__init__(name, employee_id, hourly_wage, shift_hours, station)
        self.kitchen_section = kitchen_section
        self.staff_supervised = []
    
    def add_staff(self, employee):
        if isinstance(employee, Cook):
            self.staff_supervised.append(employee)
            return f"Added {employee.name} to {self.kitchen_section} section"
        return "Can only supervise other cooks"
    
    def conduct_inspection(self):
        return f"Conducting inspection of {self.kitchen_section} section"


class Cleaner(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, cleaning_specialty):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.cleaning_specialty = cleaning_specialty
        self.areas_cleaned = 0
    
    def clean_area(self, area_name):
        self.areas_cleaned += 1
        return f"Cleaning {area_name} (specialty: {self.cleaning_specialty})"
    
    def restock_supplies(self, supply_type):
        return f"Restocking {supply_type} supplies"