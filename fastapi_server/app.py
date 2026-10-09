from fastapi import FastAPI
from pydantic import BaseModel
class Student(BaseModel):
    stuname:str
    studept:str
    stuusername:str
    stupassword:str
    stuage:int
    stumark:float
app = FastAPI()

@app.get("/getStudents")
@app.post("/addStudent")
def getStudents():
    return "Get students method called"
#localhost:8000/getStudent
@app.post("/addStudent")
def addStudent(stu:Student):
    return {"student_details":stu}


@app.put("/updateStudent")
def updateStudent():
    return "Update student method called"
@app.delete("/deleteStudent")
def deleteStudent():
    return "Delete student method called"

@app.get("/getParticularStudent/{id}")
def getParticularStudent(id:int):
    return {"userid":id}
@app.get("/filterdept")
def filterdept(dept:str,mark:int):
    return {"dept":dept,"mark":mark}