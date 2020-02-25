#import time

main = 'run'

while main == 'run':
        spielphase = 0
        h = 0
        placeholder = 0
        nodraw = 0
        gotanswer = False
        feldgröße = 3
        raster = [[''] * feldgröße for i in range(feldgröße)]
        for i in range(feldgröße):
                for j in range(feldgröße):
                        raster[i][j] = ' '



        print("TIC TAC TOE the GAME!!!:")
        print('')
        try:
                time.sleep(1)
        except:
                placeholder += 1 
        #exaple matrix
        example = [[''] * feldgröße for i in range(feldgröße)]
        for i in range(feldgröße):
                for j in range(feldgröße):
                                example[i][j] = str(i) + ' ' + str(j)

        for row in example:
                print('|'.join([str(elem) for elem in row]))                
        #Game explanation
        print('')
        print("the first number represents the collum.")
        print("the second number represents the row.")
        print('')
        print("Sign of player 1 is 'X'")
        print("Sign of player 1 is 'O'")
        print("Enter ur position alternating.")
        print('')
        print("You win if you can place ur simbol in one full row, collum or diagonal!")
        print('')
        try:
                time.sleep(5)
        except:
                placeholder += 1
        for row in raster:
                print('|'.join([str(elem) for elem in row]))

        try:
                time.sleep(0.5)
        except:
                placeholder += 1
        print('')
        print('')
        
        #begin of the game                
        while spielphase != 9:
                print('')
                try:
                        x = input("Enter columm, row and 'ur sign'. Seperate them with spaces. (example: 0 1 X)")
                        x = x.upper()
                        x = x.split()
                        if str(x[2]) != 'X' and str(x[2]) != 'O':
                                print('You need to enter "X" or "O"!')
                                continue
                        if raster[int(x[0])][int(x[1])] != ' ':
                                print('already taken! please pic another spot.')
                        else:
                                raster[int(x[0])][int(x[1])] = str(x[2])
                                spielphase += 1
                        for row in raster:
                            print('|'.join([str(elem) for elem in row]))
                except:
                        continue
                #Checks if someone won horizontaly
                for e in range(feldgröße):
                        if raster[e].count('X') == 3:
                                print("Congratulation 'X' won!")
                                nodraw = 1
                                spielphase = 9
                                break
                        elif raster[e].count('O') == 3:
                                print("Congratulation 'O' won!")
                                nodraw = 1
                                spielphase = 9
                                break
                        else:
                                continue

                #Checks if someone won verticaly  
                for e in range(feldgröße):
                        for q in range(feldgröße):
                                if raster[q][e] == 'X':
                                        h = str(h).join(['', str('X')])
                                        
                                elif raster[q][e] == 'O':
                                        h = str(h).join(['', str('O')])
                                        
                                else:
                                        continue
                        try:
                                h = list(h)     
                        except:
                                break
                        for k in range(feldgröße):
                                if h.count('X') == 3:
                                        print("Congratulation 'X' won!")
                                        nodraw = 1
                                        spielphase = 9
                                        break
                                elif h.count('O') == 3:
                                        print("Congratulation 'O' won!")
                                        nodraw = 1
                                        spielphase = 9
                                        break
                                else:
                                        continue
                        h = 4

                # Checks if someone won diagonaly
                #from top left to bottom right
                if raster[0][0] == 'X' and raster[1][1] == 'X' and raster[2][2] == 'X':
                        print("Congratulation 'X' won!")
                        nodraw = 1
                        spielphase = 9
                        break
                if raster[0][0] == 'O' and raster[1][1] == 'O' and raster[2][2] == 'O':
                        print("Congratulation 'O' won!")
                        nodraw = 1
                        spielphase = 9
                        break
                #from top right to bottom left
                if raster[0][2] == 'X' and raster[1][1] == 'X' and raster[2][0] == 'X':
                        print("Congratulation 'X' won!")
                        nodraw = 1
                        spielphase = 9
                        break
                if raster[0][2] == 'O' and raster[1][1] == 'O' and raster[2][0] == 'O':
                        print("Congratulation 'O' won!")
                        nodraw = 1
                        spielphase = 9
                        break

        #ask if play again if !true breaks main loop
        while gotanswer != True:
                try:
                        if nodraw != 1:
                                m = input("It's a DRAW! Do yoou want to play again? (j/n)")
                        else:
                                m = input("Do you want to play again? (j/n)")
                        m = m.lower()
                        if m == 'j':
                                gotanswer = True
                                main = 'run'
                                print("OK")
                                print('')
                                try:
                                        time.sleep(1)
                                except:
                                        placeholder += 1
                                continue
                        elif m == 'n':
                                gotanswer = True
                                main = 'stop'
                                print("OK ... Bye!")
                                break
                        else:
                                print("Sorry I didn't understand that!")
                                continue
                except:
                        print("Sorry I didn't understand that!")
                        continue

