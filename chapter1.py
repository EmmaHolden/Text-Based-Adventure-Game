from character import *
from utility import *
import random


def wake_up(player):
    print("You wake up in a dark, damp cell, your memory of the night before somewhat hazy.")
    print("You seem to remember being chased by the city guard.")
    print("As you sit in your cell, you have time to reflect on your life and how you ended up here.")
    move_on()
    player.set_crime()
    move_on()
    player.set_alignment()
    explore_cell(player)


def explore_cell(player):
    answered = False
    while not answered:
        clear()
        print("Your cell door is locked.")
        print(
            "From the little light in the room, you can see a table, a chair and another prisoner curled up sleeping"
            " next to the wall.\nYou can hear several guards outside your cell playing Goblin Rocks.\n")
        choice = input("Would you like to:\nA: Wake the prisoner.\nB: Search the cell.\nC: Call out to the guards.\n")
        if choice.lower() in ["a", "b", "c"]:
            answered = True
            clear()
            if choice.lower == "a":
                wake_prisoner(player)
            elif choice.lower == "b":
                search_cell(player)
            else:
                call_guards(player)


def wake_prisoner(player):
    print(
        "You whisper to the prisoner nearby.\nNo answer.\nYou try again, louder.\n'What do you want?' he asks.\nLooks "
        "like he's not a morning person.")
    answered = False
    while not answered:
        choice = input(
            "Do you:\nA: Ask him about himself.\nB: Ask what he knows about this place.\nC: Ask him how to escape.\n")
        if choice.lower() in ["a", "b", "c"]:
            clear()
            answered = True
            if choice.lower() == "a":
                print(
                    "The prisoner seems taken aback by your curiosity.\nHe tells you that his name is Rolph and that a "
                    "misunderstanding has brought him here.\n")
            elif choice.lower() == "b":
                print(
                    "The prisoner, who you learn is called Rolph, has little to tell you about where you are.\nHe "
                    "explains that he was captured by guards because of a misunderstanding, and was knocked out before "
                    "waking up here... several weeks ago.")
            else:
                print(
                    "The prisoner, who you find out is named Rolph, laughs at your question.\n'You think them lot out"
                    " there will just let us escape?\nNo, dear child.\nIt is always better to wait for the right time,"
                    " when fate and circumstances align.\n'")
            if player.social >= 5:
                print(
                    "Although Rolph asks you no questions in return, it is clear that he is somewhat charmed by"
                    " you.\nHe reaches into his pocket and hands you an orb.\n'I have no use for this,' he tells you.")
                player.rel_with_prisoner += 1
                player.increase_skill(skillincrease=1)


def search_cell(player):
    print(
        "You get to work quickly, combing the cell - somewhat blindly in the dark - for anything of interest.\nYou run "
        "your hands along the walls, around the table, under the chair.")
    if player.luck >= 5:
        print("You find an orb!")
        player.increase_skill(skillincrease=1)
        print(
            "You continue your search until a loud voice startles you.\n'That is my foot!' it says.\nIt's the voice of "
            "the other prisoner.")
    else:
        print(
            "Your fingers tremble as you come across a switch.\nAs you move your fingers away, a large metal spike "
            "comes flying out of the cell wall.\n")
        if player.dexterity >= 5:
            print("You manage to jump out of the way in time to avoid being impaled.")
        else:
            print(
                "You try to jump out of the way but you aren't quite quick enough. The spike catches your shoulder as"
                " it zooms past and you cry out in pain.")
            player.reduce_health(amount=2)
        print(
            "You hear the voice of the other prisoner.\n'You know, if you're trying to kill me, there are less "
            "messy ways.'")
        player.rel_with_prisoner -= 1
    print("'I'm Rolph by the way,' the prisoner says.")


def call_guards(player):
    print(
        "You call out as loudly as you can, over the sounds of laughter and general merriment coming from the guards "
        "table nearby.\nEventually, a guard appears at the bars.\n'What is it prisoner? Is the elf bothering "
        "you?'\n'I have a name,' says the elf. 'My name is Rolf.'\n'Whatever, elf.\n' the guard says.\nAs you look"
        " back at the prisoner, you notice, even in the dim light, two pointed ears poking out from his hood.\n")
    answered = False
    while not answered:
        choice = input(
            "Do you:\nA: Demand that both you and your cellmate be released instantly.\nB: Complain that you have "
            "been put in a cell with an elf.\nC: Ask if you can play a round of Goblin Rocks.\n")
        if choice.lower() in ["a", "b", "c"]:
            clear()
            answered = True
            if choice.lower() == "a":
                player.rel_with_prisoner += 2
                player.guard_rel -= 2
                print(
                    "The guard laughs at you.\n'Very funny, prisoner.\nGet back before I make you regret it.'\nThe "
                    "guard pushes you back with his club, more roughly than necessary, before turning on his heel "
                    "and returning to his game.\n'Rolph steps closer towards you.\n'Sometimes I wonder if humans are "
                    "brave or stupid, he says.'")
            if choice.lower() == "b":
                player.rel_with_prisoner -= 2
                player.guard_rel += 1
                print("'Not enough cells.\nYou'll have to take it up with the boss.\nAin't nothing to do with me.\n")
                answered = False
                while not answered:
                    choice = input("'Hey, want to play a round of goblin rocks?' he says.\nAnswer [y]es or [n]o.\n")
                    if choice.lower() == "y" or choice.lower() == "yes":
                        answered = True
                        clear()
                        player.guard_rel += 2
                        play_goblin_rocks(player)
                    elif choice.lower() == "n" or choice.lower() == "no":
                        answered = True
                        clear()
                        player.guard_rel -= 1
                        print(
                            "'Please yourself,' the guard says, before walking away.'\n'Probably a good idea,' says "
                            "Rolph. 'I can't imagine they play fair.'\n")
            if choice.lower() == "c":
                player.guard_rel += 1
                play_goblin_rocks(player)


def play_goblin_rocks(player):
    choices = ["princess", "orc", "wood nymph", "dragon", "ogre", "four tailed dog"]
    guard_ran_num = random.randint(0, 5)
    player_ran_num = random.randint(0, 5)
    print(
        f"The guard rolls the dice.\n'I got the {choices[guard_ran_num]},' he says, before handing the dice to"
        f" you.\nYou roll.\nIt's the {choices[player_ran_num]}.")
    if guard_ran_num > player_ran_num:
        print("You lose.\nThe guard reaches through the bars and punches you on the nose.\n")
        player.reduce_health(amount=2)
    elif player_ran_num > guard_ran_num:
        print('You win.\nThe guard mumbles under his breath before handing you an orb!')
        player.increase_skill(skillincrease=1)
    else:
        print("'A draw. Let's roll again.''")
        play_goblin_rocks(player)
    print(
        "'That was a good game, prisoner,' the guard says, before returning back to his group with a chuckle.'\n'You're"
        " very strange, even for a human,' Rolph says to you.")


