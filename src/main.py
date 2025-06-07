from intro import intro
from user import User
from round import countdown, play_round



def main():
    username, countdown_time = intro()
    new_user = User(username)
    continue_game = play_round(countdown_time)
    print(continue_game)
    

if __name__ == "__main__":
    main()