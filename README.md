# Financial tool

Herramienta que almacena los cambios en los valores financieros de los usuarios en cada actualizacion del precio de una de los valores subadyacentes. Recalcula el indice sintético del valor financiero, generando un nuevo registro en la base de datos para asi poder tener un historico.

Los datos esta almacenados en una base de datos MongoDB, los registros guardan el timestamp para poder estar trazados en todo momento.

los datos se introducen mediante formularios web,p ara hacer la aplicacion funcional para un flujo de datos grande, la opcion optima sería configurar un broker de kafka que gestionase todas las peticiones de entrada a la base de datos, para no perder informacion.

El framework que he elegido para este proyecto es Flask, por su lijereza y potencia sin necesidad de instalar plugins, cuenta con la tecnologia suficiente para hacer este proyecto.

## Rutas:

La aplicacion cuenta con 3 rutas:
 - Insertar (/inser): esta ruta es la que usaremos para añadir nuevos valores financieros, el formulario requiere un fichero json con el siguiente formato:  
```json
 {      
    "id":'BS_AM',  
    "timestamp":1581717368.347977,  
    "Synthetic_index":100,  
    "owner":"Alex Méndez",  
    "entity":"Banco santander",  
    "underlying_securities":  
    [  
        {  
            "id":0,  
            "type":"ACCION",  
            "price":70,  
            "weight":5  
        },  
        {   
            "id":1,  
            "type":"DEUDA",  
            "price":100,  
            "weight":15  
        }  
    ]  
} 
```

Donde:  
   >- id: formado por la entidad a la que pertenece y las iniciales del nombre y primer apellido del propietario.  
   >- timestamp: se genera automaticamente al crear el fichero, hay que pasarlo como valor 0.  
   >- Synthetic index: indice sintetico del valor financiero.  
   >- Owner: propietario del valor financiero.  
   >- entitiy: entidad de la que es el valor financiero.  
underlying securities: valores subadyacentes del valor financiero, este campo es una lista de jsons, en los que hay id del valor, tipo de valor, precio del valor y peso.  
 
 - Actualizar (/update): esta ruta es la que usaremos para actualizar los precios de los valores subadyacentes y actualizar el indice sintetico, esto genera un nuevo registro en la base de datos. El fichero de actualizaccion, solo puede actualizar un valor financiero. La forma del json debe ser la siguiente:  
```json
{
    "0":{
            "id":"EN_AM",  
            "id_fs":0,  
            "price":100  
        },
    "1":{
            ...  
        }  
    ...
}  
````

Donde:    
>- id: formado por la entidad a la que pertenece y las iniciales del nombre y primer apellido del propietario. Sirve para identiicar el valor  
financiero que vamos a actualizar.
>- id_fs: identifica el valor suadyacente al que pertenece la modificacion de precio.  
>- precio: nuevo valor de precio a actualizar.  

 - Visualizar (/line): Esta ruta la usaremos para ver una grafica de la evolucion del indice sintetico en el tiempo, la grafica esta generada en javascript, la funcion que la genera esta modificada para hacer la query de los valores financieros que queramos. La entrada de datos en esta ruta es un formulario de texto en el cual introduciremos el id del valor financiero.

 Para poder utilizar la aplicacion, es necesario añadir la URL de conexion de mongo al fichero .env con la clave: **URLMONGO**.

 El dockerfile esta preparado para crear un contenedor funcional de la aplicacion.