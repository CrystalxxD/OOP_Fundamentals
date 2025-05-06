from subjects import Subject

subjects_list = []

def add_subject():
    print("\nAdd a new subject")
    name = input("Enter subject name: ")
    year_level = input("Enter year level: ")
    class_code = input("Enter class code: ")
    num_students = input("Enter number of students enrolled: ")
    
    try:
        num_students = int(num_students)
        new_subject = Subject(name, year_level, class_code, num_students)
        subjects_list.append(new_subject)
        print("Subject added successfully!")
    except ValueError:
        print("Invalid input for number of students. Please enter a valid integer.")

def view_subject():
    if not subjects_list:
        print("No subjects in the list.")
        return
    
    print("\nSubjects available:")
    for i, subject in enumerate(subjects_list, 1):
        print(f"{i}. {subject.name} (Year {subject.year_level})")
    
    try:
        choice = int(input("Enter the number of the subject to view: ")) - 1
        if 0 <= choice < len(subjects_list):
            print("\nSubject details:")
            subjects_list[choice].display()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_all_subjects():
    print("\nAll Subject Details:")
    Subject.display_all(subjects_list)

def main():
    while True:
        print("\nSubject Management System")
        print("1. Add a subject")
        print("2. View a subject")
        print("3. View all subjects")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_subject()
        elif choice == '2':
            view_subject()
        elif choice == '3':
            view_all_subjects()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()