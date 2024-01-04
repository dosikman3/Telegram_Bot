from Token import bot
from Start import Start
from Unit1A import Unit1A
from Unit1B import Unit1B
from Unit2A import Unit2A
from Unit2B import Unit2B
from Unit3A import Unit3A
from Unit3B import Unit3B
from Practical_English import Practical
from Unit4A import Unit4A
from Unit4B import Unit4B
from Unit5A import Unit5A
from Unit5B import Unit5B
from Unit6A import Unit6A
from Unit6B import Unit6B
from Unit7A import Unit7A
from Unit7B import Unit7B
from Finish import Finish
from Help import Help
from Test import Test

if __name__ == '__main__':
    while True:
        try:
            start = Start()
            start.start()

            unit1A = Unit1A()
            unit1A.unit1A()

            unit1B = Unit1B()
            unit1B.unit1b()

            unit2A = Unit2A()
            unit2A.unit2a()

            unit2B = Unit2B()
            unit2B.unit2b()

            unit3A = Unit3A()
            unit3A.unit3a()

            unit3B = Unit3B()
            unit3B.unit3b()

            practical = Practical()
            practical.practical()

            unit4A = Unit4A()
            unit4A.unit4a()

            unit4B = Unit4B()
            unit4B.unit4b()

            unit5A = Unit5A()
            unit5A.unit5a()

            unit5B = Unit5B()
            unit5B.unit5b()

            unit6A = Unit6A()
            unit6A.unit6a()

            unit6B = Unit6B()
            unit6B.unit6b()

            unit7A = Unit7A()
            unit7A.unit7a()

            unit7B = Unit7B()
            unit7B.unit7b()

            finish = Finish()
            finish.finish()

            helper = Help()
            helper.help()

            tester = Test()
            tester.test()

            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
