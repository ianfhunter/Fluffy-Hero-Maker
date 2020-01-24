from databases.dnd5.dnd5_spell_db import look_for_spell_by_name, get_number_of_spells_in_db, \
    get_all_spell_names_from_db, get_all_spell_names_of_level, get_random_spell, get_spells_of_school, \
    get_all_spells_of_class, get_all_spells_of_class_and_level, get_all_schools


def cli_display(spell):
    print("Spell name: " + spell.name)
    print("School: " + spell.school)
    print("Level: " + str(spell.level))
    print("Casting time: " + spell.casting_time)
    print("Range: " + spell.range)
    print("Duration: " + spell.duration)
    print("Components: " + spell.components)
    if spell.concentration != "":
        print("Concentration: " + spell.concentration)
    print("Description:\n" + spell.cli_description_string())
    if spell.upgrade != "":
        print("At higher levels:\n" + spell.upgrade)


def dnd_spell_display():
    print("For a specific spell, type 1, 2 to get all spell names in the database, 3 to get all spells of a certain "
          "level type, 4 for a random spell, 5 to get all spells of a certain school, 6 to get all spells of a certain"
          " class, 7 to get all spells of a certain class and level")
    choice = input()
    if choice == "1":
        print("Please give the name of the spell you are looking for:")
        spell_name = input().strip()
        spell = look_for_spell_by_name(spell_name)
        if spell is None:
            print("No spell found with name: {spell}".format(spell=spell_name))
        else:
            cli_display(spell)
    if choice == "2":
        print("The database contains " + str(get_number_of_spells_in_db()) + " spells.")
        print("The database contains the following spells: ")
        print(", ".join(get_all_spell_names_from_db()))
    if choice == "3":
        print("Choose a level")
        level = input().strip()
        spells = get_all_spell_names_of_level(int(level))
        if len(spells) == 0:
            print("There are no spell of level {level}".format(level=level))
        else:
            print(", ".join(spells))
    if choice == "4":
        cli_display(get_random_spell())
    if choice == "5":
        print("There are the following schools of magic: ")
        print(", ".join(get_all_schools()))
        print("Pick a school to find the spells of")
        school_choice = input().strip()
        spells = get_spells_of_school(school_choice)
        if len(spells) == 0:
            print("There are no spell of school {school_choice}".format(school_choice=school_choice))
        else:
            print(", ".join(spells))
    if choice == "6":
        print("Pick a class to find the spells associated with it")
        class_choice = input().strip()
        spells = get_all_spells_of_class(class_choice)
        if len(spells) == 0:
            print("There are no spell for the class {class_choice}".format(class_choice=class_choice))
        else:
            print(", ".join(spells))
    if choice == "7":
        print("Pick a class to find the spells associated with it")
        class_choice = input().strip()
        print("Choose a level")
        level_choice = input().strip()
        spells = get_all_spells_of_class_and_level(class_choice, level_choice)
        if len(spells) == 0:
            print("There are no spell for the class {class_choice} and level {level}".format(class_choice=class_choice, level=level_choice))
        else:
            print(", ".join(spells))
