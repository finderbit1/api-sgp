from database2.bd import get_session
from .schema import Envio



def search_id(id:int) -> Envio| None:
    with get_session() as se:
        return se.get(Envio, id)



if __name__ == "__main__":
    search_id(15)




