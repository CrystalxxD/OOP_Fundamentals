class Person:
    """Base class representing a person in the school system."""
    
    def __init__(self, name, dob):
        """
        Initialize a Person with name and date of birth.
        
        Args:
            name (str): Full name of the person
            dob (str): Date of birth in 'YYYY-MM-DD' format
        """
        self.name = name
        self.dob = dob
    
    def display_details(self):
        """Display basic personal information."""
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
    
    def __str__(self):
        return f"Person: {self.name}"


class Teacher(Person):
    """Class representing a teacher, inherits from Person."""
    
    def __init__(self, name, dob, subject, employee_id):
        """
        Initialize a Teacher with additional attributes.
        
        Args:
            subject (str): Subject taught by the teacher
            employee_id (str): Unique identifier for the teacher
        """
        super().__init__(name, dob)
        self.subject = subject
        self.employee_id = employee_id
        self.classes = []  # List of classes taught
    
    def add_class(self, class_name):
        """Add a class that the teacher teaches."""
        self.classes.append(class_name)
    
    def display_details(self):
        """Display teacher-specific information."""
        super().display_details()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")
        if self.classes:
            print("Classes taught:", ", ".join(self.classes))
        else:
            print("Currently not assigned to any classes")
    
    def __str__(self):
        return f"Teacher: {self.name} (ID: {self.employee_id})"


class Student(Person):
    """Class representing a student, inherits from Person."""
    
    def __init__(self, name, dob, student_id, grade_level):
        """
        Initialize a Student with additional attributes.
        
        Args:
            student_id (str): Unique identifier for the student
            grade_level (int): Current grade level
        """
        super().__init__(name, dob)
        self.student_id = student_id
        self.grade_level = grade_level
        self.enrolled_courses = []
    
    def enroll_course(self, course_name):
        """Enroll the student in a new course."""
        self.enrolled_courses.append(course_name)
    
    def display_details(self):
        """Display student-specific information."""
        super().display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Grade Level: {self.grade_level}")
        if self.enrolled_courses:
            print("Enrolled Courses:", ", ".join(self.enrolled_courses))
        else:
            print("Not enrolled in any courses")
    
    def __str__(self):
        return f"Student: {self.name} (Grade {self.grade_level})"


class Parent(Person):
    """Class representing a parent, inherits from Person."""
    
    def __init__(self, name, dob, children=None):
        """
        Initialize a Parent with children information.
        
        Args:
            children (list): List of Student objects (optional)
        """
        super().__init__(name, dob)
        self.children = children if children is not None else []
    
    def add_child(self, child):
        """Add a child to the parent's record."""
        if isinstance(child, Student):
            self.children.append(child)
        else:
            raise ValueError("Child must be a Student object")
    
    def display_details(self):
        """Display parent-specific information."""
        super().display_details()
        if self.children:
            print("Children:")
            for child in self.children:
                print(f"  - {child.name} (Grade {child.grade_level})")
        else:
            print("No children registered")
    
    def __str__(self):
        return f"Parent: {self.name} ({len(self.children)} children)"