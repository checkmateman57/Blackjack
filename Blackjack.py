def lb():
    try:
        with open('balance.txt', 'r') as file:
            return float(file.read())
    except FileNotFoundError:
        return 500
def sb(balance):
    with open('balance.txt', 'w') as file:
        file.write(str(balance))
cb = lb()
uc1 = int(0)
uc2 = int(0)
dc1 = int(0)
dc2 = int(0)
a = int(1)
bet = int(0)
bet2 = int(0)
print("Welcome to Blackjack! Please answer with 'yes' to any yes or no questions you want to answer with yes.")
rules = input("Would you like to know the rules?\n")
if rules.lower() == 'yes':
    print("Here are the rules of blackjack:"
          "Your goal is to reach a score of 21, which is a blackjack"
          "All cards are worth what they say, except 11s which can turn into 1s if you go over 21\n"
          "If you go over 21, and don't have any 11s, you bust and automatically lose\n"
          "During you turn you have the option to hit, stand, double down, or split\n"
          "Hit: get another card\n"
          "Stand: Keep the score you have\n"
          "Double Down: Double your bet and get only one more card\n"
          "Split: This only works when you have 2 of the same worth card. You double your bet, and get 2 separate hands, with the cards you split as the base of the hand\n"
          "You don't always need to hit to get closer to 21, the dealer must stop when their score reaches at least 17\n"
          "You win if the dealer gets over 21\n"
          "This is a strategy game: be smart\n")
p = True
import random


