from fastapi import FastAPI
from typing import List
import read_db, options_sch


app = FastAPI()

@app.get("/")
async def root():
   return {"message":"Benvingut a fastapi"}


@app.get("/penjat/tematica/opcions", response_model = List[dict])
async def get_options():
   return options_sch.options_schema(read_db.read_db())


@app.get("/penjat/tematica/{option}", response_model = List[dict])
async def get_word(option: str):
   word = options_sch.options_schema(read_db.read_word_db(option))
   print("")
   print("IMPRESSIÓ WORD del mètode GET_WORD")
   print(type(word))
   print(word)
  
   return word