from fastapi import Response
from dbConnect import doctorCollection
from bson import ObjectId


# CREATE
async def create_doctor(doctor, response: Response):
    try:
        result = await doctorCollection.insert_one(doctor.dict(exclude={"id"}))
        response.status_code = 201
        return {
            "isSuccess": True,
            "message": "Doctor added successfully",
            "doctorId": str(result.inserted_id)
        }
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "error": str(e)}


# READ ALL
async def get_doctors(response: Response):
    try:
        doctors = []
        async for doctor in doctorCollection.find({}):
            doctor["id"] = str(doctor.pop("_id"))
            doctors.append(doctor)
        response.status_code = 200
        return {"isSuccess": True, "count": len(doctors), "doctors": doctors}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "error": str(e)}


# READ BY ID
async def get_doctor_by_id(id: str, response: Response):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400
            return {"isSuccess": False, "message": "Invalid Doctor ID"}

        doctor = await doctorCollection.find_one({"_id": ObjectId(id)})
        if doctor:
            doctor["id"] = str(doctor.pop("_id"))
            response.status_code = 200
            return {"isSuccess": True, "doctor": doctor}

        response.status_code = 404
        return {"isSuccess": False, "message": "Doctor not found"}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "error": str(e)}


# UPDATE
async def update_doctor_by_id(id: str, doctor, response: Response):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400
            return {"isSuccess": False, "message": "Invalid Doctor ID"}

        result = await doctorCollection.update_one(
            {"_id": ObjectId(id)},
            {"$set": doctor.dict(exclude={"id"})}
        )
        if result.matched_count == 1:
            response.status_code = 200
            return {"isSuccess": True, "message": "Doctor updated"}

        response.status_code = 404
        return {"isSuccess": False, "message": "Doctor not found"}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "error": str(e)}


# DELETE
async def delete_doctor_by_id(id: str, response: Response):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400
            return {"isSuccess": False, "message": "Invalid Doctor ID"}

        result = await doctorCollection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            response.status_code = 200
            return {"isSuccess": True, "message": "Doctor deleted"}

        response.status_code = 404
        return {"isSuccess": False, "message": "Doctor not found"}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "error": str(e)}
