from fastapi import FastAPI  # FastAPI import

app = FastAPI()

@app.get("/") #get불러오기, post쓴다, update(put), delete() 
def printHello():
	return "멋진 멍청이"

@app.get("/json")
def printJson():
	return {
		"Number" : 12345
	}
    
class Post(BaseModel):
	title: str
	content: str

@app.post("/posts")   #클라이언트에게 받음 
def createContents(post : Post):
	title = post.title
	content = post.content
 
 
