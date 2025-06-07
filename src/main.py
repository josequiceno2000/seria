from intro import intro
from user import User
from round import countdown



def main():
    countdown_time = intro()
    countdown(countdown_time)
    

if __name__ == "__main__":
    main()