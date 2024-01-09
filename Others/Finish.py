from Token import Token


class Finish:
    @staticmethod
    def finish():
        @Token.bot.message_handler(commands=['END'])
        def finishing(message):

            if message.from_user.first_name and message.from_user.last_name:
                mess = f'Congratulation, <b>{message.from_user.first_name} {message.from_user.last_name}!</b>&#127468;&#127463;\n'
            else:
                mess = f'Congratulation, <b>{message.from_user.first_name}!</b>&#127468;&#127463;\n'
            file_name = 'Text/Finish.txt'
            with open(file_name) as file_object:
                contents = file_object
                print(contents)

            Token.bot.send_message(message.chat.id, mess, parse_mode='html')
            Token.bot.send_message(message.chat.id, contents)
