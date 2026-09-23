import time

while True:
   
    
    '''The Mystery of Bob:

        Description:

            _ A guy wakes up and doesn't remember his name 
            - The man (nameless guy) finds a missing person poster
            - He goes on with life
            - Five years later... he goes to a hotel and spots a familiar guy
            - Choice 1- he talks to the person and get a billion dollars and goes to become leader of Doofenfermds
            - Choice 2- he becomes poor and stays poor and he dies alone
            - You can play again'''


    #Main Story Line

    story='''The Mystery of Bob — Storyline

    A man wakes up one morning and realizes he can't remember his name or anything about his past. He walks around town trying to figure out who he is. While walking, he finds a missing-person poster with a picture that looks exactly like him. Confused, he decides to continue with his life without investigating.

    Five years later, he goes to a hotel and suddenly spots a person who looks very familiar. He feels like he has seen this person before, but he can't remember where. He now has to make a choice:

    Choice 1: Talk to the person.
    Choice 2: Ignore the person.
    (either 1 or 2)'''

    for letter in story:
        print(letter, end="")
        time.sleep(0.005)

    choices=input() 
    if choices=="1":
        print('''Choice 1

    Bob decides to talk to the familiar person. The person recognizes him immediately and reveals that they knew Bob before he lost his memory. Bob finally learns the truth about his past and discovers that he is connected to the Doofenfermds. As a reward for finding his way back, Bob receives one billion dollars and eventually becomes the leader of the Doofenfermds.''')


    elif choices=="2":
        print('''Choice 2

        Bob decides not to talk to the familiar person. He leaves the hotel and continues living his life without ever finding out who he really is. Over time, Bob becomes poor and struggles to survive. He stays poor for the rest of his life and eventually dies alone.''')

    else:
        print('''I am not falling for your trickeries. You can play again.''')  
        

    playagain=input("do you want to play again (say y or n)")
    if playagain=="n":
        break    
