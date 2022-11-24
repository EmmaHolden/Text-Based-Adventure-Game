from utility import *
import random


class Character:
    def __init__(self):
        self.name = create_character_name()
        character_stats = create_character_stats(self.name, total_points=20)
        self.rel_with_prisoner = 5
        self.guard_rel = 5
        self.max_energy = 5
        self.energy = 5
        self.max_health = 5
        self.health = 5
        self.alignment = "neutral"
        self.crime = "unknown"
        self.fitness = character_stats["Fitness"]
        self.magic = character_stats["Magic"]
        self.social = character_stats["Social"]
        self.dexterity = character_stats["Dexterity"]
        self.luck = character_stats["Luck"]
        self.prisoner_tied = True
        self.player_tied = True
        self.ghost_mode = False
        clear()
        print(
            f"{self.name}'s adventure is about to begin.\nAs you level up, you will be able to add points to your "
            f"skills.\n\nYou currently have {self.health} points of health.\nYou will lose health points when you take "
            f"damage.\nIf your health falls to zero, you will die.\nIf you die, you can continue playing in ghost "
            f"mode.\n\nYou also have {self.energy} points of energy.\nYou consume energy to do difficult"
            f" tasks.\nIf your energy falls too low, the actions you can take will be limited.")

    def set_alignment(self):
        alignment_chosen = False
        while not alignment_chosen:
            alignment = input(
                "Why did you commit your crime(s)?\nA: For good and selfless reasons.\nB: For my own sake, to benefit "
                "myself.\nC: For evil - I wanted others to suffer.\n")
            if alignment.lower() in ["a", "b", "c"]:
                clear()
                alignment_chosen = True
                if alignment.lower() == "a":
                    self.alignment = "good"
                    self.guard_rel += 2
                if alignment.lower() == "b":
                    self.alignment = "neutral"
                if alignment.lower() == "c":
                    self.alignment = "evil"
                    self.guard_rel -= 2
            else:
                print("Please choose A, B or C.")

    def set_crime(self):
        crime_chosen = False
        while not crime_chosen:
            crime = input(
                "You're a prisoner. What crime did you commit?\nA: Murder\nB: Thievery\nC: I got involved with"
                " politics. My side didn't win.\nD: Experimenting with forbidden magic.\nE: All of the above, "
                "and more, but you were caught for dodging taxes...\n")
            if crime.lower() in ["a", "b", "c", "d", "e"]:
                clear()
                crime_chosen = True
                if crime.lower() == "a":
                    self.crime = "murderer"
                    self.fitness += 5
                    print(
                        f"Your murderous tendencies have kept you in shape.\nYour strengths lie in physically "
                        f"overpowering others.\nYou have been given a bonus to fitness."
                        f" Your fitness is now {self.fitness}")
                elif crime.lower() == "b":
                    self.crime = "thief"
                    self.dexterity += 5
                    print(
                        f"You're quick. You're slippery.\nYou can go under the radar, undetected.\nYou have been given "
                        f"a bonus to dexterity. Your dexterity is now {self.dexterity}")
                elif crime.lower() == "c":
                    self.crime = "political"
                    self.social += 5
                    print(
                        f"Silver-tongued, you can be very convincing when you want to.\nYou are a master at getting "
                        f"others to do your bidding and keeping your hands clean.\nYou have been given a bonus to "
                        f"social and your social is now {self.social}")
                elif crime.lower() == "d":
                    self.crime = "magician"
                    self.magic += 5
                    print(
                        f"Power. Knowledge. Exploring the unknown. For some, the pull of magic is irresistable.\nYou "
                        f"have been given a bonus to magic and your magic is now {self.magic}")
                elif crime.lower() == "e":
                    self.crime = "lucky"
                    self.luck += 5
                    print(
                        f"An interesting life you have led.\nYou should probably have died several times by now, but"
                        f" somehow you just keep getting away.\nYou have been given a bonus to luck and now your"
                        f" luck is {self.luck}")
            else:
                print("Please choose A, B, C, D or E")

    def level_up(self):
        clear()
        if self.ghost_mode == False:
            self.max_health += 3
            self.health += 3
            self.max_energy += 3
            self.energy += 3
        num_skills = random.randint(2, 4)
        print(f"You have levelled up! You can increase {num_skills} of your skills!")
        for _ in range(0, num_skills):
            skill_chosen = False
            while not skill_chosen:
                choice = input(
                    f"\nWhich skill would you like to increase?\n[F]itness (currently {self.fitness})\n[M]agic"
                    f" (currently {self.magic})\n[D]exterity (currently {self.dexterity})\n[S]ocial "
                    f"(currently {self.social})\n[L]uck (currently {self.luck})\n")
                if choice.lower() in ["f", "m", "d", "s", "l"]:
                    skill_chosen = True
                    clear()
            if choice.lower() == "f":
                self.fitness += random.randint(2, 5)
                print(f"Your fitness is now {self.fitness}!")
            elif choice.lower() == "m":
                self.magic += random.randint(2, 5)
                print(f"Your magic is now {self.magic}!")
            elif choice.lower() == "s":
                self.social += random.randint(2, 5)
                print(f"Your social is now {self.social}!")
            elif choice.lower() == "d":
                self.dexterity += random.randint(2, 5)
                print(f"Your dexterity is now {self.dexterity}!")
            else:
                self.luck += random.randint(2, 5)
                print(f"Your luck is now {self.luck}!")
        if self.ghost_mode == False:
            print(f"\nYou now have {self.max_health} maximum health and {self.max_energy} maximum energy.")

    def increase_skill(self, skillincrease):
        skill_chosen = False
        while not skill_chosen:
            skill = input(
                f"You can increase a skill of your choice by {skillincrease}.\nWhich skill would you like to"
                f" increase? [F]itness, [M]agic, [S]ocial, [L]uck or [D]exterity?\n")
            if skill.lower() == "f":
                self.fitness += skillincrease
                print(f"Your fitness is now {self.fitness}\n")
                skill_chosen = True
            elif skill.lower() == "m":
                self.magic += skillincrease
                print(f"Your magic is now {self.magic}\n")
                skill_chosen = True
            elif skill.lower() == "s":
                self.social += skillincrease
                print(f"Your social is now {self.social}\n")
                skill_chosen = True
            elif skill.lower() == "l":
                self.luck += skillincrease
                print(f"Your luck is now {self.luck}\n")
                skill_chosen = True
            elif skill.lower() == "d":
                self.dexterity += skillincrease
                print(f"Your dexterity is now {self.dexterity}\n")
                skill_chosen = True

    def reduce_health(self, amount):
        if self.ghost_mode == False:
            self.health -= amount
            if self.health <= 0:
                self.ghost_mode = True
                self.max_health = 999
                self.health = self.max_health
                self.max_energy = 999
                self.energy = 999
                print(
                    "\nYOU HAVE DIED.\nYou will play the rest of the game on ghost mode.\nYou can continue playing "
                    "for the story, but you are now invincible.\nIf you don't want this, stop the game"
                    " and start again.\n")
            else:
                print(f"\nYou have lost {amount} points of health. Your health is now {self.health}.\n")

    def add_health(self, amount):
        if self.ghost_mode == False:
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\nYou have restored {amount} points of health. Your health is now {self.health}.\n")

    def reduce_energy(self, amount):
        if self.ghost_mode == False:
            self.energy -= amount
            if self.energy < 0:
                self.energy = 0
            print(f"\nYou have lost {amount} energy points. Your energy is now {self.energy}.\n")

    def add_energy(self, amount):
        if self.ghost_mode == False:
            self.energy += amount
            if self.energy > self.max_energy:
                self.energy = self.max_energy
            print(f"\nYou have restored {amount} energy points. Your energy is now {self.energy}.\n")


