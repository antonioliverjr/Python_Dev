import uvicorn
from fastapi import FastAPI
from package_viacep import viacep

app = FastAPI()

@app.get("/")
async def root():
    casa = viacep.ViaCep()
    return casa.GetData('42808193')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
