Doctor CRUD USING MONGODB

Structure follows the uploaded FastAPI study notes, section 12.1.
Routes are in main.py. There is no separate routers folder.
This is adapted from the notes' Product example; entity names and fields vary.
All six versions provide the same five CRUD operations.

FILES
main.py
 dbConnect.py
 .env
 requirements.txt
 controllers/doctorController.py
 models/doctorModel.py

RUN LOCALLY (Python 3.12 recommended)
1. Open this folder in VS Code. The terminal must be in the folder with main.py.
2. Make sure your local MongoDB Server is running at localhost:27017.
   If you already have MongoDB running, do not start another server.
3. Install dependencies:
   python -m pip install -r requirements.txt
4. Start FastAPI:
   python -m uvicorn main:app --reload
5. Open http://127.0.0.1:8000/docs
6. Use POST /addDoctor with the request body shown below.
7. Copy the returned doctorId for GET by ID, PUT and DELETE.
   The ID is a MongoDB-generated string, not an integer.

REQUEST {
    "name": "Dr Patel",
    "specialization": "Cardiology",
    "salary": 50000.0
} (POST and PUT)
{
    "name": "Dr Patel",
    "specialization": "Cardiology",
    "salary": 50000.0
}

Database: doctor_database
Collection: doctors
Both are created on the first successful insert.

For Atlas, replace DB_URL in .env with your own connection string.
For Render, set DB_URL in the service environment to your Atlas URI;
localhost on Render cannot connect to MongoDB running on your Windows PC.
Do not commit actual database credentials. .env is excluded by .gitignore.

NOTES
- The optional id field is excluded from insert/update. MongoDB generates _id.
- ObjectId is converted to string id before returning data as JSON.
- Invalid ID: 400; missing record: 404; invalid body: 422.
- No f-strings or .bat files are included.
- .dict() is retained to match your class notes' code style.
- Motor is retained to match your supplied async code.
- MongoDB must be reachable for CRUD calls to succeed.
- This bundle does not copy an existing deployment hook or CI/CD workflow.
