from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Form, Header, Request
from fastapi.responses import JSONResponse
from fastapi import requests
from fastapi import FastAPI, Response, Form,status
from chat_roles.roles_response import chatbot
from transcripe.transcripe import transcription
#Fast API Object
app = FastAPI() 


# origins = ["*"]  
# origins = ["https://user-app.click", "https://user-app.click/", "https://voltox.tech/", "https://voltox.tech" ,"https://voltox.global/", "https://voltox.global","https://super-admin.click/", "https://super-admin.click" ,"http://localhost:3000/","http://localhost:3000"]

origins = ['*']  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


@app.post('/transcripe') 
async def transcripe(id: str = Form(...)): 
    try:
        flag = False
        data = ""
        # MODEL_NAME = "gpt-3.5-turbo"
        # chromadb.Client()
        print("API HIT ************* Transcription")
        flag , data = transcription(id)
        if status:
            response = {'status':200, 'flag':flag,'transcription_data' : data}
        else:
            response = {'status':404, 'flag':flag,'transcription_data' : data}
        print(response)
        return response
    except Exception as e:
        print(e)
        response = {'status':404, 'flag':flag,'transcription_data' : data}
        return response
    








@app.post('/send_chatbot_response') 
async def send_chatbot(context: str = Form(...),human_question: str = Form(...)): 
    try:
            
        # MODEL_NAME = "gpt-3.5-turbo"
        # chromadb.Client()
        print("API HIT ************* send_chatbot_response")

        chatbot_response,start_chat = chatbot(context,human_question)

        response = {'status':200, 'Chatbot':'{}'.format(start_chat)}
        print(response)

        return response
    except Exception as e:
        print(e)
        response = {'status':404, 'msg':'Something Went Wrong'}
        return response
    

