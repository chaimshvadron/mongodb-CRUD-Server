from fastapi import FastAPI
from dal_c import SoldierDAL

app = FastAPI()
dal = SoldierDAL()

@app.get("/soldiersdb/")
def get_all_soldiers():
    soldiers = dal.get_all_soldiers()
    return [s.to_dict() for s in soldiers]
