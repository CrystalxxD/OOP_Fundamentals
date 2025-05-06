class Subject:
    def __init__(self, name, year_level, class_code, num_students):
        self.name = name
        self.year_level = year_level
        self.class_code = class_code
        self.num_students = num_students
    
    def display(self):
        print(f"Subject: {self.name}")
        print(f"Year Level: {self.year_level}")
        print(f"Class Code: {self.class_code}")
        print(f"Number of Students: {self.num_students}")
        print("-" * 30)
    
    @staticmethod
    def display_all(subjects):
        if not subjects:
            print("No subjects in the list.")
            return
        
        for subject in subjects:
            subject.display()