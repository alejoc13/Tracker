Codigo recopilatorio de distintas funcionalidades de tracker que se han desarrollado en el equipo System Innovation (SI)

*helper*
Carpeta almacenadora de distintos .py utiles para el flujo de trabajo

    *LoadDAta*
    Este archivo contiene las fucniones que cargan los datos desde los excel
    
    *procesing*
    Contiene todas las fucniones realcioandas al procesamiento de datos, cosas como el trimeo de datos, recorte de columnas
    que tienen datos importantes en una sola celda y creación de exceles de salida entre otras cosas.

    *trackerType*
    Este .py compila los pasos necesarios para generar los trackers del menú de inicio

    *callOption*
    ejecutor de lso distintos tipso de traccker, cada tipo de tracker carga unicamente los excel necesarios para su funcionamiento
 
 *Documents*
 En esta carpeta se deben almacenar los excel necesarios, los correpondientes al submmision plan, vouchers y critical communications deben con servar esos nombres
 siempre, los relacionados a cfns y numeros de licencia pueden cambiar su nombre pero deben cumplir una regla:
   1. El documento para trackear pro CFNs debe tener una unica columna y su encabezado debe ser CFN
   2. El documento para trackear por Registration number debe tener uan unica columna y debe tener como encabezado REGISTRATION
   Importante en ambos casos conservar las mayusculas en los encabezados de las columnas

*trackResults*
Ene sta carpeta se almacenaran los resultados de los trackers qeu se realicen.

*main*
Ejecutor del proyecto, contiene el entry poinit y despliega en cosonla el menú de usuario

*Nota importante*
Cuando el algoritmo le pida los nombres de lso archivos a cargar o los nombres para los archivos a crear NO PONER LA EXTENCIÓN (xlsx) puesto que el algoritmo se lo adicionará automaticamente



