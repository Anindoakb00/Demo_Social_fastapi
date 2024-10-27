


from..import models,schemas,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from..database import get_db
from ..routers import auth  

from sqlalchemy.orm import Session
from typing import List,Optional
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#after separated schemas into different modules.py we don't need this. that is why we are commiting out this
#@app.get("/sqlalchemy")
#def test_posts(db:Session = Depends(get_db)):
    #posts = db.query(models.Post).all()
    #return {"data": posts}

@router.get("/",response_model=List[schemas.Post])
#def get_posts():
    #cursor.execute(""" SELECT * FROM posts""")
    #posts = cursor.fetchall()
def get_posts(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user),
               limit: int = 10,skip: int =0,search:Optional[str] = "" ):
    print(limit)
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
 
    
    if not posts:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authioraised to perferm requested action")
    print(posts)
    return posts



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post :schemas.PostCreate, db:Session = Depends(get_db)
                 ,get_current_user:int = Depends(oauth2.get_current_user)):
      
   # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #(post.title,post.content,post.published))
    #new_post = curso  r.fetchone()
    #conn.commit()
    print(get_current_user)#The meaning of using star is here to unpack the dictionaries
    new_post = models.Post(owner_id=get_current_user.id, **post.dict())# it will catch all the data in the formate of dictionary type
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

#title str, content str, category, Bool published    
     

#Retreving one individual Post
@router.get("/{id}",response_model=schemas.Post)
def get_post(id:int, db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):  
    #cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))
   # post = cursor.fetchone()
   # start code with sqlalchemy
   post = db.query(models.Post).filter(models.Post.id == id).first()
   #print(post)

    
   if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"post with id: {id} was not found")
   if post.owner_id != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not a uthioraised to perferm requested action")
        
   return post  

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)#Must return 204 status
                                                                
def delete_post(id: int,db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #deleting post
    #find the index in the array that has required ID
    #my_posts.pop(index)
    #lets postpone the sqlcode
    #cursor.execute("""DELETE FROM posts WHERE id =%s returning *""",(str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    #let us start the sqlalchey post
    Post_query = db.query(models.Post).filter(models.Post.id==id)

    Post = Post_query.first()


   
    if Post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} does not exist")
    if Post.owner_id != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authioraised to perferm requested action")
    Post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #lets comment out the postgre post 
    #cursor.execute("""UPDATE posts SET title = %s, content = %s ,published = %s WHERE id = %s RETURNING *""",
    #(post.title,post.content,post.published, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()
    Post_Query = db.query(models.Post).filter(models.Post.id==id)
    Post = Post_Query.first()


    
    if Post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")
    if Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authioraised to perferm requested action")
    
    Post_Query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    
    return Post_Query.first()










