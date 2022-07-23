from click import echo
from playsound import playsound



for i  in range(1,5):
 if i==3:
    playsound('./free.mp3')
 elif i > 3:
    print("greater than three")
 else:
    print("lesser than three")    