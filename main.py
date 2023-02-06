import helper.callOption as op
import helper.LoadData as ld

if __name__ == "__main__":
    menu = True
    token = input('Ingrese el Token de seguridad para acceder a los datos de SmartSheet: ')
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
            12. Tracker by CFN (as sufix)
            13. Cruzar Documento externo con Submission Plan
            14. Reportar Expected Submission Date omitidas
            15. Track no ID licenses
            16.External tracker for no ID
            17.Compare Expirations Dates (SP and DBs)
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
        elif option == 4:
            op.option_Planning(token)
        elif option == 5:
            op.option_submitted(token)
        elif option == 6:
            op.option_voucher(token)
        elif option == 7:
            op.option_Timelapse(token)
        elif option == 8:
            op.option_expired(token)         
        elif option == 9:
            op.cancel_criticalOP(token)           
        elif option == 10:
            op.CFN_WithdrawalOP(token)
        elif option == 11:
            op.gaps_option(token)
        elif option == 12:
            op.sufix_option(token)
        elif option == 13:
            op.track_manual(token)
        elif option == 14:
            op.MissedExpectedDAte(token)
        elif option == 15:
            op.planingRenewals(token)
        elif option == 16:
            op.compareNoID(token)
        elif option == 17:
            op.DatesComparation(token)
            
        else:
            print('Opción incorrecta')
            print('#-------------------------------')
    
    
    
    

        
        
        