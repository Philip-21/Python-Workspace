#creating api for a  basic socialmedia news app
from fastapi import FastAPI, Response,status,HTTPException
from typing import Optional
from pydantic import BaseModel 
from fastapi.params import Body
class Newspost(BaseModel):#declaring the newspost as data model
    title: str
    contents: str 
    published : bool = True#defining if a user publishes a post 
    rating: Optional[int]= None

app =FastAPI()


@app.get("/")
def root():
    return{'message':'hi There'}


#creating a variable post that stores all posts in an array .
mypost =[{'title':"WWE","contents":"Monday night raw ","id":1},{"title":'football news','contents':"Transfer Window","id":2}]


#updating  the create post path operation to figure out how to add a new post to mypost array 
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_new_post(Post:Newspost): #declaring Post as a variable to the datamodel 
    Newspost_dict=Post.dict() #parsing the datamodel into a dictionary
    Newspost_dict['id']=randrange(0,10000000) #generating an ID in the basemodel when a client posts 
    mypost.append(Newspost_dict)#adding a new item to basemodel dictionary inline with the array variable mypost
    return{"data":Newspost_dict} #data that would be genarated 

#implementing the logic of getting the post 
def find_Post(id):
    for p in mypost:   #iterating over the specific post p
        if p["id"]==id:
            return p

#retrieving one individual post
@app.get("/posts/{id}")#our path parameter is id
def get_post(id:int,response:Response): #performing validation on id as an integer,parsing response into a varable  
    Post = find_Post(id)
    if not Post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"oops ID {id} was not found")
    return{'postdetail':Post}


@app.get("/posts")
def get_news():
    return{"result":mypost} 
    

#update post
@app.put("/posts/{id}")
def update_post(id:int,post:Newspost):
    index= find_index_post(id) #finding the index of a specific post wh

    if index ==None:
         if index== None:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


    post_dict= post.dict() #this takes the data we recieve from the frontend which is stored in post and converts it to a dictionary 
    post_dict['id']= id
    mypost[index]= post_dict
    return {"data":post_dict}   

#deleting a post
def find_post(id):
    for p in mypost:
        if p['id']==id:
            return p

def find_index_post(id):
    for i, p in enumerate(mypost):   #gets access to the individual posts and the  index      
        if p["id"]==id:
             return i     
#delete request
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index= find_index_post(id) #find the index in the array of specific item with required ID
    if index== None: #raising a response for an id that doesnt exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    mypost.pop(index)#removing index
    return Response(status_code=status.HTTP_204_NO_CONTENT) #response code for deleted item         



