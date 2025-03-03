from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import leyendaRoute
# import uvicorn


app = FastAPI()

# if __name__ == "__main__":
#     uvicorn.run(app, host="http://127.0.0.1", port=8080, reload=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(leyendaRoute.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}