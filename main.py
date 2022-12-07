import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr
import helper.callOption as op
import pandas as pd

if __name__ == "__main__":
    menu = True
    while menu != False:
        try:
            option = input('''1. Tracker por CFN
            2. Tracker por SubOU
            3. Tracker por Número de Registro
            4. Tracker de planning review(fechas omitidas de submitted y Approved)
            5. Tracker de procesos Resagados(mas tiempo del esperado en Submitted)
            Presione entre sin ningun texto para salir
            ingrese el número de la opción a utilizar: ''')
            option =int(option)
        except:
            if option == '':
                menu = False
            else:
                print('Opción invalida')
                print('#-------------------------------')
        if option == 1:
            op.option_cfn()
            menu = False
        elif option == 2:
            op.option_SubOU()
            menu = False
        elif option == 3:
            op.option_reg()
            menu = False
        elif option == 4:
            op.option_Planning()
            menu = False
        elif option == 5:
            op.option_submitted()
            menu = False
        else:
            print('Opción incorrecta')
            print('#-------------------------------')

        
        
        