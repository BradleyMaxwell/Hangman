
def hangmanState (wrongGuesses):
    states = {
        0: """--------\n|      |\n|\n|\n|\n|""",
        1: """--------\n|      |\n|      O\n|\n|\n|""",
        2: """--------\n|      |\n|      O\n|      |\n|\n|""",
        3: """--------\n|      |\n|      O\n|     \|\n|\n|""",
        4: """--------\n|      |\n|      O\n|     \|/\n|\n|""",
        5: """--------\n|      |\n|      O\n|     \|/\n|     /\n|""",
        6: """--------\n|      |\n|      O\n|     \|/\n|     / \ \n|"""
    }

    print(states[wrongGuesses])

hangmanState(6)


    