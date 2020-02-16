import time

def update_financial_securitie(financial_securitie,peticion):    
    activos = financial_securitie["underlying_securities"]
    isi = financial_securitie["Synthetic_index"]
    p_peticion = peticion["price"]
    
    Rt,activos = calculate_Rt(financial_securitie["underlying_securities"],peticion)
    si = isi*(1+Rt)
    
    fs_final = {
                "id":financial_securitie["id"]+1,
                "timestamp":time.time(),
                "Synthetic_index":si,
                "owner":"pepe",
                "entity":"banco santander",
                "underlying_securities":activos
                }
    return fs_final


def calculate_Rt(activos,peticiones):
    Rt = 0
    for ind in range(len(peticiones)):
        for i in range(len(activos)):
            if activos[i]["id"]==peticiones[ind]["idAS"]:
                rit=(peticiones[ind]["price"]/activos[i]["price"])-1
                Rt+=activos[i]["weight"]*rit
                activos[i]["price"] = peticiones[ind]["price"]
        return Rt, activos

