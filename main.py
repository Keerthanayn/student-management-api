from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

students = [
    {
        "id": 1,
        "name": "Gagan",
        "age": 21,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Rachana",
        "age": 22,
        "course": "FastAPI"
    }
]

@app.get("/")
def home():
    return {
    "message": "Welcome to Student Management API",
    "status": "Running",
    "version": "1.0"
}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):

    students.append(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student
    }

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = updated_student.model_dump()

            return {
                "message": "Student updated successfully",
                "student": students[index]
            }

    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    return {"message": "Student not found"}

@app.get("/test/{number}")
def test_path(number: int):
    return {
        "received_number": number
    }

@app.get("/search")
def search_students(course: str):

    result = []

    for student in students:

        if student["course"] == course:
            result.append(student)

    return result