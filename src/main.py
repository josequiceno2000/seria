from intro import intro
from user import User
from round import countdown



def main():
    username, countdown_time = intro()
    new_user = User(username)
    
    

if __name__ == "__main__":
    main()