import pydantic
from config import db
from fastapi import APIRouter
from bson.objectid import ObjectId

LogRouter = APIRouter()


@LogRouter.post("/log/nuevo", description="registro log")
def logNuevo(data: list):
    arRegistro = db.mydb.insert_many(data)
    return {
        "Mensaje": "se agrego un registro nuevo"
    }

@LogRouter.post("/log/movimiento")
async def logMovimiento(data: dict):
    arrRegistros = db.mydb.find({"nombreEntidad": data['nombreEnditad'], "codigoRegistroPk": data['codigoRegistroPk']})
    arrResultado = []
    for item in arrRegistros:
        item['_id'] = str(item['_id'])
        arrResultado.append(item)

    return arrResultado


@LogRouter.post("/log/detalle/{id}", description="registro log")
def logDetalle(id: str):
    pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str
    arRegistro = db.mydb.find_one({"_id": ObjectId(id)})
    return arRegistro
