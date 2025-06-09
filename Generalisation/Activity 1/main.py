from school_system import Teacher, Student, Parent

def main():
    # Create some students
    student1 = Student("Alice Johnson", "2010-05-15", "S1001", 8)
    student1.enroll_course("Mathematics")
    student1.enroll_course("Science")
    
    student2 = Student("Bob Smith", "2011-03-22", "S1002", 7)
    student2.enroll_course("English")
    student2.enroll_course("History")
    
    # Create a teacher
    teacher1 = Teacher("Mr. Thompson", "1980-11-10", "Mathematics", "T2001")
    teacher1.add_class("8th Grade Math")
    teacher1.add_class("9th Grade Algebra")
    
    # Create parents
    parent1 = Parent("Mrs. Johnson", "1985-07-30", [student1])
    parent2 = Parent("Mr. Smith", "1982-09-14", [student2])
    
    # Demonstrate functionality
    print("=== Teacher Details ===")
    teacher1.display_details()
    
    print("\n=== Student 1 Details ===")
    student1.display_details()
    
    print("\n=== Student 2 Details ===")
    student2.display_details()
    
    print("\n=== Parent 1 Details ===")
    parent1.display_details()
    
    print("\n=== Parent 2 Details ===")
    parent2.display_details()
    
    # Add another child to parent2
    student3 = Student("Emily Smith", "2009-08-05", "S1003", 9)
    parent2.add_child(student3)
    
    print("\n=== Updated Parent 2 Details ===")
    parent2.display_details()

if __name__ == "__main__":
    main()