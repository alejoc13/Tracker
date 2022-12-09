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

#--------------------------------------------------------------------------------------------
Consideraciones de cada funcionalidad del tracker:

*Todos los archivos deben ser archivos de tipo .xlsx*

 1. Los archivos: La herramienta tiene una carpeta de nombre 'Documents' en la cual se deberán almacenar los documentos que se espera utilizar al ejecutar el tracker.
    Por favor tenga en cuenta lo siguiente a la hora de cargar archivos:
      a. Para los tracker de CFN y Resgistration number: El nombre del documento no es relevante, lo importante es cumplir con la normativa de como debe estar internamente
         el documento, además tenga en cuenta que cuando la herramienta le solicite el nombre del archivo debe ingresarlo sin la extensión (.xlsx)
      b. Documentos de Smartsheets: Por el momento no es posible conectarse directamente con Smarsheet desde la herramienta, por tanto siempre que usted utilice la herramienta
         lo aconsejable es qeu descargue los reportes y los reemplace en la carpeta documents Manteniendo los nombres orginales con los que se le entregará inicialmente. Esto le
         garantizará que la información se encuentra al día y no perderá datos. Los nombres que debe conservar son:
            - Submission Plan - Full Report
            - Expected Critical Communications Report
            - Vouchers Report
 2. Los ingresos manuales: Algunas partes de la herramienta requeiren que el usuario de infomración a través de la consola. Tenga en cuenta que el exito del funcionamiento de la herramienta 
    está en gran medida en que lo qeu usted ingrese de forma manual se encuente correctamente escrito, algunos casos son los siguiente:
      a. SubOU: En este caso es imperativo que el separador sean comas(,) de lo contrario el algoritmo dejará de funcionar. Si usted deja un esapcio despues de la coma para escribir la siguiente
         SubOU no representará un problema en particular.
      b. Nombres de Archivo: En casos como lso tracker por CFN y Número de registro debe ser muy preciso en la escritura y repetar mayuscular y minusculas que contenga el nombre del documento, puesto
         que de no ser así no se podrá encontrar el documento y fallará la herramienta.
   
   En los archivos principales (listados en 1.b) se deberá mantener intacto los nombres de columnas, si se modifican generará errores en la ejecución de la herramienta
         
   Reitero que las extensiones deben ser unicamente .xlsx

#--------------------------------------------------------------------------------------------
Como Iniciar el uso de la herramienta

Opcion 1: Aunqeu como podrá observar, el proyecto está dividido en multiples carpetas y archivos .py, pero para inciiar el uso de la herramienta deberá unicamente correr el el archivo de nombre main.py
el cual se encuentra fuera de todas las carpetas internas del proyecto.

Opción 2: Con VScode abierto en la caprta del proyecto (Tracker) utilice en la consola el sigueinte comando:
   python main.py

NOTA: si inició la ejecución del algoritmo y decidió que no requeire utilizar en este momento precione enter en el menú de selección de la herramienta y esto terminará la ejecución del algoritmo de forma inmediata

#--------------------------------------------------------------------------------------------
Seleccionar la opción a utilizar

Puede surgir la duda de como hacer la selección del tracker a uilziar, si utilizar el número de la opción o el nombre de la misma. Para el caso de nuestra herramienta usted hará la selección con el número de la opción
como le indicará el menú de selección qeu se despliega al iniciar el uso del proyecto.

