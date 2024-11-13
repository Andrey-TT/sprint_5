import string
import random

new_name = ''.join(random.choices(string.ascii_lowercase, k=7))
new_email = ''.join(random.choices(string.ascii_lowercase, k=7)) + '@yandex.ru'
new_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=6))
fail_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=5))
