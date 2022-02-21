# import FastAPI - it is a python class that provides all the functionality for my API
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User

# create a FastAPI instance.
# this is the main point of interaction to create all the API
app = FastAPI()

# create a database, which is a list of users
db: List[User] = [
    User(
        id=UUID("48823efd-1a3a-4a64-b723-196fbd35e96e"),
        first_name="Dee",
        last_name="Leo",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("574ff1cb-9d31-4774-a3a3-d55ef05a22df"),
        first_name="Scott",
        last_name="Muir",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

### CREATE A PATH OPERATION FUNCTION ###
# path is "/"
# operation is "get"
# function is "async def" ( it can also be a normal "def" fucntion, if async is not necessary)
# return the content (can be a dict, a list, a singular value..)

# you can declare path paramenters, which can be passed to the function as arguments
# you can also declare the type of a path parameter in the function -- this gives editor support!
# With the same Python type declaration, FastAPI gives you data validation (passing a string or a float will throw an error with a clear message, helpful for debugging)
# data validation is performed by Pydantic


@app.get("/")
async def root():
    return {"Hello": "Mundo"}

# define a route to get all users


@app.get("/users")
async def fetch_users():
    return db

# post requests cant be tested


@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
