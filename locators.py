class TestLocators:
    # Поля ввода
    INPUT_NAME = "//label[text()='Имя']/following-sibling::input" # Поле ввода имени
    INPUT_EMAIL = "//label[text()='Email']/following-sibling::input" # Поле ввода почты
    INPUT_PASS = "//label[text()='Пароль']/following-sibling::input" # Поле ввода пароля в форме регистрации

    # Кнопки
    REGISTER_TEXT_BUTTON = "//*[contains(@class, 'Auth_link') and text() ='Зарегистрироваться']" # Текстовая кнопка зарегистрироваться в окне входа
    REGISTER_BUTTON = "//*[contains(@class, 'button_button') and text() ='Зарегистрироваться']" # Кнопка зарегистрироваться в форме регистрации
    ENTER_BUTTON = "//*[contains(@class, 'button_button') and text() ='Войти']" # Кнопка войти в окне входа
    ENTER_ACCOUNT_BUTTON = "//*[contains(@class, 'button_button') and text() ='Войти в аккаунт']" # Кнопка войти в аккаунт на главной странице
    PLACE_ORDER_BUTTON = "//*[contains(@class, 'button_button') and text() ='Оформить заказ']" # Кнопка Оформить заказ на главной странице
    PERSONAL_ACCOUNT_BUTTON = "//*[contains(@class, 'AppHeader_header') and text() ='Личный Кабинет']" # Кнопка личный кабинет на главной странице
    ENTER_TEXT_BUTTON = "//*[contains(@class, 'Auth_link') and text() ='Войти']" # Текстовая кнопка войти в окне регистрация
    EXIT_TEXT_BUTTON = "//*[contains(@class, 'Account_button') and text() ='Выход']" # Текстовая кнопка выйти в личном кабинете
    SAVE_BUTTON = "//*[contains(@class, 'button_button') and text() ='Сохранить']"  # Кнопка сохранить в личном кабинете
    CONSTRUCTOR_BUTTON = "//*[contains(@class, 'AppHeader_header') and text() ='Конструктор']"  # Кнопка конструктор
    BUNS_TEXT_BUTTON = "//*[contains(@class, 'text text_type_main-default') and text() ='Булки']"  # Текстовая кнопка булки в конструкторе
    SAUCES_TEXT_BUTTON = "//*[contains(@class, 'text text_type_main-default') and text() ='Соусы']"  # Текстовая кнопка соусы в конструкторе
    FILLINGS_TEXT_BUTTON = "//*[contains(@class, 'text text_type_main-default') and text() ='Начинки']"  # Текстовая кнопка начинки в конструкторе


    # Сообщения, надписи
    ERROR_PASS = "//*[contains(@class, 'input__error text_type_main-default')]" # Сообщение о неккоректином пароле
    ASSEMBLE_BURGER = "//*[contains(@class, 'text text_type_main-large mb-5 mt-10') and text() ='Соберите бургер']" # Надпись Соберите бургер
    LOGO_STELLAR_BURGERS = "//*[contains(@class, 'AppHeader_header__logo')]"  # Логотип бургерной
    BUNS_TEXT = "//*[contains(@class, 'text text_type_main-medium') and text() ='Начинки']" # Надпись булки в конструкторе
    SAUCES_TEXT = "//*[contains(@class, 'text text_type_main-medium') and text() ='Начинки']"  # Надпись соусы в конструкторе
    FILLINGS_TEXT = "//*[contains(@class, 'text text_type_main-medium') and text() ='Начинки']"  # Надпись начинки в конструкторе











#register_page_already_registered = "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']" #не понял зачем!

register_page_fields= "//input[@class='text input__textfield text_type_main-default']"
register_page_register_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
register_page_error = "//p[@class='input__error text_type_main-default']"
register_page_login_button = "//a[@class='Auth_link__1fOlj' and @href='/login']"


#Страница авторизации
login_page_email_field = "//input[@class='text input__textfield text_type_main-default' and @name='name']"
login_page_password_field = "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"
login_page_login_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
login_page_recover_password_button = "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"


#Главная страница
main_page_personal_account = "//a[@class='AppHeader_header__link__3D_hX' and .//p[text()='Личный Кабинет']]"
main_page_login_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
main_page_make_burger_text = "//h1[@class='text text_type_main-large mb-5 mt-10']"
main_page_select_sauce = ".//span[text()='Соусы']"
main_page_select_sauce_up = main_page_select_sauce + "/.."
main_page_select_filling = ".//span[text()='Начинки']"
main_page_select_filling_up = main_page_select_filling + "/.."
main_page_select_bun = ".//span[text()='Булки']"
main_page_select_bun_up = main_page_select_bun + "/.."

#Страница личный аккаунта
personal_account_save_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
personal_account_email_field = "//input[@class='text input__textfield text_type_main-default input__textfield-disabled']"
personal_account_exit_button = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"

#Страница забыли пароль
forgot_page_login_button = "//a[@class='Auth_link__1fOlj' and @href='/login']"

#Лого бургера и конструктор
constructor_button = "//p[@class='AppHeader_header__linkText__3q_va ml-2']"
burger_logo = "//a[@href='/']"

#Ожидамое значение для теста. Селект выбран
selected_this_one = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

#Ожидаемое значение для теста. Селект не выбран
selected_value_not_this = "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"
