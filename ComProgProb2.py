class EmployeeRecord:
    def __init__(self, employee_id, name, organization):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []

    def mark_attendance(self, is_present):
        self.attendance.append(is_present)

    def attendance_percentage(self):
        total_days = len(self.attendance)
        if total_days == 0:
            return 0.0
        present_days = self.attendance.count(True)
        return (present_days / total_days) * 100

    def __str__(self):
        attendance_str = ", ".join(["P" if day else "A" for day in self.attendance])
        return f"ID: {self.employee_id}, Name: {self.name}, Organization: {self.organization}, Attendance: [{attendance_str}], Percentage: {self.attendance_percentage():.2f}%"


class AttendanceManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added")

    def mark_attendance(self):
        if not self.employees:
            print("No employees to mark attendance")
            return

        print("Mark attendance for the day:")
        for employee in self.employees:
            status = input(f"Is {employee.name} (ID: {employee.employee_id}) present? (y/n): ").strip().lower()
            if status == "y":
                employee.mark_attendance(True)
            elif status == "n":
                employee.mark_attendance(False)
            else:
                print("Invalid input, marking absent by default.")
                employee.mark_attendance(False)
        print("Attendance marked for all employees")

    def display_attendance_records(self):
        if not self.employees:
            print("No employee attendance records")
        else:
            print("\nEmployee Attendance Records:")
            for employee in self.employees:
                print(employee)

    def display_attendance_percentages(self):
        if not self.employees:
            print("No employee attendance records")
        else:
            print("\nEmployee Attendance Percentages:")
            for employee in self.employees:
                print(f"{employee.name} (ID: {employee.employee_id}): {employee.attendance_percentage():.2f}% attendance")


def main():
    manager = AttendanceManager()
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Add an employee")
        print("2. Mark attendance")
        print("3. View attendance records")
        print("4. Display attendance percentage")
        print("5. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            employee_id = input("Enter Employee ID: ").strip()
            name = input("Enter Employee Name: ").strip()
            organization = input("Enter Organization Name: ").strip()
            employee = EmployeeRecord(employee_id, name, organization)
            manager.add_employee(employee)
        elif choice == "2":
            manager.mark_attendance()
        elif choice == "3":
            manager.display_attendance_records()
        elif choice == "4":
            manager.display_attendance_percentages()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    main()
