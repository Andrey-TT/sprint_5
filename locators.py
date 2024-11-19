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