while p == True:
    if a == int(1):
        sbd = False
        split = False
        dd = False
        play = input('Do you want to play?\n')
        if play.lower() == 'yes':
            a = int(11)
        while a == int(11):
            totalbet = 0
            sbet1 = 0
            sbet2 = 0
            sbet3 = 0
            sbet4 = 0
            sbet5 = 0
            bet = float(input(f'How much do you want to bet? Your current balance is {cb}\n'))
            if bet > cb:
                print("You can't bet that amount.")
            else:
                a = int(20)
        if play.lower() != 'yes':
            p = False
            break


    if a == int(20):
        sbd = input('Would you like to make any side bets?\n')
        if sbd.lower() == 'yes':
            sbd = True
            a = int(21)
        else:
            a = int(10)

    if a == int(21):
        Pairs = False
        tp3 = False
        tkind = False
        OU13 = False
        S7 = False
        sbet1 = int(0)
        sbet2 = int(0)
        sbet3 = int(0)
        sbet4 = int(0)
        sbet5 = int(0)
        sbetc = int(0)
        sbrules = 'no'
        sbrules = input('Would you like to know the side bets available, and what needs to be done?\n')
        if sbrules.lower() == 'yes':
            print('Here are the side bets:\n'
                  'Pairs: If both of your cards are the same number. Payout: 5:1\n'
                  '21+3: If both your cards and the dealers first card are sequential. Payout: 10:1\n'
                  '3 of a kind: If your 2 cards and the dealers first card are all the same. Payout: 30:1\n'
                  'Over/Under 13: Choose whether your first 2 card will be over or under 13. Payout: 2:1\n'
                  'Super 7s: If one, two, or three cards between your first 2 and the dealers first are 7. Payout: One 7, 3:1  Two 7s, 50:1, Three 7s, 100:1\n')
        else:
            sbets = int(input('How many side bets would you like to make? (max 5)\n'))
            sbetc = int(0)
            while sbets != sbetc:
                sbetc = sbetc + 1
                sbetq = input('What side bet would you like to make? Your options are: Pairs, 21+3, 3 of a kind, Over/Under 13, and Super 7s\n')


                if sbetq.lower() == 'pairs':
                    if Pairs == True:
                        print('You already made a bet here\n')
                        sbetc = sbetc - 1
                    else:
                        sbet1 = int(input('How much would you like to bet on this side bet\n'))
                        if sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet > cb:
                            print("You don't have enough money to make that bet\n")
                            sbet1 = int(0)
                            sbetc = sbetc - 1
                        else:
                            Pairs = True
                            print('Your bet has been made\n')


                if sbetq == '21+3':
                    if tp3 == True:
                        print('You already made a bet here\n')
                        sbetc = sbetc - 1
                    else:
                        sbet2 = int(input('How much would you like to bet on this side bet\n'))
                        if sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet > cb:
                            print("You don't have enough money to make that bet\n")
                            sbet2 = int(0)
                            sbetc = sbetc - 1
                        else:
                            tp3 = True
                            print('Your bet has been made.\n')

                if sbetq.lower() == '3 of a kind':
                    if tkind == True:
                        print('You already made a bet here\n')
                        sbetc = sbetc - 1
                    else:
                        sbet3 = int(input('How much would you like to bet on this side bet\n'))
                        if sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet > cb:
                            print("You don't have enough money to make that bet\n")
                            sbet3 = int(0)
                            sbetc = sbetc - 1
                        else:
                            tkind = True
                            print('Your bet has been made.\n')

                if sbetq.lower() == 'over/under 13':
                    U13 = False
                    O13 = False
                    if OU13 == True:
                        print('You already made a bet here\n')
                        sbetc = sbetc - 1
                    else:
                        sbet4 = int(input('How much would you like to bet on this side bet\n'))
                        if sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet > cb:
                            print("You don't have enough money to make that bet\n")
                            sbet4 = int(0)
                            sbetc = sbetc - 1
                        else:
                            OU = input('Would you like to bet the over or under\n')
                            if OU.lower() == 'over':
                                O13 = True
                                OU13 = True
                                print('Your bet has been made.\n')
                            else:
                                U13 = True
                                OU13 = True
                                print('Your bet has been made.\n')

                if sbetq.lower() == 'super 7s':
                    if S7 == True:
                        print('You already made a bet here\n')
                        sbetc = sbetc - 1
                    else:
                        sbet5 = int(input('How much would you like to bet on this side bet\n'))
                        if sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet > cb:
                            print("You don't have enough money to make that bet\n")
                            sbet5 = int(0)
                            sbetc = sbetc - 1
                        else:
                            S7 = True
                            print('Your bet has been made.\n')
                totalbet = sbet1 +sbet2 + sbet3 + sbet4 + sbet5 + bet
            if sbetc == sbets:
                a = int(10)








    if a == int(10):
        totalbet = sbet1 + sbet2 + sbet3 + sbet4 + sbet5 + bet
        s1e = int(0)
        s2e = int(0)
        e = int(0)
        de = int(0)
        uc1 = random.randint(7,7)
        if uc1 == int(11):
            e = e + 1
        dc1 = random.randint(7,7)
        if dc1 == int(11):
            de = de +1
        uc2 = random.randint(7,7)
        if uc2 == int(11):
            e = e + 1
        dc2 = random.randint(2,11)
        if dc2 == int(11):
            de = de + 1
        uh = uc1 + uc2
        if uc1 == int(11) and uc2 == int(11):
            uh = int(12)
            e = int(1)
        dh = dc1 +dc2
        if dc1 == int(11) and dc2 == int(11):
            dh = int(12)
            de = int(1)
        if uc1 == uc2 and totalbet + bet <= cb:
            split = True
            pairsc = True
        if uc1 != uc2 or totalbet + bet > cb:
            split = False
            pairsc = False
        if totalbet + bet <= cb:
            dd = True
        if totalbet + bet > cb:
            dd = False
        print (f'Your first card is {uc1}, your second card {uc2}, and your total hand {uh}')
        if uh == int(21):
            print("Blackjack!")
            print (f'The dealers first card is {dc1}')
            a = int(3)
        if uh != int(21):
            print (f'The dealers first card is {dc1}')
            a = int(2)



    if a == int(2):
        play = 'no'
        action = input ('What would you like to do: Hit, Stand, Split, or Double Down?\n')
        if action.lower() == 'split':
            if split == False:
                print("You can't split because either your cards don't match or you don't have enough money")
            if split == True:
                bet2 = bet
                s1 = random.randint(2,11)
                if s1 == int(11):
                    s1e = s1e + 1
                s2 = random.randint(2,11)
                if s2 == int(11):
                    s2e = s2e + 1
                if uc1 == int(11):
                    s1e = s1e + 1
                if uc2 == int(11):
                    s2e = s2e +1
                sh1 = uc1 + s1
                sh2 = uc2 + s2
                print(f'Your first hand draws a {s1}, for a first hand of {sh1}')
                print(f'Your second hand draws a {s2}, for a second hand of {sh2}')
                a = int(9)
        if action.lower() == 'hit':
            split = False
            uc3 = random.randint(2,11)
            if uc3 == int(11):
                e = e+1
            uh = uh + uc3
            if uh > int(21):
                if e >= int(1):
                    e = e - 1
                    uh = uh - 10
                else:
                    print(f'{uh}, You bust')
                    cb = cb - bet
                    a = int(6)
            print (f'You draw a {uc3}, bringing your hand to {uh}')
            if uh == int(21):
                print('Blackjack!')
                a = int(3)
        if action.lower() == 'stand':
            split = False
            a = int(3)
        if action.lower() == 'double down':
            if dd == False:
                print("You don't have enough money to do that.")
            else:
                split = False
                bet = bet * 2
                uc3 = random.randint(2,11)
                if uc3 == int(11):
                    e = e + 1
                uh = uh + uc3
                if uh > int(21):
                    if e >= int(1):
                        e = e - 1
                        uh = uh - 10
                    else:
                        print (f'{uh}, You bust')
                        cb = cb - bet
                        a = int(6)
                print(f'You draw a {uc3}, bringing your hand to {uh}')
                if uh == int(21):
                    print('Blackjack!')
                a = int(3)



    if a == int(9):
        sh1a = input('What would you like to do with your first hand: Hit, Stand, or Double Down?\n')
        if sh1a.lower() == 'hit':
            s12 = random.randint(2,11)
            if s12 == int(11):
                s1e = s1e + 1
            sh1 = sh1 + s12
            if sh1 > int(21):
                if s1e >= 1:
                    s1e = s1e - 1
                    sh1 = sh1 - 10
                else:
                    print(f'You draw a {s12}, and bust your first hand at {sh1}')
                    cb = cb - bet
                    a = int(8)
            if sh1 < int(21):
                print(f'You draw a {s12}, which brings your first hand to {sh1}')
            if sh1 == int(21):
                print('Blackjack!')
                a = int(8)
        if sh1a.lower() == 'stand':
            a = int(8)
        if sh1a.lower() == 'double down':
            bet = bet * 2
            if totalbet + bet + bet2 <= cb:
                dds1 = True
            if totalbet + bet + bet2 > cb:
                dds1 = False
            if dds1 == True:
                s12 = random.randint(2,11)
                if s12 == int(11):
                    s1e = s1e + 1
                sh1 = sh1 + s12
                if sh1 > int(21):
                    if s1e >= 1:
                        s1e = s1e - 1
                        sh1 = sh1 - 10
                    else:
                        print(f'You draw a {s12}, and bust your first hand at {sh1}')
                        cb = cb - bet
                        a = int(8)
                if sh1 > int(21):
                    print(f'You draw a {s12}, which brings your hand to {sh1}')
                a = int(8)
            if dds1 == False:
                bet = bet / 2
                print("You don't have enough money to do this")



    if a == int(8):
        sh2a = input('What would you like to do with your second hand: Hit, Stand, or Double Down?\n')
        if sh2a.lower() == 'hit':
            s22 = random.randint(2,11)
            if s22 == int(11):
                s2e = s2e +1
            sh2 = sh2 + s22
            if sh2 > int(21):
                if s2e >= 1:
                    s2e = s2e - 1
                    sh2 = sh2 - 10
                else:
                    print(f'You draw a {s22}, and bust your second hand at {sh2}')
                    cb = cb - bet2
                    a = int(3)
            if sh2 < int(21):
                print(f'You draw a {s22}, which brings your second hand to {sh2}')
            if sh2 == int(21):
                print('Blackjack!')
                a = int(3)
        if sh2a.lower() == 'stand':
            a =int(3)
        if sh2a.lower() == 'double down':
            bet2 = bet2 * 2
            if bet + bet2 <= cb:
                dds2 = True
            if bet + bet2 > cb:
                dds2 = False
            if dds2 == True:
                s22 = random.randint(2,11)
                if s22 == int(11):
                    s2e = s2e + 1
                sh2 = sh2 + s22
                if sh2 > int(21):
                    if s2e >= 1:
                        s2e = s2e - 1
                        sh2 = sh2 - 10
                    else:
                        print(f'You draw a {s22}, and bust your second hand at {sh2}')
                        cb = cb - bet2
                        a = int(3)
                print(f'You draw a {s22}, which brings your hand to {sh2}')
                a = int(3)
            if dds2 == False:
                bet2 = bet2 / 2
                print("You don't have enough money to do that")



    if a == int(3):
        print(f"The dealer's second card is {dc2}, and their hand is {dh}\n")
        a = int(4)



    if a == int(4):
        if dh >= int(17):
            a = int(5)
        else:
            dc3 = random.randint(2,11)
            if dc3 == int(11):
                de = de + 1
            dh = dh + dc3
            if dh > int(21):
                if de >= int(1):
                    de = de - 1
                    dh = dh - 10
            print(f'The dealer draws a {dc3}, bringing their hand to {dh}\n')



    if a == int(5):
        if split == True:
            if sh1 > int(21) and sh2 > int(21):
                a = int(6)
            if sh1 > int(21):
                if dh > int(21):
                    print('The dealer busts, and you win your second hand. Your balance remains the same.\n')
                    cb = cb + bet2
                    a = int(6)
                elif dh > sh2:
                    print('The dealer has a higher score than you on your second hand, you lose both hands.\n')
                    cb = cb - bet2
                    a = int(6)
                elif sh2 > dh:
                    if sh2 == int(21):
                        print('You win your second hand with a blackjack!\n')
                        bet2 = bet2 * 1.5
                        cb = cb + bet2
                    else:
                        print('Your second hand is higher than the dealer. You win!\n')
                        cb = cb + bet2
                else:
                    print('Your second hand ties the dealer. You have lost money\n')
                a = int(6)
            elif sh2 > int(21):
                if dh > int(21):
                    print('The dealer busts, and you win your first hand. Your balance remains the same.\n')
                    cb = cb + bet
                    a = int(6)
                elif dh > sh1:
                    print('The dealer has a higher score than you on your first hand, you lose both hands.\n')
                    cb = cb - bet
                    a = int(6)
                elif sh1 > dh:
                    if sh1 == int(21):
                        print('You win your first hand with a blackjack!\n')
                        bet2 = bet * 1.5
                        cb = cb + bet
                    else:
                        print('Your first hand is higher than the dealer. You win!\n')
                        cb = cb + bet
                else:
                    print('Your first hand ties the dealer. You have lost money\n')
                a = int(6)
            else:
                if sh1 > dh > sh2:
                    if sh1 == int(21):
                        print('Your first hand was a blackjack! The dealer had a higher hand than your second hand')
                        bet = bet * 1.5
                        cb = cb + bet
                        cb = cb - bet2
                    else:
                        print('One of your hands is higher than the dealer and the other is lower. Your balance remains the same.\n')
                if sh2 > dh > sh1:
                    if sh2 == int(21):
                        print('Your second hand was a blackjack! The dealer had a higher hand than your first hand.')
                        bet2 = bet2 * 1.5
                        cb = cb + bet2
                        cb = cb - bet
                    else:
                        print('One of your hands is higher than the dealer and the other is lower. Your balance remains the same.\n')
                if dh > sh2 > sh1:
                    if dh > 21:
                        print ('The dealer busts, both of your hands wins')
                        cb = cb + bet
                        cb = cb + bet2
                    else:
                        print('The dealers hand is higher than both of yours. You lose both hands.\n')
                        cb = cb - bet
                        cb = cb - bet2
                if dh > sh1 > sh2:
                    if dh > 21:
                        print ('The dealer busts, both of your hands wins')
                        cb = cb + bet
                        cb = cb + bet2
                    else:
                        print('The dealers hand is higher than both of yours. You lose both hands\n')
                        cb = cb - bet
                        cb = cb - bet2
                if sh1 > dh and sh2 > dh:
                    print('Both of your hands beat the dealer. You win both hands\n')
                    if sh1 == int(21):
                        print('Your first hand was a blackjack!')
                        bet = bet * 1.5
                    if sh2 == int(21):
                        print('Your second hand was a blackjack!')
                        bet2 = bet2 * 1.5
                    cb = cb + bet
                    cb = cb + bet2
                if sh1 == dh == sh2:
                    print('All of your hands tie.\n')
                if sh1 == dh or sh2 == dh:
                    if sh1 > dh or sh2 > dh:
                        if sh1 == int(21) or sh2 == int(21):
                            print('One of your hands tie, and one of your hands is a blackjack!\n')
                            if sh1 == int(21):
                                bet = bet * 1.5
                                cb = cb + bet
                            else:
                                bet2 = bet2 * 1.5
                                cb = cb + bet2
                        else:
                            print('One of your hands tie, and the other one is higher\n')
                            if sh1 > dh:
                                cb = bet + cb
                            else:
                                cb = cb + bet2
                    if dh > sh1 or dh > sh2:
                        print('One of your hands tie, and the other one is lower\n')
                        if dh > sh1:
                            cb = cb - bet
                        else:
                            cb = cb - bet2
            a = int(6)
        if split == False:
            if dh > int(21):
                print('Dealer busts, you win\n')
                cb = cb + bet
                a = int(6)
            if dh == uh:
                print("You and the dealer tie. You don't win any money but don't lose any money\n")
                a = int(6)
            if dh > uh:
                print('The dealer has a higher score than you. You lose\n')
                cb = cb - bet
                a = int(6)
            if uh > dh:
                if uh == int(21):
                    print('You win with a Blackjack! You win 1.5x your bet\n')
                    bet = bet * 1.5
                    cb =  cb + bet
                    a = int (6)
                else:
                    print('You have a higher score than the dealer! You win!\n')
                    cb = cb + bet
                    a = int(6)
            a = int(6)



    if a == int(6):
        if sbd == True:
            if Pairs == True:
                if pairsc == True:
                    print(f'You won your side bet on pairs. You get double your side bet, which was {sbet1}')
                    cb = cb + sbet1
                else:
                    print('You lost your side bet on pairs.')
                    cb = cb - sbet1
            if tp3 == True:
                tp3c = False
                if uc1 + 1 == uc2 and uc2 + 1 == dc1:
                    tp3c = True
                if uc1 + 1 == dc1 and dc1 + 1 == uc2:
                    tp3c = True
                if uc2 + 1 == dc1 and dc1 + 1 == uc1:
                    tp3c = True
                if uc2 + 1 == uc1 and uc1 + 1 == dc1:
                    tp3c = True
                if dc1 + 1 == uc1 and uc1 + 1 == uc2:
                    tp3c = True
                if dc1 + 1 == uc2 and uc2 + 1 == uc1:
                    tp3c = True
                if tp3c == True:
                    print(f'You won your 21+3 side bet. You get 10x your side bet, which was {sbet2}')
                    sbet2 = sbet2 * 9
                    cb = cb + sbet2
                if tp3c == False:
                    print('You lost your 21+3 side bet')
                    cb = cb - sbet2
            if tkind == True:
                tkindc = False
                if uc1 == uc2 and uc1 == dc1:
                    tkindc = True
                if tkindc == True:
                    print(f'You won your 3 of a kind side bet. You get 30x your side bet, which was {sbet3}')
                    sbet3 = sbet3 * 29
                    cb = cb + sbet3
                else:
                    print('You lost your 3 of a kind side bet')
                    cb = cb - sbet3
            if OU13 == True:
                U13c = False
                O13c = False
                if uc1 + uc2 > 13:
                    O13c = True
                    U13c = False
                if uc1 + uc2 < 13:
                    U13c = True
                    O13c = False
                if O13 == True:
                    if O13c == True:
                        print(f'You won the over. You get double your side bet, which was {sbet4}')
                        cb = cb + sbet4
                    if O13c == False:
                        if U13c == False:
                            print("It's 13, so you don't win or lose")
                        else:
                            print('You lost the over')
                            cb = cb - sbet4
                if U13 == True:
                    if U13c == True:
                        print(f'You won the under. You get double your side bet, which was {sbet4}')
                        cb = cb + sbet4
                    if U13c == False:
                        if O13c == False:
                            print("It's 13, so you don't win or lose")
                        else:
                            print('You lost the under')
                            cb = cb - sbet4
            if S7 == True:
                S7c = False
                if uc1 == 7 or uc2 == 7 or dc1 == 7:
                    S7c = True
                if S7c == True:
                    if uc1 == 7 and uc2 != 7 and dc1 !=7:
                        print(f'Only one 7 was present, you get 3x your sidebet, which was {sbet5}')
                        sbet5 = sbet5 * 2
                        cb = cb + sbet5
                    if uc2 == 7 and uc1 != 7 and dc1 !=7:
                        print(f'Only one 7 was present, you get 3x your sidebet, which was {sbet5}')
                        sbet5 = sbet5 * 2
                        cb = cb + sbet5
                    if dc1 == 7 and uc2 != 7 and uc1 !=7:
                        print(f'Only one 7 was present, you get 3x your sidebet, which was {sbet5}')
                        sbet5 = sbet5 * 2
                        cb = cb + sbet5
                    if uc1 == 7 and uc2 == 7 and dc1 != 7:
                        print(f'2 7s were present, so you get 50x your side bet, which was {sbet5}')
                        sbet5 = sbet5 * 49
                        cb = cb + sbet5
                    if dc1 == 7 and uc2 == 7 and uc1 != 7:
                        print(f'2 7s were present, so you get 50x your side bet, which was {sbet5}')
                        sbet5 = sbet5 * 49
                        cb = cb + sbet5
                    if uc1 == 7 and dc1 == 7 and uc2 != 7:
                        print(f'2 7s were present, so you get 50x your side bet, which was {sbet5}')
                        sbet5 = sbet5 * 49
                        cb = cb + sbet5
                    if uc1 == 7 and dc1 == 7 and uc2 == 7:
                        print(f'You got the Super 7s! You winn 100x your side bet, which was {sbet5}')
                        sbet5 = sbet5 * 99
                        cb = cb + sbet5
                if S7c == False:
                    print('You lost your side bet of super 7s')
                    cb = cb - sbet5
            a = int(100)
        else:
            a = int(100)

    if a == int(100):
        sb(cb)
        print(f'Your new balance is {cb}')
        if cb == int(0):
            print('You went bankrupt, your balance resets at 500')
            cb = int(500)
            sb(cb)
        else:
            a = int(1)