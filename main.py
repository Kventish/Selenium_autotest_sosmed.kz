import tests.main_page as main_page
import tests.service as service
import tests.Assistance as Assistance
import tests.Check_Up as Check_Up
import tests.doctors as doctors
import tests.Preyskurant as Preyskurant
import tests.Mc_Tole_Bi as Mc_Tole_Bi
import tests.Mc_Dostyk as Mc_Dostyk
import tests.cart as cart
import time

functions_array = [main_page.header, main_page.body, main_page.footer,service.test,Assistance.assistance,Check_Up.stock,Check_Up.programm,doctors.docktors_main,doctors.doctor_page,Preyskurant.preyskurant,Mc_Tole_Bi.button_check,Mc_Dostyk.button_check,cart.check_button]
for function in functions_array:
    function()
    time.sleep(5)