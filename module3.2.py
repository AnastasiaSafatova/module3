def send_email(massage, recipiend, sender = "university.help@gmail.com" ):
    if recipiend.find('@') and (recipiend.endswith('.com') or recipiend.endswith('.ru') or recipiend.endswith('net')):
        a_recipiend = True
    if sender.find('@') and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('net')):
        a_sender = True
    else:
        print(f'Невозможно отправить с адреса {sender} на адрес {recipiend}')


    if recipiend == sender:
        print('Нельзя отправить письмо самому себе')

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipiend}')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipiend}.')



send_email('Это сообщение для проверки связи', "vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')