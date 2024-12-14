class StudentRecord:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = [grade1, grade2, grade3, grade4]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        grades_str = ", ".join(f"{g:.2f}" for g in self.grades)
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Grades: [{grades_str}], Average: {self.average_grade():.2f}"


class StudentGradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully!")

    def update_grade(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Updating grades for {student.name}")
                for i in range(4):
                    student.grades[i] = float(input(f"Enter new grade {i + 1} (0-100): ").strip())
                print("Grades updated successfully!")
                return
        print("Student ID not found!")

    def display_students(self):
        if not self.students:
            print("No students in the system!")
        else:
            print("\nStudent Records:")
            for student in self.students:
                print(student)

    def calculate_class_average(self):
        if not self.students:
            print("No students to calculate average!")
            return
        total_average = sum(student.average_grade() for student in self.students) / len(self.students)
        print(f"\nClass Average Grade: {total_average:.2f}")


def main():
    manager = StudentGradeManager()
    while True:
        print("\nStudent Grade Record1")
        print("1. Add a new student")
        print("2. Update a student's grades")
        print("3. Display all students")
        print("4. Calculate class average grade")
        print("5. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            course = input("Enter Course (e.g., BSEcE, BSCS): ").strip()
            grade1 = float(input("Enter Grade 1 (0-100): ").strip())
            grade2 = float(input("Enter Grade 2 (0-100): ").strip())
            grade3 = float(input("Enter Grade 3 (0-100): ").strip())
            grade4 = float(input("Enter Grade 4 (0-100): ").strip())
            student = StudentRecord(student_id, name, course, grade1, grade2, grade3, grade4)
            manager.add_student(student)
        elif choice == "2":
            student_id = input("Enter Student ID to update grades: ").strip()
            manager.update_grade(student_id)
        elif choice == "3":
            manager.display_students()
        elif choice == "4":
            manager.calculate_class_average()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()
