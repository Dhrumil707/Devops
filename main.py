from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from controllers.doctorController import (
    create_doctor, get_doctors, get_doctor_by_id,
    update_doctor_by_id, delete_doctor_by_id
)
from models.doctorModel import Doctor

app = FastAPI(title="Doctor API", version="1.0.0")


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


@app.post("/addDoctor")
async def add_doctor(doctor: Doctor, response: Response):
    return await create_doctor(doctor, response)


@app.get("/getDoctors")
async def get_doctor_list(response: Response):
    return await get_doctors(response)


@app.get("/getDoctor/{id}")
async def get_doctor(id: str, response: Response):
    return await get_doctor_by_id(id, response)


@app.put("/updateDoctor/{id}")
async def update_doctor(id: str, doctor: Doctor, response: Response):
    return await update_doctor_by_id(id, doctor, response)


@app.delete("/deleteDoctor/{id}")
async def delete_doctor(id: str, response: Response):
    return await delete_doctor_by_id(id, response)
