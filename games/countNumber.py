from os import system
from random import randint

#this say function is the most important part of kids programming
#it uses the built in OSX say command to convert text to speech
def say(something):
    system('say "%s"' % something)

welcome_input = "Hi, Baby, Please input a number you would like to count."
print(welcome_input)
say(welcome_input)

Start_Number = 1
Max_Number = eval(input("Your Input? "))

bot_said = "OK. Let me start to count from 1 to %d" % Max_Number
say(bot_said)

not_solved = True
while not_solved:
    bot_count = "%d" % Start_Number
    print(bot_count)
    say(bot_count)

    if Max_Number > Start_Number:
        Start_Number +=1
    else:
        not_solved = False
        say("My Dear, I have done!")
