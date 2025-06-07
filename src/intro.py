TITLE_CARD = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗     ██╗██╗██╗    ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗    ██║██║██║    ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝    ██║██║██║    ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗    ██║██║██║    ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║    ██║██║██║    ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝╚═╝    ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                                        
██╗      ██████╗ ██╗    ██╗███████╗██████╗     ██╗██╗██╗    ██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗    ██║██║██║    ██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝    ██║██║██║    ███████║██║██║  ███╗███████║█████╗  ██████╔╝
██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗    ██║██║██║    ██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║    ██║██║██║    ██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝╚═╝    ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                        
"""

def classic_or_beat_the_clock() -> int:
    """Asks user to choose game mode then returns related countdown time value."""

    game_mode = input("\nPlay CLASSIC or BEAT THE CLOCK? Type 'c' or 'b':\n> ").lower()

    while game_mode not in ["c", "b"]:
        game_mode = input("ERROR || Please enter either:\n●'c' for CLASSIC\n●'b' for BEAT THE CLOCK\n\n> ").lower()

    return 60 if game_mode == 'c' else 10

def intro() -> int:
    """Prints title card, explains game, and returns countdown time based on game mode."""

    print(TITLE_CARD)
    print("A bitterly addictive game of popularity ranking based on Instagram follower counts.".center(100))
    print()
    print("The data is based on Instagram counts from June of 2025.".center(100))

    print()
    username = input("Enter your name:\n> ")

    countdown_time = classic_or_beat_the_clock()
    return username, countdown_time