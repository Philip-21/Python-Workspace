from fastapi import FastAPI 
from fastapi import HTTPException
from model1 import User
from typing import List 
from uuid import UUID
from uuid import uuid4
from model1 import User, Gender, Role, UserUpdateRequest

db: List[User]=[# building a database which is in a list to store the User dataset found in model1
    User(
        id=uuid4(),
        first_name='Julia',
        last_name='Andrews',
        gender=Gender.female,
        roles=[Role.student, Role.user]#parsing julias role as a student
 ),
    User(
        id=uuid4(),
        first_name='John',
        last_name='Matthews',
        gender=Gender.male,
        roles=[Role.admin, Role.user]#parsing johns role as an admin
    )
]
#defining a route to give all the users in the list and exposing it to clients using fastapi
app =FastAPI()
@app.get('/') #sending a get request that retrives data from the db to api and getting back a list of users 
async def fetch_Users():
    return db;
    
#adding a new user to the database using post request sending a post request to api using the client extension click>post>json>body after click send
@app.post("/")
async def register_user(user:User):
    db.append(user) #adding a single item to the list 
    return{'id':user.id}

#Deleting a database , after parsing this code reload the swagger docs or use the client extensions  to select the ID and delete 
@app.delete("/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return

#raising a 404 error response to the client , after searchig an item deleted inthe database 
raise HTTPException(
    status_code=404,
    detail='user with id:{user_id} does not exists'
)

# parsing a put request for updating database
@app.put("/{user_id}")         #user_id is the path variable
async def update_user(user_update: UserUpdateRequest, user_id=UUID):
    for user in db: #using a for loop to check if all the Id and items match
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
        if user_update.last_name is not None :
            user.last_name=user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name=user_update.middle_name
        if user_update.roles is not None:
            user.roles=user_update.roles
            return #re raiseturn if everything matches
        raise HTTPException( #raise a 404 exception if the user is not found 
        status_code=404,
        detail=f'user with id: {user_id} does not exist'
         )            
