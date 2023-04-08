import helper.callOption as op

if __name__ == "__main__":
    menu = True
    token = input('Ingrese el Token de seguridad para acceder a los datos de SmartSheet: ')
    menu = True
    while menu != False:
        try:
            option = input('''
            1. Tracker por CFN
            2. Tracker por SubOU
            3. Tracker por Número de Registro
            12. Tracker by CFN (as sufix)
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
            op.option_cfn(token)
        elif option == 2:
            op.option_SubOU(token)
        elif option == 3:
            op.option_reg(token)
        # elif option == 4:
        #     op.option_Planning(token)
        # elif option == 5:
        #     op.option_submitted(token)
        # elif option == 6:
        #     op.option_voucher(token)
        # elif option == 7:
        #     op.option_Timelapse(token)
        # elif option == 8:
        #     op.option_expired(token)         
        # elif option == 9:
        #     op.cancel_criticalOP(token)           
        # elif option == 10:
        #     op.CFN_WithdrawalOP(token)
        # elif option == 11:
        #     op.gaps_option(token)
        elif option == 12:
            op.sufix_option(token)
        # elif option == 13:
        #     op.track_manual(token)
        # elif option == 14:
        #     op.MissedExpectedDAte(token)
        # elif option == 15:
        #     op.planingRenewals(token)
        # elif option == 16:
        #     op.compareNoID(token)
        # elif option == 17:
        #     op.DatesComparation(token)
        # elif option == 18:
        #     op.approvalsReview(token)
            
        else:
            print('Opción incorrecta')
            print('#-------------------------------')