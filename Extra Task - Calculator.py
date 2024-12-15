name = input("Hello! I am your favourite thing to use in math! My name is calculator! Yh! You use me everyday! Wanna play a game? Before that, tell me your name:")
print("Hello " , name , "Nice to meet you 😜🥰🩷🩷")
game = input("Do you wanna see how smart I am?")
if game == "yes" :
    print("Yay! Your so kind!")
else:
    print("Rude! I feel offended! Guess what! With that attitude of yours, your playing it anyway!")
num1 = int(input("Input any number of your choice:"))
num2 = int(input("Input another number of your choice:"))
answer = input("Would you like me to: add it? subtract it? multiply it? or divide it?")
if answer == "add it":
    print("Your answer is " , num1 + num2)
elif answer == "subtract it":
    print("Your answer is " , num1 - num2)
elif answer == "multiply it":
    print("Your answer is " , num1*num2)
else:
    print("Your answer is " , num1/num2)

print("See how smart I am 😝😜😝")
goodbye = input("Did I get your answer right?")
if goodbye == "yes":
    print("Yay! I was sure I did! I hope you enjoyed! Goodbye 👋😊🙌")
else:
    print("OH! I was for sure I got it right! If I didn't, my apoligies! Better luck next time I guess! Bye 😔👋")


