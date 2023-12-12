from fastapi import FastAPI

#app = FastAPI(
#    title="Sample Docs",
#    description="This is private docs",
#    version='1.0',
#)

# in production we disable specification
#app = FastAPI(docs_url=None)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"hello {name}"}
# https://legendary-space-sniffle-4wvqqvg5pw43jpxx-8000.app.github.dev/

#root/docs