from intro import intro
from user import User

def main():
    intro()
    new_user = User("Michael")
    print(User.high_scores)
    print(new_user.name)
    print(new_user.score)

    new_user.increase_score()
    new_user.record_run()
    print(User.high_scores)

if __name__ == "__main__":
    main()