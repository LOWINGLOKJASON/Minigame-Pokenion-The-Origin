#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/qoyaqadwmt-lowinglokjason
#****************************************************************

# Packages
import time
import numpy as np
import random as random

# Rooms with informational greetings
bedroom = "In the morning, you woke up in your bedroom on the 5th floor of the apartment; you see there is no one on the street, and you are running out of food. You decide to go outside to find out what's happening..."
window = "You didn't notice that your room is on the 5th floor. But it's too late and you fall from the window."
door = "You observe the common corridor is quiet, you can go down by elevator or stairs. But it seems the elevator doesn't work..."
elevator = "The elevator doesn't have the power."
stairs = "After a moment of walks, you reach the ground."
mystery_place = "The silence spread along the street but you a mystery facility...a girl is standing over there...Meanwhile, you find there is a Celery nearby your feet..."
final_stage = "You walk inside the place, you see it's an empty space with nothing but a purple thing..."
look_closer = "You gently walk towards the purple thing and you find it is..."

# Characters
npc_1 = "Clary"
npc_2 = "Evil Minion"
npc_3 = "Minion"

# Status indiactors and items
health = 100
wallet = 0
bag = []
celery = "Celery"
minion = "Minion"
computer_choice = np.array([0, 1, 2])
minion_health = 5

# Game Introuction
while True:
  print("Welcome to play the game called 'Pokénion--The Origin'")
  play = input("Would you like to play?(y/n)\n")
  if play == "Y" or play == "y":
    print("Let's go!")
    time.sleep(1)
    break
  elif play == "N" or play == "n":
    print("Game Over!")
    exit()
  else:
    print("Invalid input. Please enter again!")
    time.sleep(2)
    continue

