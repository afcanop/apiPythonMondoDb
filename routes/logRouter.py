import pydantic
from config import db
from fastapi import APIRouter
from bson.objectid import ObjectId

LogRouter = APIRouter()


@LogRouter.post("/log/nuevo", description="registro log")
def logNuevo(data: dict):
    arRegistro = db.connecion.cromo.genLog.insert_one(data).inserted_id
    return {
        "Mensaje": "se agrego un registro nuevo",
        "id": str(arRegistro)
    }

@LogRouter.get("/log/movimiento/{nombreEnditad}/{codigoRegistroPk}")
async def logMovimiento(nombreEnditad: str, codigoRegistroPk: str):
    arrRegistros = db.connecion.cromo.genLog.find({"nombre_entidad": nombreEnditad, "codigo_registro_pk": codigoRegistroPk})
    arrResultado = []
    for item in arrRegistros:
        item['_id'] = str(item['_id'])
        arrResultado.append(item)

    return arrResultado


@LogRouter.post("/log/detalle/{id}", description="registro log")
def logDetalle(id: str):
    pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str
    arRegistro = db.connecion.cromo.log.find_one({"_id": ObjectId(id)})
    return arRegistro
