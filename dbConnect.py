import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
doctorDB = client["doctor_database"]
doctorCollection = doctorDB["doctors"]
