from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
	return { 'Hola': 'Mundo' }

if __name__ == '__main__':
	uvicorn.run('main:app', reload=True)
