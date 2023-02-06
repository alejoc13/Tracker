import helper.callOption as op
import helper.LoadData as ld

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
            op.option_cfn()
        elif option == 2:
            op.option_SubOU()
        elif option == 3:
            op.option_reg()
        elif option == 4:
            op.option_Planning()
        elif option == 5:
            op.option_submitted()
        elif option == 6:
            op.option_voucher()
        elif option == 7:
            op.option_Timelapse()
        elif option == 8:
            op.option_expired()         
        elif option == 9:
            op.cancel_criticalOP()           
        elif option == 10:
            op.CFN_WithdrawalOP()
        elif option == 11:
            op.gaps_option()
        elif option == 12:
            op.sufix_option()
        elif option == 13:
            op.track_manual()
        elif option == 14:
            op.MissedExpectedDAte()
        elif option == 15:
            op.planingRenewals()
        elif option == 16:
            op.compareNoID()
        elif option == 17:
            op.DatesComparation()
            

        else:
            print('Opción incorrecta')
            print('#-------------------------------')
    
    
    
    

        
        
        