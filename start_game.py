import random
from time import sleep 
from msvcrt import kbhit, getch
from os import system as command

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"
BG_WHITE = "\033[47m"

characters_encountered = {}  
character_encounters = {}
character_levels = {"леший": 1, "фея": 1, "дракон": 1, "мачеха": 1, "светлячки": 1, "водяной":1}

def encounter_glowworn():
    textglowworn= """\nВы увидели мерцание в нескольких метрах от вас, и отправились на свет.
Оказалось, что он исходит от ядовитых светлячков.\n"""
    type(textglowworn)
    if character_encounters.get("светлячки"):
        
        character_levels["светлячки"] += 1
        levelglowworn="""Эти светлячки более токсичны и ядовиты.Уровень ядовитости светлячков:""",
        character_levels["светлячки"]
        type(levelglowworn)
        choice = input("\nХотите узнать интересный факт о светлячках? (Нажмите 1 если 'да'): ")
        if choice.lower() == "1":
          factglowworn= """Они излучают плохую энергетику и если человек дышит одим воздухом с
светлячкками дольше 3 минут он впадает в депрессию.\n"""
        type(factglowworn)
    else:
        character_encounters["светлячки"] = True
    print("1. Применить медицинскую маску")
    print("2. Использовать сачек нейтрализатор")

    choice = input("Выберите действие: ")
    
    if choice == "1":
        print("Вы применили медицинскую маску и спокойно прошли мимо светлячков.")
    elif choice == "2":
        print("Вы ловите всех светлячков в сачек и они засыпают!")
    else:
        print("Вы выбрали неверное действие,  светлячки отравили вас..."
              "Вы впали в глубочайшую депрессию и задохнулись в своих слезах!")
        exit_game()

def encounter_leshy():
    textleshego ="""\nВы внезапно слышите шум и ворчание.Из-за деревьев выходит Леший.
Он выглядит враждебно и стоит на вашем пути к замку.\n"""
    type(textleshego)
    if character_encounters.get("леший"):
        character_levels["леший"] += 1
        leshilevel="""Этот леший опаснее предыдущего!! Уровень лешего:""",
        character_levels["леший"]
        type(leshilevel)
        choice = input("\nХотите узнать интересный факт о лешем? (Нажмите 1 если 'да'): ")
        if choice.lower() == "1":
            factleshego="""Лешие — это сказочные существа, которые обитают в лесах.
Они могут утащить тебя в глубь леса из которого невозможно выбраться.\n"""
            type(factleshego)
    else:
        character_encounters["леший"] = True
    print("1. Использовать шапку невидимку")
    print("2. Использовать эликсир уменьшения")

    choice = input("Выберите действие: ")
    
    if choice == "1":
        print("Вы используете шапку невидимку и ускользаете от лешего!")
    elif choice == "2":
        print("Вы используете эликсир уменьшения. Этот леший становится размером с мизинец!")
    else:
        print("Вы выбрали неверное действие, леший утащил вас в болото!")
        exit_game()

def encounter_fairy():
    textfairy="""\nВы идете по узкой тропинке и на вашем пути появляется опасная и хитрая фея\n"""
    type(textfairy)
    if character_encounters.get("фея"):
        character_levels["фея"] += 1
        levelfairy="""Эта фея куда хитрее предыдущей! Уровень феи:""",
        character_levels["фея"]
        type(levelfairy)
        choice = input("Хотите узнать интересный факт о фее?(Нажмите 1 если 'да'): ")
        if choice.lower() == "1":
            factfei="""Феи на твоем пути очень похожи на бабочек, но это их прикрытие. 
На самом деле феи способны превратить тебя в гусеницу!\n"""
            type(factfei)
    else:
        character_encounters["фея"] = True
    print("1. Подарить фее новые туфельки")
    print("2. Использовать эликсир сна")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы дарите фее новые туфельки и откупаетесь от нее!")
    elif choice == "2":
        print("Вы используете эликсир сна и усыпляете фею!")
    else:
        print("Вы выбрали неверное действие, фея вас заколдовала!")
        exit_game()

def encounter_vodanoi():
    textvodanoi="""\nВы идете и чувствуете очень резкий запах, он исходит от болота в котором сидит страшный водяной\n"""
    type(textvodanoi)
    if character_encounters.get("водяной"):
        character_levels["водяной"] += 1
        levelvodanoi="""Этот водяной еще сташнее! Уровень водяного:""",
        character_levels["водяной"]
        type(levelvodanoi)
        choice = input("\nХотите узнать интересный факт о водяном?(Нажмите 1 если 'да'): ")
        if choice.lower() == "1":
            factvodanoi="""Тело Водяного опутывает тина, а ноги ему заменяет рыбий хвост!
Эти водяные привлекают жертв ультразвуком...\n"""
            type(factvodanoi)
    else:
        character_encounters["фея"] = True
    print("1. Применить барьерную каску")
    print("2. Использовать стрелы")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы применяете барьерную каску и без проблем удаляетесь от водяного!")
    elif choice == "2":
        print("Вы используете стрелы и убиваете этого водяного!")
    else:
        print("Вы выбрали неверное действие, фея вас заколдовала!")
        exit_game()

