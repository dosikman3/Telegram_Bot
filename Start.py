from Token import bot
import gspread


class Start:
    @staticmethod
    def start():
        is_welcome_pinned = False  # Flag to track if the welcome message is already pinned

        @bot.message_handler(commands=['start'])
        def start(message):
            nonlocal is_welcome_pinned

            gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
            sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
            worksheet = sh.sheet1

            user_id = message.from_user.id
            user_first_name = message.from_user.first_name
            user_last_name = message.from_user.last_name

            user_exists = False
            values = worksheet.col_values(1)
            if str(user_id) in values:
                user_exists = True

            if not user_exists:
                worksheet.append_row([str(user_id), user_first_name, user_last_name])

            if user_last_name:
                mess = f'''Hello, <b>{user_first_name} {user_last_name}&#127468;&#127463</b> 👋;

Let's start with the Unit 1A Names:
<b>"Why did they call you that?"</b>

Click on the link to start this section /Unit1A👈'''
            else:
                mess = f'''Hello, <b>{user_first_name}&#127468;&#127463</b> 👋;

Let's start with the Unit 1A Names:
<b>"Why did they call you that?"</b>

Click on the link to start this section /Unit1A 👈'''

            bot.send_message(message.chat.id, mess, parse_mode='html')

            # Pin the welcome message if not pinned already
            if not is_welcome_pinned:
                pinned_message = '''
To view a list of all lessons, click /Lessons

And to view a list of all tests, click /Test
'''
                pinned_message_id = bot.send_message(message.chat.id, pinned_message).message_id
                bot.pin_chat_message(message.chat.id, pinned_message_id)
                is_welcome_pinned = True

                try:
                    # Adjust chat permissions to prevent unpinning by users
                    chat_id = message.chat.id
                    permissions = bot.get_chat(chat_id).permissions
                    permissions.can_pin_messages = False  # Disable users from pinning messages
                    permissions.can_change_info = False  # Disable users from changing chat info (including unpinning)
                    bot.set_chat_permissions(chat_id, permissions)
                except Exception as e:
                    print(f"Error adjusting chat permissions: {str(e)}")
