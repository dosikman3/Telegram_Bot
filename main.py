from Token import Token
from Others import Start
from Unit1 import Unit1A
import Unit1.Unit1B
from Unit2 import Unit2A
from Unit2 import Unit2B
from Unit3 import Unit3A
from Unit3 import Unit3B
from Practical import Practical_English
from Unit4 import Unit4A
from Unit4 import Unit4B
from Unit5 import Unit5A
from Unit5 import Unit5B
from Unit6 import Unit6A
from Unit6 import Unit6B
from Unit7 import Unit7A
from Unit7 import Unit7B
from Others import Finish
from Others import Help
from Others import Test

if __name__ == '__main__':
    while True:
        try:
            start = Start.Start
            start.start()

            unit1A = Unit1A.Unit1A
            unit1A.unit1A()

            unit1B = Unit1.Unit1B.Unit1B()
            unit1B.unit1b()

            unit2A = Unit2A.Unit2A
            unit2A.unit2a()

            unit2B = Unit2B.Unit2B
            unit2B.unit2b()

            unit3A = Unit3A.Unit3A
            unit3A.unit3a()

            unit3B = Unit3B.Unit3B
            unit3B.unit3b()

            practical = Practical_English.Practical
            practical.practical()

            unit4A = Unit4A.Unit4A
            unit4A.unit4a()

            unit4B = Unit4B.Unit4B
            unit4B.unit4b()

            unit5A = Unit5A.Unit5A
            unit5A.unit5a()

            unit5B = Unit5B.Unit5B
            unit5B.unit5b()

            unit6A = Unit6A.Unit6A
            unit6A.unit6a()

            unit6B = Unit6B.Unit6B
            unit6B.unit6b()

            unit7A = Unit7A.Unit7A
            unit7A.unit7a()

            unit7B = Unit7B.Unit7B
            unit7B.unit7b()

            finish = Finish.Finish
            finish.finish()

            helper = Help.Help
            helper.help()

            tester = Test.Test
            tester.test()

            Token.bot.polling(none_stop=True)

        except Exception as e:
            print(e)
