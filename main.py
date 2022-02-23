#creating api for a  basic socialmedia news app
#using the traditional method to communicate between the API and  the SQL  database
#using the CRUD operation (Create,Read, Update, Delete) which are the main functions of an applications

from fastapi import FastAPI, Response,status,HTTPException
from typing import Optional
from pydantic import BaseModel 
from fastapi.params import Body
import psycopg2 # a python postgres driver adapter for importing and ugrading the database from Postgres
from  psycopg2.extras import RealDictCursor #parses an extra field to get the names column not  just the value of the columns 
from random import randrange #to create a random number ot intrger to genarate an ID
import time 


class Newspost(BaseModel):#declaring the newspost as data model
    title: str
    contents: str 
    published : bool = True#defining if a user publishes a post 
    rating: Optional[int]= None


app =FastAPI()
while True: #creating a loop to run continuosly until a connection is gotten
    try :#used if connection to a database fails 
        conn =psycopg2.connect(host="localhost", database="FastApi", user="postgres",
        password="philippians",cursor_factory=RealDictCursor)
        cursor =conn.cursor()# performs database operations like sql statements 
        print("Database connected successfully")
        break #break th loop if database is connected    
    except Exception as error:
        print("Database connetion failed ")
        print("Error: ",error)
        time.sleep(3)#taking 3 seconds to reconnect

@app.get("/")
def root():
    return{'message':'welcome'}

#updating  the create post path operation  
@app.post("/posts",status_code=status.HTTP_201_CREATED) #create operation 
def create_new_post(post:Newspost): #declaring post as a variable to the datamodel 
    cursor.execute("""INSERT INTO newspost (title,contents,published) VALUES(%s,%s,%s) RETURNING *""" ,(post.title,post.contents,post.published)) #%srepresents variables (post.title,post.contents,post.published) that describe the  data  passed into the sql statement 
    new_post=cursor.fetchone()# gets the return value from the returning keyword
    conn.commit() #pushes the changes out and the posts will be saved and reflects into the postgres databse
    return{"data":new_post} 
   

@app.get("/posts") #read operation
def get_news():
    cursor.execute("""SELECT * FROM newspost """)#parsing the sql statement in retrieving columns 
    posts= cursor.fetchall()
    return{"data":posts} 
    


#retrieving one individual post
@app.get("/posts/{id}")#read operation extracting id from a specific url
def get_post(id:str): 
    cursor.execute("""SELECT * FROM newspost WHERE id = %s """,(str(id))) #id is parsed as a str due to the select statement parsed 
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"oops ID {id} was not found")
    return{'postdetail':post}

#update posts
@app.put("/posts/{id}") #update operation 
def update_post(id:int,post:Newspost):
    cursor.execute("""UPDATE newspost SET title=%s, contents=%s, published=%s RETURNING*""",(post.title,post.contents,post.published),(str(id)))
    updated_post =cursor.fetchone()
    conn.commit() #push changes in the postgres database
    if updated_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return{"data":updated_post}


#deleting posts
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT) #Delete operation 
def delete_post(id: int):
    cursor.execute("""Delete from newspost where id=%s  RETURNING* """,(str(id)))  #returning * is used used to see what the post was before deleting 
    deleted_post = cursor.fetchone()
    conn.commit() #push changes in the postgres database
    if deleted_post== None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)   
    return Response(status_code=status.HTTP_204_NO_CONTENT)    





