import main_page
import service
import Assistance
import Check_Up

#Вызов тестирования шапки главной страницы страницы
main_page.header()

# #Вызов тестирования тела главной страницы
main_page.body()

# #Вызов тестирования футера главной страницы
main_page.footer()

#Вызов тестирования услуг и добавление в корзину
service.test()

#Вызов тестирования модального окна страницы Ассистанс
Assistance.assistance()

#Вызов тестирования модального окна страницы Акции
Check_Up.stock()

#Вызов тестирования модального окна страницы Программы
Check_Up.programm()