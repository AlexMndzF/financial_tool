import time

def update_financial_securitie(financial_securitie,peticion):    
    activos = financial_securitie["underlying_securities"]
    isi = financial_securitie["Synthetic_index"]
    Rt,activos = calculate_Rt(financial_securitie["underlying_securities"],peticion)
    #print(f"==============RT = {Rt}")
    #print(f"==============indice sintetico inicial = {isi}")
    si = isi*(1+Rt)
    #print(f"==============indice sintetico final = {si}")
    
    fs_final = {
                "id":financial_securitie["id"],
                "timestamp":time.time(),
                "Synthetic_index":si,
                "owner":financial_securitie['owner'],
                "entity":"banco santander",
                "underlying_securities":activos
                }
    return fs_final


def calculate_Rt(activos,peticiones):
    Rt = 0
    for ind in peticiones:
        print(peticiones[ind])
        for i in range(len(activos)):
            #activosid = activos[i]["id"]
            #peticionesid = peticiones[ind]["id"]
            #print('aid', activosid)
            #print('pid',peticionesid)
            if activos[i]["id"]==peticiones[ind]["idAS"]:
                #ppeticiones = peticiones[ind]["price"]
                #pactivos = activos[i]["price"]
                #print(f"=====================P_peticion = {ppeticiones}=====================")
                #print(f"=====================P_acit¡vos = {pactivos}=====================")
                rit=(peticiones[ind]["price"]/activos[i]["price"])-1
                Rt+=activos[i]["weight"]*rit
                activos[i]["price"] = peticiones[ind]["price"]
        return Rt, activos