#--------------------------------------------------------------------------------------------
Descripción de cada funcionalidad

 1. Tracker por cfn: Este tracker requiere qeu se cargue a la carpeta 'Documents' un archivo de extensión .xlsx el cual debe contener una unica columna
    la cual debe tener por header(titulo de columna) CFN respetando las mayusculas, posterioremnte debe venir el listado de CFNs a trackear. Cuando la herramienta
    le solicite el nombre del archivo, recuerde que no debe darselo con la extensión(.xlsx) puesto que el algoritmo se la asignará internamente. Tenga en cuenta
    que el archivo puede tener cualqueir nombre siempre que se repeten las condicioens anteriormente expresadas
 
 2. Tacker por SubOU: Este tracker le pedirá que ingrese de forma manual y separado por comas (,) el lsitado de subOUs qeu necesita trackear, tenga en cuenta que al 
    ser un ingreso manual parte del exito del tracker es que usted ingrese adecuadamente el texto. Además tenga en cuenta que de necesitar trackear SubOU antiguas, deberá
    ingresarlas de forma independiente tambien separadas por coma (,) cuando se lo solciite la herramienta.

 3. Tracker por Número de registro: Este tracker requiere qeu se cargue a la carpeta 'Documents' un archivo de extensión .xlsx el cual debe contener una unica columna
    la cual debe tener por header(titulo de columna) REGISTRATION respetando las mayusculas, posterioremnte debe venir el listado de CFNs a trackear. Cuando la herramienta
    le solicite el nombre del archivo, recuerde que no debe darselo con la extensión(.xlsx) puesto que el algoritmo se la asignará internamente. Tenga en cuenta
    que el archivo puede tener cualqueir nombre siempre que se repeten las condicioens anteriormente expresadas.
 
 4. Tracker de planning review(fechas omitidas de submitted y Approved): Esta función está especializada en la busqueda de procesos que en el submission Plan alcanzaron los
    estados 'submitted' y 'Approved' a los cuales no se les ingresaron las fechas en qeu se alcanzaron estos estados.

 5. Tracker de procesos Resagados(mas tiempo del esperado en Submitted): Esta función enceuntra todos los precesos del submission Plan que se encuentran en submitted, a los cuales
    se les realiza uan revisión de la fecha estamada de aprovación, en caso de que esta fecha se enceuntre superada por 90 días calendario, se reportará el proceso como un proceso
    resagado.
 
 6. Tracker Missed Voucher: Utilizando el reporte de Smartsheet que consolida todo el historial de Vouchers atendidos por el equipo SI se realiza una busqeuda en el submmission plan
    de todos los preocesos para México y Argentina que potencialmente signifiquen un proceso de vouchers, de no estar este proceso en nuestro consolidado se reportará como un missed
    Voucher.
 
 7. Tracker por lapsos de tiempo(se da una fecha de inicio y de finalización): Esta funcionalidad le solicitará que ingrese dos fechas una de inicio y otra de finalizacion, estas dos
    estas fechas definirám el rango de busqeuda de fechas de vencimiento que se tendrá en ceunta para el reporte. de vencimientos, siendo esta la opción mas adecuada para realziar
    planeación de renovaciones.

 8. Tracker de elementos vencidos(Se omite Honduras y Rep. Dominicanda): Esta función busca los registros en lso cuales se superó la fecha de expiración presente en la base de datos y
    vrea un reporte con ellos. Es la mejor herramietna para la limpieza de registros vencidos en las bases de datos.

 9. Missed Critical communications(Cancell Renewal): Opción que permite comparar el reporte 'Expected Critical Communications Report' con las bases de datos, de manera que nos permite
    determinar todos los procesos qeu degberían reportarse como No se renovará pero no se encuentran de esa manera.
 
 10. Missed Critical communications (approved CFN Withdrawal): en este caso se reportan todas las potenciales critical communications que provienen del proceso de retirar CFNs de licencias
     (CFN Withdrawal), para hcer mas facil la lectura de los acmbiso que devieron realiarce se presenta una hoja enq eu se cruza con el submmision plan de manera que si el RAS reportó los CFNs
     afectados esstos se encontrarán listados ahí.
 
 11. Gaps on DataBases Report: Esta herramienta genera un consolidado de todos los registros y permite identificar cuando un registro no fue alimentado en las bases de datos un CFN despues del sigueinte,
     sino   que por el contrario tiene saltos en la BD, cosa que podría inducir a perdida vizual de la información si no se tioene esto en ceunta. 
 
#--------------------------------------------------------------------------------------------
Consideraciones en la finalización de la ejecución

Por cuestiones de orden se desarrolló la herramienta para tener una carpeta llamada 'trackResults' en la cual se almacenarán todos los resultados de las diferentes ejecuciones que se realicen a lo largo del
uso de la misma.

En general las funcionalidades cuando terminen de realizar el proceso de busqueda de la información le solictará un nombre de archivo, Este nombre es el que se le dará al archivo de excel que es el resultado
de cada función. De la misma manera que con os archivos de entrada ustede deberá proporcionar un nombre sin extensión de archivo (.xlsx) ya que esto será agregado internamente por el algoritmo.

Adiconalmente tenga en cuenta que algunas funcionalidades le generaran mas de una rchivo de salida, en este caso en pantalla se le informará como se encuentra internamente dividido el archivo(titulos de las hojas)
siendo las opciones por cluster y por Therapy group. tenga esto en cuenta a la hora de nombrar sus archivos para evitar confuciones de su contenido.
   Aclaración: En los casos en qeu se presente el doble archivo la diferencia no será de contenido, sino de como se separa la información por hojas.

#--------------------------------------------------------------------------------------------
IMPORTANTE:
1. Usted no deberá realizar modificaciones en el codigo en ningun moemnto, la herramienta está diseñada para qeu toda la experiencia de uso sea desde la consola y no sea necesario modificar nada en los distintos archivos .py
que comforman el proyecto.

2. Depresentarse fallas por favor comuniquese con Alejandro Castrillon email: johanalejandro.castrillonrodriguez@medtronic.com uy especifique el fallo en el e-mail. La falla será atendida tan pronto como sea posible.
