import helper.callOption as op

if __name__ == "__main__":
    menu = True
    while menu != False:
        try:
            option = input('''
            1. Tracker por CFN
            2. Tracker por SubOU
            3. Tracker por Número de Registro
            4. Tracker de planning review(fechas omitidas de submitted y Approved)
            5. Tracker de procesos Resagados(mas tiempo del esperado en Submitted)
            6. Tracker Missed Voucher
            7. Tracker por lapsos de tiempo(se da una fecha de inicio y de finalización)
            8. Tracker de elementos vencidos(Se omite Honduras y Rep. Dominicanda)
            9. Missed Critical communications(Cancell Renewal)
            10. Missed Critical communications (approved CFN Withdrawal)
            11. Gaps on DataBases Report
            Presione entre sin ningun texto para salir
            ingrese el número de la opción a utilizar: ''')
            option =int(option)
        except:
            if option == '':
                menu = False
                break
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
        elif option == 6:
            op.option_voucher()
            menu = False
        elif option == 7:
            op.option_Timelapse()
            menu = False
        elif option == 8:
            op.option_expired()
            menu = False
        elif option == 9:
            op.cancel_criticalOP()
            menu = False
        elif option == 10:
            op.CFN_WithdrawalOP()
            menu = False
        elif option == 11:
            op.gaps_option()
            menu = False
        else:
            print('Opción incorrecta')
            print('#-------------------------------')

        
        
        