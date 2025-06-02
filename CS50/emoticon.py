#this line can be access anywhere (global)
emo = "v.v"

#create a function main() that say(smt)
def main():
    global emo
    say("Anyone there?")
    emo = ":D"
    say("Supriseeeee")
    emo = ">:()"
    say("Wtf, you scared me!!!")



#create a function that when say(smt) it print smt on demand
def say(phrase):
    print(phrase + " " + emo)

# "phrase" will make the program run the the string we typed
main()
