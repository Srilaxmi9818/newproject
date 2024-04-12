import pickle

# Part A: Serialize student records to a file named "students.pkl"
def serialize_students(records):
    try:
        with open("students.pkl", "wb") as file:
            pickle.dump(records, file)
        print("Student records serialized successfully.")
    except Exception as e:
        print("An unexpected error occurred during serialization:", e)

# Part B: Deserialize "students.pkl" and print the contents
def deserialize_students():
    try:
        with open("students.pkl", "rb") as file:
            records = pickle.load(file)
            print("Student records:")
            for student in records:
                print(f"Name: {student['name']}, ID: {student['id']}, Grades: {student['grades']}")
    except FileNotFoundError:
        print("Error: 'students.pkl' file not found.")
    except Exception as e:
        print("An unexpected error occurred during deserialization:", e)

# Sample student records
students = [
    {"name": "John Doe", "id": 101, "grades": [85, 90, 88]},
    {"name": "Jane Smith", "id": 102, "grades": [78, 92, 85]},
    {"name": "Alice Johnson", "id": 103, "grades": [90, 88, 95]}
]

# Serialize student records
serialize_students(students)

# Deserialize and print student records
deserialize_students()
