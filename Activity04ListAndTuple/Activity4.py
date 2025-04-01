import json
import os

class StudentRecordManager:
    def __init__(self):
        #Initialize an empty records list and filename variable.
        self.records = []
        self.filename = None

    def load_file(self, filename):
        #Load student records from a JSON file.
        if os.path.exists(filename):  # Check if file exists
            with open(filename, "r") as file:
                self.records = json.load(file)  # Load records into the list
            self.filename = filename
            print("File loaded successfully.")
        else:
            print("File not found.")

    def save_file(self):
        #Save current records to the opened file.
        if self.filename:
            with open(self.filename, "w") as file:
                json.dump(self.records, file)  # Save records in JSON format
            print("File saved successfully.")
        else:
            print("No file is currently open. Use 'Save As' to specify a filename.")

    def save_as(self, filename):
        #Save records to a new file and update the filename.
        with open(filename, "w") as file:
            json.dump(self.records, file)
        self.filename = filename
        print("File saved successfully as", filename)

    def show_all_records(self):
        #Display all student records.
        for record in self.records:
            print(record)

    def order_by_last_name(self):
        #Sort records by last name in ascending order.
        self.records.sort(key=lambda x: x[1][1])  # Sort using last name
        print("Records sorted by last name.")

    def order_by_grade(self):
        #Sort records by computed grade (60% Class Standing + 40% Major Exam).
        self.records.sort(key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
        print("Records sorted by grade.")

    def show_student_record(self, student_id):
        #Find and display a specific student's record by ID.
        record = next((r for r in self.records if r[0] == student_id), None)
        if record:
            print(record)
        else:
            print("Student record not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):
        # Add a new student record if the Student ID is unique.
        if any(r[0] == student_id for r in self.records):
            print("Student ID already exists.")  # Prevent duplicate IDs
            return
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    def edit_record(self, student_id, first_name=None, last_name=None, class_standing=None, major_exam=None):
        #Edit an existing student's record while keeping unchanged fields.
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                # Replace only the fields that are provided, keep others unchanged
                new_record = (
                    student_id,
                    (first_name or record[1][0], last_name or record[1][1]),
                    class_standing if class_standing is not None else record[2],
                    major_exam if major_exam is not None else record[3]
                )
                self.records[i] = new_record
                print("Record updated successfully.")
                return
        print("Student ID not found.")

    def delete_record(self, student_id):
        #Remove a student's record by ID.
        self.records = [r for r in self.records if r[0] != student_id]
        print("Record deleted successfully.")

def main():
    manager = StudentRecordManager()

    while True:
        #Display menu options
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter filename: ")
            manager.load_file(filename)
        elif choice == "2":
            manager.save_file()
        elif choice == "3":
            filename = input("Enter new filename: ")
            manager.save_as(filename)
        elif choice == "4":
            manager.show_all_records()
        elif choice == "5":
            manager.order_by_last_name()
        elif choice == "6":
            manager.order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == "8":
            # Collect new student data
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "9":
            # Collect details for editing an existing record
            student_id = input("Enter Student ID to Edit: ")
            first_name = input("Enter New First Name (leave blank to keep current): ") or None
            last_name = input("Enter New Last Name (leave blank to keep current): ") or None
            class_standing = input("Enter New Class Standing Grade (leave blank to keep current): ")
            major_exam = input("Enter New Major Exam Grade (leave blank to keep current): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam = float(major_exam) if major_exam else None
            manager.edit_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "10":
            student_id = input("Enter Student ID to Delete: ")
            manager.delete_record(student_id)
        elif choice == "11":
            break  # Exit the program
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