def create_character_name():
    name_created = False
    while not name_created:
        name = input("What is your character's name?\n")
        happy = input(f"\nAre you happy with the name: '{name}'?\nYou won't be able to change it again.\n")
        if happy.lower() == "yes" or happy.lower() == "y":
            clear()
            name_created = True
            return name


def create_character_stats(chosenname, total_points):
    character_stats_complete = False
    while not character_stats_complete:
        print(
            f"Now we need to create some stats for {chosenname}.\nYou have {total_points} points to spend in"
            f" total.\n\nThe stats are 'Fitness', 'Magic', 'Social', 'Dexterity', and 'Luck'.")
        character_stats = input_stats(total_points)
        values = character_stats.values()
        if sum(values) != total_points:
            clear()
            print(f"Looks like your values don't add up to {total_points}! Let's try again.")
            character_stats_complete = False
        else:
            clear()
            print("Okay, so your stats are:")
            print('\n'.join("{}: {}".format(k, v) for k, v in character_stats.items()))
            happy = input("\nIs this okay? You may not be able to change them again: ").lower()
            if happy.lower() == "yes" or happy.lower() == "y":
                character_stats_complete = True
                return character_stats
            else:
                clear()
                print("Okay. Let's start again.")
                character_stats_complete = False


def input_stats(total_points):
    fitness = 0
    magic = 0
    social = 0
    dexterity = 0
    luck = 0
    character_stats = {
        "Fitness": fitness,
        "Magic": magic,
        "Social": social,
        "Dexterity": dexterity,
        "Luck": luck,
    }
    for k in character_stats:
        stat_entered = False
        while not stat_entered:
            try:
                v = int(input(f"\nHow many points would you like to spend on {k} out of {total_points}?: "))
                if v < 0:
                    raise ValueError
                if v > total_points:
                    raise ValueError
            except ValueError:
                clear()
                print("It needs to be a positive number no bigger than the points you have available!")
            else:
                total_points -= v
                character_stats[k] = v
                stat_entered = True
        if total_points == 0:
            break
    return character_stats

