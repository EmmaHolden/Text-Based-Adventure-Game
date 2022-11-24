from utility import *
from character import *


def guards_attacked(player):
    print(
        "Before you can answer Rolph, you hear the laughter and shouting from the guards table suddenly "
        "change.\nInstead, the sound of confusion and fear, followed by guttural screams of pain.\nThe cell"
        " lights up and you turn to see that Rolph has conjured three orbs of light which hang above you "
        "both.\nYou exchange solemn looks.\nRolph holds up his hands and closes his eyes, as if "
        "concentrating.\nThere is the screeching sound of metal on metal and the cell door slides open.")
    answered = False
    while not answered:
        choice = input(
            "Do you:\nA: Ask Rolph how he learned such powerful magic.\nB: Ask Rolph why he stayed in the cell this "
            "whole time if he could have escaped.\nC: Ask Rolph what he thinks has happened to the guards. ")
        if choice.lower() in ["a", "b", "c"]:
            answered = True
            clear()
            if choice.lower() == "a":
                if player.magic >= 3:
                    print(
                        "'A fellow apprentice of the arcane,' he says, seemingly impressed.\nHe lifts his finger to"
                        " your temple and you feel your mind expand.")
                    player.magic += 1
                    player.rel_with_prisoner += 2
                    print(f"Your magic has increased by 1 and is now {player.magic}.")
                else:
                    print("'You would not understand,' Rolph says. 'Your mind is not capable of such power.'")
            elif choice.lower() == "b":
                print(
                    "'You think I could have just walked past the guards and they would have waved me off?' he"
                    " says.\n'I was starting to hope you were intelligent.'")
            else:
                print(
                    "'I don't know, but it doesn't sound like they just got tired and went to bed, does it? Something "
                    "is wrong,' Rolph says.")
            find_guards(player)


def find_guards(player):
    move_on()
    print(
        "You walk slowly out of the cell towards the table.\nAs you approach, you see six bodies of dead guards on "
        "the floor.\nAbove them lurks a dark, hooded creature with scary black hands.\n'A ghast,' says Rolph. 'It's "
        "consumed their souls.'\nYou look down again at the guards, their eyes vacant and blank. The ghast swoops"
        " towards you.")
    move_on()
    player.level_up()
    encounter_ghast(player)


def encounter_ghast(player):
    answered = False
    while not answered:
        choice = input(
            "Would you like to:\nA: Fight the ghast.\nB: Cast a spell on the ghast.\n C: Hide from the ghast. ")
        if choice.lower() in ["a", "b", "c"]:
            answered = True
            clear()
            if choice.lower() == "a":
                fight_ghast(player)
            if choice.lower() == "b":
                cast_spell_ghast(player)
            if choice.lower() == "c":
                hide_ghast(player)


def fight_ghast(player):
    print(
        "You run at the ghast at full speed, hitting, kicking, biting.\nTry as you might, you just can't make contact"
        " with it.\nYour attack has no effect.\n")
    player.reduce_energy(amount=2)
    if player.fitness >= 6:
        print(
            "The ghast turns to you, its long black hand extended. As it reaches forward into your chest, you feel as"
            " if your whole body is filled with ice.\nAs it spreads, you grow weary but manage to resist"
            " and avoid injury.")
        player.reduce_energy(amount=1)
        prisoner_fights_back(player)
    else:
        ghast_attacks_player(player)


def cast_spell_ghast(player):
    if player.magic >= 5:
        print("You focus your mind to cast a spell.")
        player.reduce_energy(amount=1)
        answered = False
        while not answered:
            choice = input("Would you like to cast a [w]ater, [l]ightning, [f]ire or [a]ir spell?")
            if choice.lower() in ["w", "l", "f", "a"]:
                answered = True
                clear()
                if choice.lower() == "w":
                    print(
                        "You conjure a rising whirlpool of water, which you push towards the ghast.\nIt doesn't seem "
                        "to do much.\nThe ghast retaliates, knocking you over with a powerful magical force.")
                    player.reduce_health(amount=1)
                elif choice.lower() == "l":
                    print("You conjure a bolt of lightning which hits the air ghast, causing it to shriek in pain.")
                elif choice.lower() == "f":
                    print(
                        "You conjure a ball of flames which you push towards the ghast.\nIt reacts quickly, pushing "
                        "the fireball back to you.\nYou fall backwards as your own magic burns you.")
                    player.reduce_health(amount=2)
                else:
                    print(
                        "You conjure a billowing whirlwind of air and push it towards the ghast.\nIt doesn't seem to"
                        " hurt it.\nIn fact... the ghast seems more energized than ever, as it retaliates, knocking "
                        "you down with a powerful magical force.")
                    player.reduce_health(amount=3)
                prisoner_fights_back(player)
    else:
        print(
            "You try to focus your mind to cast a magic spell but you are not powerful. A spark ignites in your hand"
            " and is extinguished immediately.")
        player.reduce_energy(amount=2)
        ghast_attacks_player(player)


def hide_ghast(player):
    player.rel_with_prisoner -= 2
    if player.dexterity >= 6:
        print(
            "You look back at Rolph and give him a solemn nod before moving off to hide effortlessly in the shadows."
            " Rolph shoots you a pained look as you retreat.")
        prisoner_fights_back(player)
    else:
        print(
            "Rolph shoots you a look of betrayal as he watches you sneak away. Unfortunately, the hiding places are "
            "scarce and you are unable to hide yourself in the shadows.")
        ghast_attacks_player(player)


def ghast_attacks_player(player):
    answered = False
    while not answered:
        choice = input(
            "The ghast glides towards you, a long, shadowy arm extended.\nIts arm reaches out to you and penetrates "
            "your chest.\nYour body twiches in pain as the cold runs through your body.\nDo you:\nA: Physically "
            "resist\nB: Mentally resist\n")
        if choice.lower() in ["a", "b"]:
            clear()
            answered = True
            if player.energy >= 2:
                if choice.lower() == "a":
                    if player.fitness >= 5 or player.dexterity >= 5:
                        print("You cry out as you struggle against the air ghast.\nYou avoid injury.")
                    else:
                        print("You try to resist but the pain overwhelms you.\nYou cry out, dropping to your knees.")
                        player.reduce_health(amount=1)
                elif choice.lower() == "b":
                    if player.magic >= 5 or player.social >= 5:
                        print("You focus your mind to push away the pain.\nYou manage to avoid injury.")
                    else:
                        print(
                            "You try to focus your mind to push away the pain, but it is too much.\nYou cry out and"
                            " drop to your knees.")
                        player.reduce_health(amount=1)
            else:
                print("You are too tired to resist.\nThe pain overwhelms you.")
                player.reduce_health(amount=2)
            player.reduce_energy(amount=2)
    prisoner_fights_back(player)


def prisoner_fights_back(player):
    if player.rel_with_prisoner > 6:
        print("Rolph reacts quickly.\nHe chants a spell and you are healed.")
        player.add_health(amount=3)
    else:
        print("Rolph reacts quickly.\nHe chants loudly and gestures wildly, as spells fly through the air.")
        move_on()
    print(
        f"The ghast tackles Rolph to the ground.\nRolph gasps as the life drains from him.\nIn his last breath,"
        f" he whispers,'{player.name}...' before his eyes glaze over.\nThe ghast feasts upon Rolph's body as you "
        f"look on, horrified.")