def encounter_dragon():
    textdragon="""\nНа вас подул сильный ветер, и вы увидели дракона в небе. Он летит прямо на вас!\n"""
    type(textdragon)
    if character_encounters.get("дракон"):
        character_levels["дракон"] += 1
        leveldragon="""Он еще больше чем прошлый дракон!! Уровень дракона:""", 
        character_levels["дракон"]
        type(leveldragon)
        choice = input("\nХотите узнать интересный факт о здешних драконах? (Нажмите 1 если 'да'): ")
        if choice.lower() == "1":
         factdragon="""Драконы в этой местности трехкрылые и четырехглавые. С ними нужно быть предельно осторожным.\n"""
         type(factdragon)
     
    else:
        character_encounters["дракон"] = True
    print("1. Использовать меч")
    print("2. Сбежать на ковре-самолете")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Вы используете меч и сильно раните дракона!")
    elif choice == "2":
        print("Вы сбегаете на ковре-самолете от дракона на 100000000 метров!")
    else:
        print("Вы выбрали неверное действие, дракон атакует вас!")
        exit_game()

def encounter_mather():
    textmather="""\nВы находитесь на развилке, и там к вам выходит злобная мачеха принцессы!\n"""
    type(textmather)
    if character_encounters.get("мачеха"):
        levelmather="""Она ходит за тобой по пятам, будь осторожнее!!\n"""
        type(levelmather)
    else:
        character_encounters["мачеха"] = True
    print("1. Использовать плащ для маскировки")
    print("2. Использовать сапоги скороходы")

    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы используете плащ и незаметно сбегаете от мачехи!")
    elif choice == "2":
        print("Вы сбегаете очень быстро с помощью сапогов скороходов!")
    else:
        print("Вы выбрали неверное действие, мачеха вас отравила!\n")
        exit_game()

def exit_game():
    print(f"{GREEN}Игра завершена из-за неверного выбора.{RESET}")
    print(f"{GREEN}Спасибо за игру!{BOLD}")
    exit()

def type(text: str, name: str = None) -> None:
    for letter in text:
        if kbhit():
            key = getch()
            
            if key == b'\r':
                command("cls")
                print(text)
            break

        print(letter, end="", flush=True)
        sleep(0.025)

def play_game():
    text = f"""{BG_WHITE}{BLACK}Добро пожаловать в игру 'Спаси принцессу из замка или погибни в осиновом лесу'!\n
    Вокруг вас лес. Вы находитесь в нескольких милях от замка, где вас ждет принцесса.Она была заточена там 
    своей мачехой, которая из за своей зависти силой удерживает принцессу в замке.Злобная мачеха с помощью 
    своего осинового кола превратила всех жителей осинового леса в злодеев,чтобы принцесса уж точно не 
    сбежала и никто не смог подобраться к замку. Вы готовы на риск ради спасения прекрасной принцессы?\n
    На вашем пути будут встречаться злодеи, с которыми вы должны побороться ради нее.
    Не переживайте! У вас в инвентаре есть все, чтобы справиться со злодеями.
    Вам предстоит истребить 4 вида персонажей, чтобы добраться до замка с принцессой.
    Мы в вас верим!\n
    Если вы выберите предмет, которого нет в инвентаре - игра, к сожалению, закончится.{RESET} \n"""
    type(text)
    
    princess_saved = False

    while not princess_saved and len(characters_encountered) < 4:

        enemy = random.choice(["леший", "фея", "дракон", "мачеха", "светлячки"])

        if enemy not in characters_encountered:
            characters_encountered[enemy] = True
        
        if enemy == "леший":
            encounter_leshy()
        elif enemy == "фея":
            encounter_fairy()
        elif enemy == "дракон":
            encounter_dragon()
        elif enemy == "мачеха":
            encounter_mather()
        elif enemy == "светлячки":
            encounter_glowworn()
        elif enemy == "водяной":
            encounter_vodanoi()

        if len(characters_encountered) < 4:
            print(f"{RED}Вам встретился {len(characters_encountered)} персонаж...{RESET}")

        if len(characters_encountered) == 4:
            princess_saved = True
            pobeda ="""\n Вот вы и одолели всех злодеев на своем пути!!
После множества приключений в осиновом лесу вы, наконец, достигаете замка, где принцесса была заключена.
Как только вы входите в замок, цепи которыми была скованна принцесса растворяются.Вы спасли ее из рук злой мачехи!
Ваша мужественная история становится легендой, и вы и принцесса живете долго и счастливо.
Поздравляю, вы победили в игре!"""
            type(pobeda)

    pozdravlenie=f"""\n{BLUE}Ты лучший герой! Спасибо за игру!{RESET}"""
    type(pozdravlenie)
play_game()