while True:
  # Room 1: Bedroom
  print(bedroom)
  time.sleep(1)
  print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
  time.sleep(1)
  # Interaction 1: Window or Door
  user_choice_1 = input("Which way will you choose to go out?\nPress [1] to jumped out of the window\nPress [2] to walk to the door\n")
  # Room 2: Window
  # Answer 1: Window (Game Over)
  if user_choice_1 == "1":
    print(window)
    time.sleep(2)
    print("You die! Game Over!")
    health -= 100
    time.sleep(1)
    print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
    exit()
  # Answer 1: Door (Continue)
  if user_choice_1 == "2":
    print("You successfully go out from your flat unit!")
    time.sleep(1)
    print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
    time.sleep(2)
    
    # Room 3: Door
    while True:
      print(door)
      time.sleep(1) 
      # Interaction 2: Stair or Elevator
      user_choice_2 = input("Which way will you choose to go down?\nPress [1] to walk the stairs\nPress [2] to use the elevator\n")
      # Room 4: Stair
      # Answer 2: Stair (Continue)
      if user_choice_2 == "1":
        print(stairs)
        time.sleep(1)
        print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
        time.sleep(2)
        
        # Room 5: Mystery Place
        while True:
          print(mystery_place)
          time.sleep(1)
          # Interaction 3: Talk, Leave or Celery
          user_choice_3 = input("(What should I do?)\nPress [1] to talk to that girl\nPress [2] to leave the place as soon as possible\nPress [3] to pick a Celery\n")
          # Answer 3: Talk (Continue)
          if user_choice_3 == "1":
            print(npc_1,": Welcome! Nice to meet you; I am",npc_1,".")
            # Interaction 4: Name Input (Continue)
            name = input("'What is your name?' ")
            print("You: Hi, my name is", name,". Nice to meet you!")
            time.sleep(1)
            print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
            time.sleep(2)
            print(npc_1,": Hi", name,",")
            time.sleep(1)
            print(npc_1,": (Chuckle)I want to play a game...\nPlease choose a number...from 5 to 15...(creepy smile)")
            time.sleep(1)
            # Interaction 5: Choose a number (Continue)
            while True:
              user_choice_4 = int(input("You are worrying if it is a trap...or a reward...\nChoose a number from 5 to 15: "))
              if user_choice_4 in range(5,16):
                print(f"You chose {user_choice_4}, what you got is...\n{user_choice_4} coins!!")
                wallet += int(user_choice_4)
                time.sleep(1)
                print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                time.sleep(1)
                print(npc_1,": Congrats, You got the reward! Please come in to play the final game. (Opening the door...)")
                time.sleep(1)
                print("You: Thank you!")
                time.sleep(2)                  
                
                # Room 6: Final Stage
                print(final_stage)
                time.sleep(1)
                print(look_closer)
                time.sleep(1)
                print("An", npc_2,"!!!")
                time.sleep(1)
                print(npc_2,": Roar!!(rushing towards you...)")
                time.sleep(1)
                while True:
                  # Interaction 6: Choose a number
                  user_choice_5 = int(input("What should you do?\nPress [1] to fight\nPress [2] to dodge\n"))
                  computer_choice_final = np.random.choice(computer_choice)
                  # Answer 6: Fight (Continue)
                  if user_choice_5 == 1:
                    # Evil Minion is stunned
                    if user_choice_5 < computer_choice_final:
                      print(npc_2,"is stunned.")
                      time.sleep(1)
                      print("You hit",npc_2,"with a coin.")
                      time.sleep(1)
                      wallet -= 1
                      minion_health -= 1
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)
                    # Evil Minion attacks
                    elif user_choice_5 == computer_choice_final:
                      print(npc_2,"also attacks.")
                      time.sleep(1)
                      print(npc_2,"and you hit each other.")
                      time.sleep(1)
                      wallet -= 1
                      health -= 20
                      minion_health -= 1
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)
                    # Evil Minion dodges
                    else:
                      print(npc_2,"dodges your coin attack.")
                      time.sleep(1)
                      wallet -= 1
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)
                  # Answer 6: Dodge (Continue)
                  elif user_choice_5 == 2:
                    # Evil Minion attacks
                    if computer_choice_final == 1:
                      print(npc_2,"attacks.")
                      time.sleep(1)
                      print("You dodge the attack from",npc_2,".")
                      time.sleep(1)
                      health += 20
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)
                    # Evil Minion is stunned
                    elif computer_choice_final == 0:
                      print(npc_2,"is stunned.")
                      time.sleep(1)
                      print("You dodge.")
                      time.sleep(1)
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)      
                    # Evil Minion dodges
                    else:
                      print(npc_2,"and you dodged each other.")
                      time.sleep(1)
                      print(f"{npc_2} health: {minion_health}")
                      time.sleep(1)
                      print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                      time.sleep(1)
                  else:
                    print("Invalid input. Please enter 1 or 2.")
                    time.sleep(2)
                    continue
                  # If your health is 0
                  if health <= 0:
                    active = True
                    while active == True:
                      # You can't retrieve when you don't have Celery
                      if celery not in bag and health <= 0:
                        print("You have nothing to retrive yourself. \nYou die. Game over!")
                        exit() 
                      # You can retrieve when you have Celery
                      elif celery in bag:
                        print("You are about to die but you remember you have a Celery in your bag...")
                        # Interaction 7: Live Or Die, Make Your Choice
                        user_choice_6 = input("Would you like to use Celery to retrieve your life?\nPress [1] Yes [2] No\n")
                        # Answer 7: Live (Continue)
                        if user_choice_6 == "1":
                          print("You: (munching Celery) Oh...I feel alive!!")
                          time.sleep(1)
                          bag.remove(celery)
                          health = 100
                          print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                          time.sleep(1)
                          active = False
                        # Answer 7: Die (Gave Over)
                        elif user_choice_6 == "2":
                          print("You give up to retrieve yourself... \nYou die. Game over!")
                          exit() 
                        else:
                          print("Invalid input. Please enter 1 or 2.")
                          time.sleep(2)
                          continue
                  # If Evil Minion's health is 0
                  if minion_health <= 0:
                    print(npc_2,": Poopaye(Goodbye)...")
                    time.sleep(1)
                    print("You win! Good job!")
                    time.sleep(1)
                    print(npc_2,"change back to normal a Minion.")
                    time.sleep(1)
                    print(npc_3,":Bello! Pwede na?(Hello! Can we start?)") 
                    time.sleep(1)
                    while True:
                      # Interaction 8: Pet a minion
                      user_choice_7 = input("Would you like adopt the minion as a pet?\nPress [1] Yes [2] No\n")
                      # Answer 8: Adopt (Gave Over)
                      if user_choice_7 == "1":
                        print("Now, you adopt the Minion as your pet and start a new adventure...")
                        time.sleep(1)
                        bag.append(minion)
                        print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                        time.sleep(1)
                        print("---Game End---\n---Thanks for playing---")
                        exit()
                      #Answer 8: Give up (Gave Over)
                      elif user_choice_7 == "2":
                        print("You give up to adopt", npc_3,"...")
                        print(npc_3,":Tatata bala tu!(I hate you!)")
                        time.sleep(1)
                        print("You:...")
                        time.sleep(1)
                        print("Anyway, you start a new journey to discover what will happen next...")
                        time.sleep(1)
                        print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
                        time.sleep(1)
                        print("---Game End---\n---Thanks for playing---")
                        exit()
                      else:
                        print("Invalid input. Please enter 1 or 2.")
                        time.sleep(2)
                        continue
                  # If you have no coin and Evil Minion's health more than 0 (Gave Over)
                  if wallet <= 0 and minion_health > 0:
                    print("You used all your coin. Game over!")
                    exit()  
              else:
                print("Invalid input. Please enter an integer from 1 to 10.")
                time.sleep(2)
                continue
          # Answer 3: Leave (Game Over)
          if user_choice_3 == "2":
            print("Never ignore a girl!!!")
            time.sleep(1)
            print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
            print("Game over!")
            exit()  
          # Answer 3: Celery (Loop)
          if user_choice_3 == "3":
            if celery not in bag:
              print("You pick a Celery!")
              bag.append(celery)
            else:
              print("You have already picked the Celery! Please choose again!")
            time.sleep(1)  
            print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
            time.sleep(2)
            continue 
          else:
            print("Invalid input. Please enter 1 or 2 or 3.")
            time.sleep(2)
            continue
      # Room 7: Elevator
      # Answer 2: Elevator (Loop)      
      if user_choice_2 == "2":
        print(elevator)
        time.sleep(1)
        print("Please choose the other way.")
        time.sleep(1)
        print(f"Your health: {health}\nYour wallet: ${wallet}\nYour bag: {bag}")
        time.sleep(2)
        continue
      else:
        print("Invalid input. Please enter 1 or 2.")
        time.sleep(2)
        continue
  else:
    print("Invalid input. Please enter 1 or 2.")
    time.sleep(2)
    continue

