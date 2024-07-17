def send_email(message, recipient,sender = "university.help@gmail.com"):
   print(message,recipient,sender)
   if '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
   elif sender == 'university.help@gmail.com'and sender != recipient:
    print (f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
   elif sender == recipient:
    print(f'Нельзя отправить письмо самому себе!')
   else:
     print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Почему не работаешь?', 'pumbahumba@mail.ru','rulka2mail.ru')
send_email('Иди работай!', 'pumbahumba@mail.ru','university.help@gmail.com')
send_email('Ты уволен!', 'university.help@gmail.com', 'university.help@gmail.com')
send_email('Надеюсь ты сдохнешь', 'university.helpgmail', 'university')
