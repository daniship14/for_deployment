
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI running"}

@app.get("/cicd-test")
async def cicd_test():
    return {
        "status": "success",
        "message": "Jenkins CI/CD is working"
    }

@app.get("/newcicd-test")
async def cicd_test():
    return {
        "status": "success",
        "message": "Jenkins CI/CD is working"
    }