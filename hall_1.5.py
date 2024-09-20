##
##
## This Game Was Developed By Sam Waters AKA: Rev2saws
## Please Do Not Claim This Game As Your Own
## If You Want To Make A Parody Of My Game Let Me Know At:
## revsaws9@gmail.com
##
##
## Imports For The Game
##
## Imports The random.randint Method
import random
## Imports The os.system('cls' if os.name == 'nt' else 'clear') Method That Lets The Program Clear The Console
import os
## Imports The time.sleep Method
import time
## Variables For The Game
## HUD Variables
HOOOF = 0
HOOO = "1"
## Player Max Health
PMH = 100
## Starting Amount Of Keys For The Player
KEY = 0
## Used For Alchemy And Potion Making
BUCK = 0
## Sets Players Health To Their Max Health
PH = PMH
## Starting Player XP
EXP = 0
## Enemy Minimum Attack Value
EMINA = 2
## Enemy Maximun Attack Value
EMA = 7
## Starting Amount For Required EXP To Level Up
EXPR = 200
## Varibles To Deal With While Loops Mainly
CSCF = 0
GC = 1
## Enemy's Starting Max Health
EMH = 50
## Sets Enemy Health To Their Max Health
EH = EMH
## Player Items
## Starting Medium Potions
MEDP = 0
## Starting Large Potions
LARGEP = 0
## Starting Small Potions
SMLLP = 3
## Starting Food
FOOD = 2
## Player Max Attack
PMA = 10
## Total Distance Moved
DM = 0
## Player Minimum Attack Value
PMINA = 5
## Player Max Defence Value
PMD = 3
## Player Minimum Defence Value
PMIND = 0
## Players Critical Hit Chance
CRTC = 5
## Critical Hit Multiplier
CRTM = 2
## The Total Amount Of The Players Gold
PGT = 0
## Keeps Track Of The Current Players Level
CPL = 1
## Locks For The Game. It Is Here For Optimization Of The Game.
TLOC = 0
ITLOC = 0
TTPLOC = 0
PCBILOC = 0
HPSLOC = 0
## Deals With Whether Or Not The Player Can Heal By The Tavern Fire
PAWBF = 0
## Deals With Player Quest Items
PQIBP = 0
PQIWK = 0
WBPBCB = 0
TOTTCQ = 0
BOC = 0
## Different Types Of Leaves For Potion Crafting
WEALEA = 0
MILLEA = 0
POTLEA = 0
## Enemy Sprites For The Game
ESL1WBR = "Wet Paper Bag + Rat    "
ESL2WBR = "-----------------------"
ESL3WBR = "Rat In A Wet Paper Bag?"
ESL1FVC = "mother..."
ESL2FVC = "i request..."
ESL3FVC = "to see the light once more..."
ESL1BD = " 0  DoRiToS "
ESL2BD = " b  "
ESL3BD = " \= "
ESL1CB = "CHADWICK"
ESL2CB = "BALDWIN"
ESL3CB = "THE THIRD"
ESL1AOD = "G E T"
ESL2AOD = "O F F"
ESL3AOD = "M Y L A W N"
ESL1HWOC = "Why Is THis Cheese A Heritic?"
ESL2HWOC = "Well You See...."
ESL3HWOC = "It Think That Melted Cheese Is Good On Popcorn"
ESL1LR = "Its A Rat..."
ESL2LR = "Thats Large.."
ESL3LR = "Seems Pretty Normal To Me"
ESL1S = "MMMM... Jello"
ESL2S = "Why Is It Moving?"
ESL3S = "Thats A Weird Peice Of Jello"
ESL1G = "GOLD"
ESL2G = "GOLD"
ESL3G = "GOLD"
## Sets The Current Quest To No Quest
CCQ = 0
## Definitions For The Game
## Potion Creation System
def HPS():
    ## Variables For Potion Creation
    global HPSLOC
    global WEALEA
    global MILLEA
    global POTLEA
    global SMLLP
    global MEDP
    global LARGEP
    global BUCK
    HPSLOC = 1
    ## Checks To See If HPSLOC Is Active. This Just Loops The Menu Unless The Player Exits It
    while HPSLOC == 1:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("         || Potion Creation ||         ")
        print(" --------------------------------------")
        print(" [1] || 5 Small Potions ||")
        print(" --------------------------------------")
        print(" 0 4 Weak Leaves / " + str(WEALEA) + " Weak Leaves")
        print(" 0 1 Empty Bucket / " + str(BUCK) + " Buckets")
        print(" --------------------------------------")
        print(" [2] || 3 Medium Potions ||")
        print(" --------------------------------------")
        print(" 0 6 Weak Leaves / " + str(WEALEA) + " Weak Leaves")
        print(" 0 3 Mild Leaves / " + str(MILLEA) + " Mild Leaves")
        print(" 0 1 Empty Bucket / " + str(BUCK) + " Buckets")
        print(" --------------------------------------")
        print(" [3] || 2 Large Potions ||")
        print(" --------------------------------------")
        print(" 0 8 Weak Leaves / " + str(WEALEA) + " Weak Leaves")
        print(" 0 6 Mild Leaves / " + str(MILLEA) + " Mild Leaves")
        print(" 0 3 Potent Leaves / " + str(POTLEA) + " Potent Leaves")
        print(" 0 1 Empty Bucket / " + str(BUCK) + " Buckets")
        print(" --------------------------------------")
        print(" [4] Exit ")
        print(" --------------------------------------")
        print(" You Currently Have: ")
        print(" " + str(SMLLP) + " Small Potions")
        print(" " + str(MEDP) + " Medium Potions")
        print(" " + str(LARGEP) + " Large Potions")
        print("")
        ## Players Choice On What To Do
        HPSCC = input("")
        if HPSCC == "1":
            if WEALEA >= 4 and BUCK >= 1:
                print(" Potions Created!")
                SMLLP = SMLLP + 5
                WEALEA = WEALEA - 4
                BUCK = BUCK - 1
                time.sleep(1)
                print("")
                print(" Press Enter To Continue")
                input("")
            elif WEALEA < 4 or BUCK < 1:
                print(" You Do Not Have The Required Materials For This Potion")
                time.sleep(1)
                print("")
                print(" Press Enter To Continue")
                input("")
        elif HPSCC == "2":
            if WEALEA >= 6 and MILLEA >= 3 and BUCK >= 1:
                print(" Potions Created! ")
                MEDP = MEDP + 3
                WEALEA = WEALEA - 6
                MILLEA = MILLEA - 3
                BUCK = BUCK - 1
                time.sleep(1)
                print("")
                print(" Press Enter To Continue ")
                input("")
            elif WEALEA < 6 or MILLEA < 3 or BUCK < 1:
                print(" You Do Not Have The Required Materials For This Potion")
                time.sleep(1)
                print("")
                print(" Press Enter To Continue ")
                input("")
        elif HPSCC == "3":
            if WEALEA >= 8 and MILLEA >= 6 and POTLEA >= 3 and BUCK >= 1:
                print(" Potions Created! ")
                LARGEP = LARGEP + 2
                WEALEA = WEALEA - 8
                MILLEA = MILLEA - 6
                POTLEA = POTLEA - 3
                BUCK = BUCK - 1
                time.sleep(1)
                print("")
                print(" Press Enter To Continue")
                input("")
            elif WEALEA < 8 or MILLEA <6 or POTLEA < 3 or BUCK < 1:
                print(" You Do Not Have The Required Materials For This Potion")
                time.sleep(1)
                print("")
                print(" Press Enter To Continue")
                input("")
        elif HPSCC == "4":
            HPSLOC = 0
## Save Code Definition
def GSCD():
    ## Clears Previous Console
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    ## ALL Of The Variables Required For The Save Code
    global PMH
    global PH
    global PMA
    global PMINA
    global PMD
    global PMIND
    global CRTC
    global CRTM
    global PGT
    global DM
    global CPL
    global PQIBP
    global PQIWK
    global WBPBCB
    global TOTTCQ
    global BOC
    global EXP
    global EXPR
    global SMLLP
    global MEDP
    global LARGEP
    global EMINA
    global EMA
    global EMH
    global FOOD
    global KEY
    global CCQ
    ## Gives The User 3 Choices When Interfacing With This Menu
    print("")
    print(" /~~~~~~~~~~~~~~~\ ")
    print("")
    print("  [1] Generate ")
    print("  [2] Read Code")
    print("  [3] Exit ")
    print("")
    print(" \~~~~~~~~~~~~~~~/")
    print("")
    GSC = input("")
    ## This Is Option 1. It Just Generates A Save Code Made Up Of Variables And Puts Them All In One String
    if GSC == "1":
        SC = "PMA"
        SC = SC + str(PMA) + "PMINA" + str(PMINA) + "PMD" + str(PMD) + "PMIND" + str(PMIND) + "PMH" + str(PMH) + "PH" + str(PH) + "CRTC" + str(CRTC) + "CRTM" + str(CRTM) + "PGT" + str(PGT) + "DM" + str(DM) + "CPL" + str(CPL) + "PQIBP" + str(PQIBP) + "PQIWK" + str(PQIWK) + "WBPBCB" + str(WBPBCB) + "TOTTCQ" + str(TOTTCQ) + "BOC" + str(BOC) + "EXP" + str(EXP) + "EXPR" + str(EXPR) + "SMLLP" + str(SMLLP) + "MEDP" + str(MEDP) + "LARGEP" + str(LARGEP) + "EMINA" + str(EMINA) + "EMA" + str(EMA) + "EMH" + str(EMH) + "FOOD" + str(FOOD) + "KEY" + str(KEY) + "CCQ" + str(CCQ)
        print("SC " + str(SC) )
        time.sleep(.5)
        print("")
        print(" Press Enter To Continue")
        input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    ## This Is Option 2. If The User Inputs A Valid Save Code, It Will Overwrite All Previous Variables That Were Added In The String
    elif GSC == "2":
        print("")
        print(" Please Input Your Save Code")
        SCR = input("")
        ## Finds The Variable In The Save Code String
        SCRLEN = len(SCR)
        print(SCRLEN)
        GROPMASC = SCR.find("PMA")
        print(" GROPMASC " + str(GROPMASC))
        SCRPMA = SCR[3:]
        print("SCRPMA " + str(SCRPMA))
        SCRAPMAEL = SCRPMA.find("PMINA")
        print("SCRAPMEAL " + str(SCRAPMAEL))
        SCRAPMA = SCRPMA
        print(" SCRAPMA " + str(SCRAPMA))
        PMA = SCRAPMA[:SCRAPMAEL]
        SCRPMINAEL = SCRAPMA.find("A")
        SCRPMINAELE = SCRAPMA.find("PMD")
        SCRPMINAEL = SCRPMINAEL + 1
        print(" SCRPMINAELE " + str(SCRPMINAELE))
        print(" SCRPMINAEL " + str(SCRPMINAEL))
        SCRCRTC = SCRPMA.find("CRTC")
        SCRCRTM = SCRPMA.find("CRTM")
        SCRPMH = SCRPMA.find("PMH")
        SCRPGT = SCRPMA.find("PGT")
        SCRDM = SCRPMA.find("DM")
        SCRCPL = SCRPMA.find("CPL")
        SCRPQIBP = SCRPMA.find("PQIBP")
        SCRPQIWK = SCRPMA.find("PQIWK")
        SCRWBPBCB = SCRPMA.find("WBPBCB")
        SCRTOTTCQ = SCRPMA.find("TOTTCQ")
        SCRBOC = SCRPMA.find("BOC")
        SCREXP = SCRPMA.find("EXP")
        SCREXPR = SCRPMA.find("EXPR")
        SCRSMLLP = SCRPMA.find("SMLLP")
        SCRMEDP = SCRPMA.find("MEDP")
        SCRLARGEP = SCRPMA.find("LARGEP")
        SCREMINA = SCRPMA.find("EMINA")
        SCREMA = SCRPMA.find("EMA")
        SCREMH = SCRPMA.find("EMH")
        SCRFOOD = SCRPMA.find("FOOD")
        SCRKEY = SCRPMA.find("KEY")
        SCRCQ = SCRPMA.find("CCQ")
        ## Prints Where The Save Code Is In The Sting, This Is Mainly Used For Testing Purposes
        print(SCRPMH)
        print(SCRCRTC)
        print(SCRCRTM)
        print(SCRPGT)
        print(SCRDM)
        print(SCRCPL)
        print(SCRPQIBP)
        print(SCRPQIWK)
        print(SCRWBPBCB)
        print(SCRTOTTCQ)
        print(SCRBOC)
        print(SCREXP)
        print(SCREXPR)
        print(SCRSMLLP)
        print(SCRMEDP)
        print(SCRLARGEP)
        print(SCREMINA)
        print(SCREMA)
        print(SCREMH)
        print(SCRFOOD)
        print(SCRKEY)
        print(SCRCQ)
        SCRPH = SCRPMA.find("PH")
        ## Convets Save Code To Values
        PMINA = SCRAPMA[SCRPMINAEL:SCRPMINAELE]
        SCRPMDELE = SCRPMINAELE + 3
        SCRPMINDELE = SCRAPMA.find("PMIND")
        PMD = SCRPMA[SCRPMDELE:SCRPMINDELE]
        SCRPMINDELE = SCRPMINDELE + 5
        PMIND = SCRPMA[SCRPMINDELE:SCRPMH]
        SCRPMH = SCRPMH + 3
        PMH = SCRPMA[SCRPMH:SCRPH]
        SCRPH = SCRPH + 2
        SCRPHE = SCRPH + 3
        PH = SCRPMA[SCRPH:SCRPHE]
        SCRCRTC = SCRCRTC + 4
        CRTC = SCRPMA[SCRCRTC:SCRCRTM]
        SCRCRTM = SCRCRTM + 4
        CRTM = SCRPMA[SCRCRTM:SCRPGT]
        SCRPGT = SCRPGT + 3
        PGT = SCRPMA[SCRPGT:SCRDM]
        SCRDM = SCRDM + 2
        DM = SCRPMA[SCRDM:SCRCPL]
        SCRCPL = SCRCPL + 3
        CPL = SCRPMA[SCRCPL:SCRPQIBP]
        SCRPQIBP = SCRPQIBP + 5
        PQIBP = SCRPMA[SCRPQIBP:SCRPQIWK]
        SCRPQIWK = SCRPQIWK + 5
        PQIWK = SCRPMA[SCRPQIWK:SCRWBPBCB]
        SCRWBPBCB = SCRWBPBCB + 6
        WBPBCB = SCRPMA[SCRWBPBCB:SCRTOTTCQ]
        SCRTOTTCQ = SCRTOTTCQ + 6
        TOTTCQ = SCRPMA[SCRTOTTCQ:SCRBOC]
        SCRBOC = SCRBOC + 3
        BOC = SCRPMA[SCRBOC:SCREXP]
        SCREXP = SCREXP + 3
        EXP = SCRPMA[SCREXP:SCREXPR]
        SCREXPR = SCREXPR + 4
        EXPR = SCRPMA[SCREXPR:SCRSMLLP]
        SCRSMLLP = SCRSMLLP + 5
        SMLLP = SCRPMA[SCRSMLLP:SCRMEDP]
        SCRMEDP = SCRMEDP + 4
        MEDP = SCRPMA[SCRMEDP:SCRLARGEP]
        SCRLARGEP = SCRLARGEP + 6
        LARGEP = SCRPMA[SCRLARGEP:SCREMINA]
        SCREMINA = SCREMINA + 5
        EMINA = SCRPMA[SCREMINA:SCREMA]
        SCREMA = SCREMA + 3
        EMA = SCRPMA[SCREMA:SCREMH]
        SCREMH = SCREMH + 3
        EMH = SCRPMA[SCREMH:SCRFOOD]
        SCRFOOD = SCRFOOD + 4
        FOOD = SCRPMA[SCRFOOD:SCRKEY]
        SCRKEY = SCRKEY + 3
        KEY = SCRPMA[SCRKEY:SCRCQ]
        SCRCQ = SCRCQ + 3
        CCQ = SCRPMA[SCRCQ:]
        ## Prints The Loaded Values
        print("")
        print(" LOADED STATS ")
        print("")
        print(" PMA " + str(PMA))
        print(" PMINA " + str(PMINA))
        print(" PMD " + str(PMD))
        print(" PMIND " + str(PMIND))
        print(" PMH " + str(PMH))
        print(" PH " + str(PH))
        print(" CRTC " + str(CRTC))
        print(" CRTM " + str(CRTM))
        print(" PGT " + str(PGT))
        print(" DM " + str(DM))
        print(" CPL " + str(CPL))
        print(" PQIBP " + str(PQIBP))
        print(" PQIWK " + str(PQIWK))
        print(" WBPBCB " + str(WBPBCB))
        print(" TOTTCQ " + str(TOTTCQ))
        print(" BOC " + str(BOC))
        print(" EXP " + str(EXP))
        print(" EXPR " + str(EXPR))
        print(" SMLLP " + str(SMLLP))
        print(" MEDP " + str(MEDP))
        print(" LARGEP " + str(LARGEP))
        print(" EMINA " + str(EMINA))
        print(" EMA " + str(EMA))
        print(" EMH " + str(EMH))
        print(" FOOD " + str(FOOD))
        print(" KEY " + str(KEY))
        print(" CCQ " + str(CCQ))
        print("")
        ## Changes The Values To Integers So The Code Wont Hit A Base 10 Value Error
        EXP = int(EXP)
        EXPR = int(EXPR)
        PH = int(PH)
        PMH = int(PMH)
        SMLLP = int(SMLLP)
        MEDP = int(MEDP)
        LARGEP = int(LARGEP)
        FOOD = int(FOOD)
        KEY = int(KEY)
        EMA = int(EMA)
        EMINA = int(EMINA)
        EMH = int(EMH)
        PMINA = int(PMINA)
        PMA = int(PMA)
        PMH = int(PMH)
        PH = int(PH)
        PMD = int(PMD)
        PMIND = int(PMIND)
        CRTC = int(CRTC)
        CRTM = int(CRTM)
        PGT = int(PGT)
        BOC = int(BOC)
        TOTTCQ = int(TOTTCQ)
        WBPBCB = int(WBPBCB)
        PQIBP = int(PQIBP)
        PQIWK = int(PQIWK)
        CPL = int(CPL)
        DM = int(DM)
        CCQ = int(CCQ)
        print(" Press Enter To Continue")
        input("")
## Definition For The Tavern Interior
def TAVERNI():
    global CCQ 
    global ITLOC
    global PCBILOC
    global PH
    global PMH
    global TOTTCQ
    global PGT
    global PMINA
    global PMA
    global BOC
    global TOTTLOC
    global TOTTQS
    global PMID
    global WBPBCB
    global PMD
    global PAWBF
    global WBPBQA
    ITLOC = 1
    while ITLOC == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(" _____________________________")
        print(" |   |____|         0 |||    |")
        print(" |                  o ||| 0  |")
        print(" |   [3] fireplace  0 ||||==||")
        print(" |                           |")
        print(" |                 [1] bar   |")
        print(" |          o                |")
        print(" |        o O o              |")
        print(" |          o           o    |")
        print(" |                    o O o  |")
        print(" |    o    [4] tables   o    |")
        print(" |  o O o               ||||||")
        print(" |    o                 ||||||")
        print(" |              [2] upstairs |")
        print(" |_| |_______________________|")
        print("")
        print(" [1] Bar")
        time.sleep(.5)
        print(" [2] Head Upstairs")
        time.sleep(.5)
        print(" [3] Check Out The Fireplace")
        time.sleep(.5)
        print(" [4] Go And See Who Is At The Tables")
        time.sleep(.5)
        print(" [5] Leave The Tavern")
        time.sleep(.5)
        print("")
        PMCIT = input("")
        if PMCIT == "1":
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Head To The Bar.")
            time.sleep(1)
            print(" 'What Can I Get Ya?' The Bartender Asks You ")
            time.sleep(1)
            PCBILOC = 1
            while PCBILOC == 1:
                print("")
                print(" [1] A Beer  [" + str(PGT) + " / 3 Sepi]" )
                print(" [2] Nothing, Im Good, I Was Just Cheking This Place Out ")
                time.sleep(.5)
                PBCI = input("")
                if PBCI == "1" and PGT >= 3:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("")
                    print(" The Bar Tender Hands You A Mug Full Of Amber Colored Liquid With Snow White Colored Foam At The Top")
                    time.sleep(1)
                    PGT = PGT - 3
                    PHAH = random.randint(1,5)
                    if PH + PHAH <= PMH:
                        print("")
                        print("You Healed " + str(PHAH) + " HP")
                        PH = PH + PHAH
                        print(" Your Total Health Is: " + str(PH) + " / " + str(PMH) + " HP")
                    elif PH + PHAH > PMH:
                        print("")
                        print(" You Could Not Heal Fully So You Are Now At Your Maximum Health")
                        PH = PMH
                    if CCQ == "D10B":
                        BD = BD + 1
                        if BD == 10:
                            time.sleep(.5)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            CCQ = D10BCOMP
                            print("")
                            print(" You Have Drank 10 Beers, Go Back To The Game Master ")
                            time.sleep(.5)
                            print("")
                            print(" Press Enter To Continue")
                            input("")
                    time.sleep(1)
                    print("")
                    print("Press Enter To Continue")
                    input("")
                elif PBCI == "1" and PGT < 3:
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("")
                    print(" You Do Not Have Enough Sepi For This")
                    time.sleep(.5)
                    print("")
                    print("Press Enter To Continue")
                    input("")
                elif PBCI == "2":
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("")
                    print(" You Walk Away From The Bar ")
                    print("")
                    print(" Press Enter To Continue")
                    input("")
                    PCBILOC = 0
        elif PMCIT == "2":
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Head Upstairs")
            print(" This Feature Is Not Yet Implemented")
            print(" Press Enter To Continue")
            input()
        elif PMCIT == "3":
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Go To The Fire And Warm Up")
            if PAWBF == 0 and PH + 20 <= PMH:
                print(" You Healed 20 HP!")
                PH = PH + 20
                PAWBF = 1
            print(" Press Enter To Continue ")
            input("")
        elif PMCIT == "4":
            TTPLOC = 1
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Go And Check Out Who Is At The Tables")
            time.sleep(.5)
            print(" INDEV: THERE WILL BE MORE ADDED TO THIS BUT FOR THE TIME BEING THIS IS IT.")
            time.sleep(1)
            print(" You See Multiple People That Look Like They Might Be Worth Talking To.")
            time.sleep(.5)
            while TTPLOC == 1:
                print("")
                print(" [1] The Game Master")
                print(" [2] Chadwick Baldwin The || ")
                print(" [3] Panic Stricken Old Lady ")
                print(" [4] Walk Away")
                print("")
                TTP = input("")
                if TTP == "1":
                    time.sleep(.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(" You Go And Talk To The Game Master... ")
                    time.sleep(1.5)
                    print(" As You Approach Him, He Says 'Who Are YOU?, You Dont Look Like You Would Be Worth My Time, Go Away' ")
                    time.sleep(1.5)
                    print("")
                    print(" Press Enter To Continue")
                    input("")
                    if CPL >= 10:
                        time.sleep(.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" Wait")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" Wait.")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" Wait..")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" Wait...")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" You Might Be Worth My Time, I Just Need You To Make Sure You Have Money And Endurance,")
                        time.sleep(1.5)
                        print(" Go Buy And Drink 10 Beers From The Bartender")
                        time.sleep(1.5)
                        input("")
                        CCQ = "D10B"
                    else:
                        time.sleep(.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" You Walk Away Not Knowing Why He Didn't Want Your Time.")
                    time.sleep(.5)
                    print("")
                    print(" Press Enter To Continue")
                    input("")
                elif TTP == "2":
                    time.sleep(.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("")
                    print(" You Start Walking Over To A Iron Cladded Person")
                    time.sleep(.5)
                    print(" The Man, Gets Up And Faces You.")
                    time.sleep(.5)
                    print(" 'Why Do You Look So Feeble And Wimp-Like?' The Man Asked,")
                    time.sleep(.5)
                    print(" Before You Can Even Respond, He Says 'You Look Far To Feeble For These Halls, You Should Do Me A Favor ")
                    time.sleep(.5)
                    print("")
                    print(" Press Enter To Continue")
                    if PQIBP == 1 and PQIWK == 1:
                        PQITI = 1
                        while PQITI == 1:
                            print(" WAIT, Its You!")
                            time.sleep(1)
                            print(" Do You Have My Families Sword?")
                            time.sleep(1)
                            print("")
                            print(" [1] Yes, Here It Is [Hand In The Body Pillow The Weeb Was Using As A Sword] ")
                            print(" [2] Yes, Here It Is [Hand In The Katana The Weeb Had On His Back]")
                            print("")
                            PQITIWBPB = input("")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("")
                            print(" WAIT!, This Isnt What I Asked For!, I Told You To Kill Jeremy, Not James!")
                            print(" These Things Are James! ")
                            time.sleep(1)
                            if PQITIWBPB == "1":
                                print(" Well... Since You Killed James Ill, Keep His Body Pillow As A Momento As He Was A Dear Friend")
                                print(" You Kept The Katana, ")
                                WBPBCB = 1
                                CCQ = 0
                                PMINA = PMINA + 5
                                PMA = PMA + 5
                                time.sleep(1)
                                print(" Your Minimum And Maximum Attack Have Increased By 5")
                            elif PQITIWBPB == "2":
                                print(" Well... Since You Killed James, Ill Keep His Prized Katana As A Momento As He Was A Dear Friend")
                                print(" You Kept The Body Pillow, Since He Did Not Want It.")
                                WBPBCB = 1
                                CCQ = 0
                                PMIND = PMIND + 5
                                PMD = PMD + 5
                                time.sleep(1)
                                print(" Your Minimum And Maximum Defence Have Increases By 5")
                    WBPBQALOC = 1
                    input("")
                    if CCQ != 0 and CCQ != "WBPB":
                        print(" But, It Looks Like You Are Busy With Another Quest. ")
                    if WBPBQALOC == 1 and CCQ == 0 and WBPBCB == 0:
                        print("")
                        print(" [1] Sure, What Do You Need Me To Do? ")
                        print(" [2] (Leave) Nah, Maybe Later, You Are Kinda Ugly, Quit Being Ugly")
                        print("")
                        WBPBQA = input("")
                        if WBPBQA == "1":
                            time.sleep(.5)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            CCQ = "WBPB"
                            print("")
                            print(" Ah! So Here's What You Need To Do You Wimp, Go And Get My Family Sword From The Weeb")
                            time.sleep(.5)
                            print(" It Should Be Easy For You Even Though You Are A Feeble Wimp")
                        elif WBPBQA == "2":
                            time.sleep(.5)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("")
                            print(" What A Grave Mistake My Friend, You Need The Expertise")
                            time.sleep(.5)
                            print(" But, I Shall Leave You To Your Devices. Come Back To Me When You Want To Be Strong And Mighty")
                elif TTP == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(.5)
                    if BOC == 0:
                        print("")
                        print(" As You Walk Up To The Old Lady, You See Her Talking To Another Person ")
                        time.sleep(.5)
                        print(" Im Sorry Kind Sir, You Do Not Look Strong Enough To Help My Child. The Other Person Walks Away In Defeat After Hearing What The Old Lady Said ")
                        time.sleep(2)
                        print(" You Walk Up To Her")
                        if CPL <= 7:
                            TOTTLOC = 1
                            while TOTTLOC == 1 and TOTTCQ == 0:
                                print(" Ah! You Look Like A Strong Person, Could You Help Find My Child? ")
                                print("")
                                if CCQ == 0:
                                    print(" [1] Of Course Madam, What Do You Need?")
                                    print(" [2] Only If You Pay Me You Old Hag")
                                    print(" [3] (Leave) No, Your Child Can Help Themselves.")
                                    print("")
                                    TOTTQS = input("")
                                    if TOTTQS == "1" or "2":
                                        time.sleep(.5)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("")
                                        print(" Oh, Thank You Dearie, Go Find My Child, He Is In The Halls, I Am Worried About Him")
                                        CCQ = "TOTT"
                                        TOTTLOC = 0
                                    elif TOTTQS != "1" or "2" or "3":
                                        TOTTLOC = 1
                                    elif TOTTQS == "3":
                                        TOTTLOC = 0
                                        time.sleep(.5)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("")
                                        print(" Oh, I Know Your Angry, Please Come Back Once You Are Ready, I Need You Help, I Beg Of You")
                                        print("")
                                        print(" Press Enter To Continue")
                                elif CCQ != 0:
                                    time.sleep(.5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(CCQ)
                                    print(" Oh, Nevermind, It Looks Like You Are Busy Right Now, Please Come Back When You Are Done ")
                                    print("")
                                    TOTTLOC = 0
                                    time.sleep(.5)
                                    print(" Press Enter To Continue")
                                    input("")
                    elif BOC == 1:
                        time.sleep(.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("")
                        print(" You Head Up To The Old Lady, And Show Her The Bag Of Candy, You Ask If Her Kid Liked Candy, She Freaks Out")
                        time.sleep(1)
                        print(" What The Hell Is Wrong With You! ")
                        time.sleep(1)
                        print(" You Killed My Child! ")
                        time.sleep(.5)
                        print("")
                        print(" [1] Sorry, I Had No Way Of Knowing It Was Your Kid")
                        print(" [2] So? He Was A Little Shit, Hell, I Basically Punted Him Halfway Across The Hall. Serves Him Right. ")
                        time.sleep(.5)
                        print(" Fair, He Was A Ugly Child Anyways. Have A Piece Of Candy! ")
                        CCQ = 0
                        TOTTCQ = 1
                    elif CPL >= 6:
                        print(" Did You Not Hear What I Said To The Other Person? You Are Not Strong Enough To Help My Child. Come Back When You Are Stronger ")
                        print("")
                        print(" Press Enter To Continue")
                        input("")
                elif TTP == "4":
                    TTPLOC = 0
        elif PMCIT == "5":
            TLOC = 0
            ITLOC = 0
            PAWBF = 0
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Left The Tavern")
            print("")
            print(" Press Enter To Continue ")
            input("")
    
## Definition For The Tavern
def TAVERN():
    global CPL
    global PGT
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    ## ASCII Art For The Tavern
    print("")
    print("              }[  ")
    print("             ]{  ")
    print("            { ]    ")
    print("          __     ")
    print("          ||     ")
    print("          ||/\   ")
    print("          ||\_\   ")
    print("         _||_\_\_   ")
    print("        /\_\_\_\_\   ")
    print("       /\_\_\_\_\_\   ")
    print("     _/\_\_\_\_\_\_\_   ")
    print("    /\_\_\_\_\_\_\_\_\   ")
    print("   /\_\_\_\_\_\_\_\_\_\   ")
    print("  /|   |=|  |=|  |=|  |\   ")
    print("   |                  |  ")
    print("   |   |=|  |=|  |=|  |  ")
    print("   |  ___             |  ")
    print("   |  |+|   |+|  |+|  |  ")
    print("   ---| |--------------  ")
    print("")
    print(" Your Found A Tavern! ")
    time.sleep(.5)
    TLOC = 1
    while TLOC == 1:
        print(" [1] Go Inside ")
        print(" [2] Walk Away And Continue Your Adventure ")
        EOLT = input("")
        if EOLT == "1":
            TLOC = 0
            TAVERNI()
        elif EOLT == "2":
            TLOC = 0
    
## Quest Manager Hud
def QM():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("     ------------- ")
    print("     |   Quests  | ")
    print("     ------------- ")
    if CCQ == 0:
        print("")
        print(" _^__________^_")
        print(" | No Current }")
        print(" ;   Quest    |")
        print(" ---=----~~-=--")
    elif CCQ == "WBPB":
        print("")
        print("   _^__________________^_       _^________________________^_")
        print("   | Weebs, Body        }       { Go Find And Kill The Weeb:")
        print("   { Pillows, And Blood :       { Turn In The Family Sword |")
        print("   --=---~-----=~--=--~--       -----==----~----=-------~~--")
    elif CCQ == "TOTT":
        print("")
        print("   _^__________________^_       _^________________________^_")
        print("   | Trick Of The Treat }       { Go Find The Old Ladie's  :")
        print("   {                    :       { Child.                   |")
        print("   --=---~-----=~--=--~--       -----==----~----=-------~~--")
    elif CCQ == "D10B":
        print("")
        print("                    __^_")
        print("            _______/   | ")
        print("   _^______/ B#er#     | ")
        print("  | Dri#k #0  e  s  =~-|")
        print("  |    n  1~~~=-~~-/")
        print("  |~--====/")
    print("Press Enter To Continue")
    input("")
    
    ## Supply Room Setup
def WRR():
    global SMLLP
    global LARGEP
    global EXP
    global FOOD
    global PH
    global PMH
    global BUCK
    global EXPR
    global EXPGFC
    global KEY
    global MEDP
    global WEALEA
    global MILLEA
    global POTLEA
    os.system('cls' if os.name == 'nt' else 'clear')
    print("~~~~~~~~~~~~~")
    time.sleep(1)
    print("!!!")
    time.sleep(1)
    print(" You found a room with shelves filled with poultices and herbs and potions. You grab some of them for the long trip ahead ")
    input("Press Enter To Continue")
    ## Determins How Many Potions The Player Finds
    SMPG = random.randint(1,2)
    MEDPG = random.randint(0,2)
    LRGEPG = random.randint(0,1)
    ## Determines How Many Of The Potion Leaves Are Found
    WEALEAG = random.randint(1,6)
    MILLEAG = random.randint(0,4)
    POTLEAG = random.randint(0,3)
    ## Tells The Player What They Have Found
    print(" You Found " + str(SMPG) + " Small Potions ")
    time.sleep(.3)
    print(" You Found " + str(MEDPG) + " Medium Potions ")
    time.sleep(.3)
    print(" You Found " + str(LRGEPG) + " Large Potions ")
    time.sleep(.3)
    print(" You Found " + str(WEALEAG) + " Weak Leaves ")
    time.sleep(.3)
    print(" You Found " + str(MILLEAG) + " Mild Leaves ")
    time.sleep(.3)
    print(" You Found " + str(POTLEAG) + " Potent Leaves ")
    time.sleep(.3)
    ## GIves The Player What They Found
    SMLLP = SMLLP + SMPG
    MEDP = MEDP + MEDPG
    LARGEP = LARGEP + LRGEPG
    WEALEA = WEALEA + WEALEAG
    MILLEA = MILLEA + MILLEAG
    POTLEA = POTLEA + POTLEAG
    
    input("Press Enter To Continue")
    ## Determines What Room Will Be Added On To The Supply Room
    ## If It Does Not Equal 1, 2, Or 3, There Is No Extra Room
    KRC = random.randint(1,8)
    ## Room For Locked Chest
    if KRC == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(" You Found A Locked Chest!")
        if KEY >= 1:
            print(" Do You Want To Use A Key To Open It?")
            print(" [1] Yes")
            print(" [2] No")
            OLCWK = input("")
            ## Gives THe Player An Option To Use A Key To Open A Chest And Gain XP
            if OLCWK == "1":
                KEY = KEY - 1
                print(" You Used A Key To Open The Chest!")
                EXPGFC = random.randint(300,900)
                print(" You Have Gained " + str(EXPGFC) + " XP!")
                EXP = EXP + EXPGFC
                input(" Press Enter To Continue")
            elif OLCWK == "2":
                print(" You Decide Not To Use A Key And Go On Your Merry Way")
                input(" Press Enter To Continue")
    ## Room For Water Related Content. (More Coming In The Future)
    elif KRC == 2:
        ## The Bucket Room, Player Has Many Choices
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("You found a room full of buckets. How Strange.")
        time.sleep(1)
        print("You look into the buckets and see they are full of water.")
        time.sleep(1)
        print("Why would someone just have random buckets of water in a room?")
        time.sleep(1)
        print("")
        print("[1] Leave And Ignore The Random Buckets Of Water ")
        print("[2] Waste Not Want Not. Douse Yourself With Water ")
        print("[3] Empty Out The Bucket And Take It With You ")
        PIIBR = input("")
        if PIIBR == "1":
            ## The Player Can Choose To Leave And Gain Nothing
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You leave this strange room. Screw Water. It never did anything for you anyway.")
        elif PIIBR == "2":
            ## Runs A Random Chance To Either Heal The Player And Increase Their Max HP Or Heal The Player And Lower Their Max HP
            PWC = random.randint(1,3)
            if PWC == 1:
                time.sleep(.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You decide to douse yourself with water. Why not? Your gonna die at some point. Live your life")
                print("The Water Was Super Clean And Felt Refreshing")
                input("Press enter to continue")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You Gained 15 HP!")
                time.sleep(.5)
                print("But")
                time.sleep(.5)
                print("You Gained 5 Max HP")
                input("Press Enter To Continue")
                PH = PH + 15
                PMH = PMH + 5
            elif PWC == 2 or PWC == 3:
                time.sleep(.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You decide to douse yourself with water. Why not? Your gonna die at some point. Live your life")
                input("Press enter to continue")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You Gained 10 HP!")
                time.sleep(.5)
                print("But")
                time.sleep(.5)
                print("You Lost 5 Max HP")
                input("Press Enter To Continue")
                PH = PH + 10
                PMH = PMH - 5
        ## Lets The PLayer Empty Out The Bucket And Let Them Use It For Brewing Potions
        elif PIIBR == "3":
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" You Empty Out The Bucket And Take It With You")
            BUCK = BUCK + 1
            print("")
            print(" You Now Have " + str(BUCK) + " Buckets")
            time.sleep(.5)
            print("")
            print(" Press Enter To Continue")
            input("")
            
    ## Banquet Room Used For Gaining Food.
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You find a very long room with a scarlet red banquet table full of food.")
        time.sleep(2)
        print("The table cloth on the table was highlighted with streaks of emerald cloth")
        time.sleep(2)
        print("You decide that some food woud be good to find and eat but what if that food is poisoned?")
        time.sleep(2)
        print("[1] Grab as much food as you can carry")
        print("[2] Dont grab any food incase it is in fact poisoned")
        GFABT = input("")
        if GFABT == "1":
            ## Rolls To See If The Food Was Poisoned Or Not
            BTFIPC = random.randint(1,4)
            ## If It Rolls A 1, The Food Will Be Poisoned
            if BTFIPC == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                print("")
                print("The food was poisoned")
                time.sleep(1)
                print(" You Lost 10 Max Health")
                ## Decreases Players Max Health By Given Value
                PMH = PMH - 10
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You grab as much food as you can carry.")
                AOFG = random.randint(4,6)
                print("You grabbed " + str(AOFG) + " plates of food")
                FOOD = FOOD + AOFG
    ## Combat System
def ECA():
    ## Varibles For Enemy Sprites
    global ESL1G
    global ESL2G
    global ESL3G
    global ESL1LR
    global ESL2LR
    global ESL3LR
    global ESL1S
    global ESL2S
    global ESL3S
    global ESL1HWOC
    global ESL2HWOC
    global ESL3HWOC
    global ESL1WBR
    global ESL2WBR
    global ESL3WBR
    global ESL1BD
    global ESL2BD
    global ESL3BD
    global ESL1CB
    global ESL2CB
    global ESL3CB
    global ESL1AOD
    global ESL2AOD
    global ESL3AOD
    global ESL1FVC
    global ESL2FVC
    global ESL3FVC
    global PMINA
    global PMA
    global CSCF
    global PH
    global PMH
    global EXP
    global EXPR
    global F
    global EMH
    global CCQ
    global EMA
    global EMINA
    global PGT
    global SPQ
    ## Determines What The Enemy's Name Will Be
    ETS = random.randint(1,9)
    ## All Possible Enemy Names (More Will Be Added)
    if ETS == 1:
        ET = "Goblin's"
        ESL1 = ESL1G
        ESL2 = ESL2G
        ESL3 = ESL3G
    elif ETS == 2:
        ET = "Large Rat's"
        ESL1 = ESL1LR
        ESL2 = ESL2LR
        ESL3 = ESL3LR
    elif ETS == 3:
        ET = "Slime's"
        ESL1 = ESL1S
        ESL2 = ESL2S
        ESL3 = ESL3S
    elif ETS == 4:
        ET = "Heretical Wheel Of Cheese's"
        ESL1 = ESL1HWOC
        ESL2 = ESL2HWOC
        ESL3 = ESL3HWOC
    elif ETS == 5:
        ET = "Rat Stuck In A Wet Paper Bag's"
        ESL1 = ESL1WBR
        ESL2 = ESL2WBR
        ESL3 = ESL3WBR
    elif ETS == 6:
        ET = "Basement Dweller's"
        ESL1 = ESL1BD
        ESL2 = ESL2BD
        ESL3 = ESL3BD
        if CCQ == "WBPB":
            WCIOBD = random.randint(1,3)
            if WCIOBF == 1:
                ESL1 = "M'lady"
                ESL2 = "*Tips Fedora*"
                ESL3 = "YOU CANT POSSIBLY DEFEAT ME!"
                SPW = 1
    elif ETS == 7:
        ET = "Chadwick Baldwin The |||'s"
        ESL1 = ESL1CB
        ESL2 = ESL2CB
        ESL3 = ESL3CB
    elif ETS == 8:
        ET = "Frail Victorian Child's"
        ESL1 = ESL1FVC
        ESL2 = ESL2FVC
        ESL3 = ESL3FVC
    elif ETS == 9:
        ET = "'Get Off My Lawn'- Angry Old Dude's"
        ESL1 = ESL1AOD
        ESL2 = ESL2AOD
        ESL3 = ESL3AOD
    ## HUD For Combat
    while CSCF == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| |" + str(PH) + " / " + str(PMH) + " | | " + str(EH) + " / " + str(EMH) + "|   ")
        print("|   Your HP  | | " + str(ET) + " HP  |")
        print("| [1] Attack                ")
        print("| [2] Flee               " + str(ESL1))
        print("|                        " + str(ESL2))
        print("|                        " + str(ESL3))
        print("|                           ")
        print("|                           ")
        print("|                           ")
        print("|                           ")
        print("|                           ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        CSPC = input("")
        ## Attack System For Both Enemy And Player. It Utilizes Their Min And Max Attack Values
        if CSPC == "1":
            PAA = random.randint(PMINA,PMA)
            ## Rolls For Your Critical Chance
            CRTCR = random.randint(1,100)
            ## Critical Hit Chance And Multiplier System
            if CRTCR <= CRTC:
                PAA = PAA * CRTM
            EH = EH - PAA
            EA = random.randint(EMINA,EMA)
            ## Chooses A Random Number For The Total Defence Roll
            PDR = random.randint(PMIND,PMD)
            ## Factors In The Defence Roll And Applies It
            PDT = EA - PDR
            ## Checks To See If The Damage Dealt To The Playe Is 0 Or Below
            if PDT <= 0:
                time.sleep(1)
            else:  
                PH = PH - PDT
        ## Flee System (Might Be Implemented So You Would Have A Chance To Flee Combat)
        elif CSPC == "2":
            print(" You can't flee a fight!")
            time.sleep(1)
            print(" COWARD!")
            time.sleep(1)
        ## System That Determines If The Enemy Is Dead Or Not
        if EH <= 0:
            CSCF = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You Won The Fight!")
            time.sleep(1)
            ## Chooses A Random Number For The Amount Of EXP Gained
            EXPGFC = random.randint(70,150)
            print(" You Gained " + str(EXPGFC) + " XP!")
            EXP = EXP + EXPGFC
            GGFC = random.randint(2,5)
            print(" You Also Gained " +str(GGFC) + " Sepi's")
            PGT = PGT + GGFC
            time.sleep(2)
            ## Checks To See If The Player Had The Quest For This Encounter And If The Enemy Was A Basement Dweller
            if CCQ == "WBPB" and ET == "Basement Dweller's":
                ## Gives The Player The Quest Items
                PQIBP = 1
                PQIWK = 1
                time.sleep(.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print(" The Weeb Dropped His Weapons When He Died...")
                time.sleep(1)
                print(" He Had A Body Pillow, That He Was Beating You Up With...")
                time.sleep(1)
                print(" And His Katana, (Looks Pretty Fake To Me) ")
                time.sleep(1)
                print(" Press Enter To Continue")
                input("")
            ## Checks To See If The Player Had The Required Quest And If The Enemy Was A Frail Victoran Child
            elif CCQ == "TOTT" and ET == "Frail Victorian Child's":
                ## GIves The Player The Quest Items
                BOC == 1
                time.sleep(.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print(" Once You Killed The Child, He Dropped A Strange Bag ")
                time.sleep(.5)
                print(" I Should Head To The Tavern And Ask The Old Lady If Her Kid Likes Candy ")
            ## System That Increases The Enemy's Difficulty
            EMH = EMH + random.randint(5,10)
            EH = EMH
            EMINA = EMINA + random.randint(1,2)
            EMA = EMA + random.randint(2,4)
        ## Determines If Player Is Dead
        if PH <= 0:
            ## Kills The Game So The Player Is Forced To Restart The Code
            GC = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(.5)
            print("")
            print(" GAME OVER")
            print(" You Died!")
            print("")
            print(" Please Stop And Start The Game")
            EGFL = 1
            while EGFL == 1:
                HGFL = 1
            
    ## Inventory System
def INVENTORY():
    global SMLLP
    global MEDP
    global PH
    global LARGEP
    global KEY
    global BUCK
    global FOOD
    ## Key For What All The Symbols Mean (Will Be More Important After Later Updates)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    ## Shows A Item Key To What Is What
    print("Key:")
    time.sleep(.1)
    print("X = Empty Slot")
    time.sleep(.1)
    print("i = Small Potion ")
    time.sleep(.1)
    print("l = Medium Potion ")
    time.sleep(.1)
    print("I = Large Potion ")
    time.sleep(.1)
    print("t = Key ")
    time.sleep(.1)
    print("u = Bucket")
    time.sleep(.1)
    print("U = Large Bucket")
    time.sleep(.1)
    print("0 = Food")
    print("")
    print("[1] Continue to inventory")
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')
    ## Shows Values For Each Item And Consumable The pLayer Picks Up
    print("")
    time.sleep(.1)
    print("i : " + str(SMLLP))
    time.sleep(.1)
    print("l : " + str(MEDP))
    time.sleep(.1)
    print("I : " + str(LARGEP))
    time.sleep(.1)
    print("t : " + str(KEY))
    time.sleep(.1)
    print("u : " + str(BUCK))
    time.sleep(.1)
    print("0 : " + str(FOOD))
    time.sleep(.1)
    print("")
    print(" [1] Exit Inventory ")
    print(" [2] Use An Item ")
    print(" [3] Brew A Potion ")
    INVCON = input("")
    if INVCON == "1":
        print("")
    elif INVCON == "2":
        INVCONUSE = 1
        ## Inventory Consumable Menu
        while INVCONUSE == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            print(" What Item Do You Want To Use?       Your HP -->    " + str(PH) + " / " + str(PMH))
            print("")
            time.sleep(.1)
            print(" [1] i : " + str(SMLLP))
            time.sleep(.1)
            print(" [2] l : " + str(MEDP))
            time.sleep(.1)
            print(" [3] I : " + str(LARGEP))
            time.sleep(.1)
            print(" [4] t : " + str(KEY))
            time.sleep(.1)
            print(" [5] u : " + str(BUCK))
            time.sleep(.1)
            print(" [6] 0 : " + str(FOOD))
            time.sleep(.1)
            print(" [7] Exit Inventory")
            time.sleep(.5)
            INVCONSEL = input("")
            ## If And Elif Statements For Consuming Consumables
            if INVCONSEL == "1" and SMLLP != 0:
                print(" You drank the potion")
                HPR = random.randint(5,10)
                if PH == PMH:
                    print(" But You Cant Heal! You Are Already At Max Health!")
                elif PH + HPR > PMH:
                    print(" You regained " + str(HPR) + " HP")
                    print(" But You Only Healed To Max Health")
                    PH = PMH
                elif PH + HPR <= PMH:
                    print(" You regained " + str(HPR) + " HP")
                    PH = PH + HPR
                time.sleep(.5)
                print(" Press enter to continue")
                input("")
                SMLLP = SMLLP - 1
            elif INVCONSEL == "2" and MEDP != 0:
                print(" You drank the potion")
                HPR = random.randint(10,20)
                if PH == PMH:
                    print("You Cant Heal! You Are ALready At Max Health!")
                elif PH + HPR > PMH:
                    print(" You regained " + str(HPR) + " HP")
                    print(" But You Only Healed To Max Health")
                    PH = PMH
                elif PH + HPR <= PMH:
                    print(" You regained " + str(HPR) + " HP")
                    PH = PH + HPR
                time.sleep(.5)
                print(" Press enter to continue")
                input("")
                MEDP = MEDP - 1
            elif INVCONSEL == "3" and LARGEP != 0:
                LARGEP = LARGEP - 1
                print(" You drank the potion")
                HPR = random.randint(15,30)
                if PH == PMH:
                    print("You Cant Heal! You Are ALready At Max Health!")
                elif PH + HPR > PMH:
                    print(" You regained " + str(HPR) + " HP")
                    print(" But You Only Healed To Max Health")
                    PH = PMH
                elif PH + HPR <= PMH:
                    print(" You regained " + str(HPR) + " HP")
                    PH = PH + HPR
                time.sleep(.5)
                print(" Press enter to continue")
                input("")
            elif INVCONSEL == "4" and KEY != 0:
                print(" You cant eat keys")
            elif INVCONSEL == "5" and BUCK != 0:
                print(" You cant eat buckets")
            elif INVCONSEL == "6" and FOOD != 0:
                FOOD = FOOD - 1
                HPR = random.randint(1,5)
                PH = PH + HPR
                time.sleep(.5)
                print(" You ate the food and regained " + str(HPR) + " HP" )
                time.sleep(.5)
                print(" Press enter to continue")
                input("")
            elif INVCONSEL == "7":
                INVCONUSE = 0
    elif INVCON == "3":
        HPS()
## Basic Stats Screen For The Players Stats
def STATS():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("Player Attack Min: " + str(PMINA) + " Max: " + str(PMA) )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("Player Health Current: " + str(PH) + " Max: " + str(PMH))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("Player Defence Min: " + str(PMIND) + " Max: " + str(PMD))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("Player Critical Chance: " + str(CRTC))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("Player Critical Multiplier: " + str(CRTM))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(.5)
    print("[1] Exit Stats")
    input("")
## Shows The HUD When It Is Called. This Is The HUD Layout And Main Control Area For The Game
def HUDON():
    global CPL
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(" /~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ")
    print("  / / / HALL/USER/MENU / / /")
    print(" \~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
    print("")
    print(" /~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ")
    print("     _")
    print("    /|\ ")
    print("    |||   " + str(PH) + " / " + str(PMH) + " HP ") 
    print("    |||   " + str(EXP) + " / " + str(EXPR) + " XP ")
    print("    |||   Distance Traveled: " + str(DM) + "M ")
    print("    |||   Sepi: " + str(PGT) + "  ")
    print("    |||   Level: " + str(CPL) + " ")
    print("    \|/ ")
    print("")
    print(" \~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
    print("")
    print(" /~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ") 
    print("     _")
    print("    /|\ ")
    print("    |||   [1] Move Forward")
    print("    |||   [2] Stats")
    print("    |||   [3] Inventory")
    print("    |||   [4] Options")
    print("    |||   [5] Quests")
    print("    \|/")
    print("")
    print(" \~~~~~~~~~~~~~~~~~~~~~~~~~~~~/ ")
    print("")
## Same Thing As HUD ON But Is More Bare Bones (Will Implement HUD Off For Other Menus Of The Game)
def HUDOFF():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("PH " + str(PH))
    print("PMH " + str(PMH))
    print("1 Move Forward")
    print("2 Stats")
    print("3 Inventory")
    print("4 Options")
    print("5 Quests")
## Settings That The Player Can Access
def OPTIONS():
    global HOOO
    global GC
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(" /~~~~~~~~~~~~~~~~\ ")
    print(" [1] HUD Toggle ")
    print(" [2] Exit Options")
    print(" [3] Save And Load")
    print(" [4] Quit Game")
    print("\~~~~~~~~~~~~~~~~/")
    print("")
    OPC = input("")
    ## Toggles HUD On And Off
    if OPC == "1":
        if HOOO == "1":
            HOOO = "2"
        elif HOOO == "2":
            HOOO = "1"
    ## Leaves The Settings Page
    elif OPC == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif OPC == "3":
        GSCD()
    elif OPC == "4":
        GC = 0
            
# Code That Runs The Game
BG = input("Boot? Y/N ")
os.system('cls' if os.name == 'nt' else 'clear')
## Disclaimers And Info
print("DISCLAMER! This game will have satire and dark humor. None of this is meant to be offensive. Please take this game with a grain of salt")
time.sleep(.1)
print("This is not an easy game. You WILL die. You Have Been Warned.")
time.sleep(.1)
print("This Game Was Made By: Samuel Waters AKA: Rev2saws")
time.sleep(.1)
print("Special Thanks To:")
time.sleep(.1)
print("")
input("Press Enter To Continue")
os.system('cls' if os.name == 'nt' else 'clear')
## Fancy Method Of Booting, Mainly ASCII
## The // Lets Me Skip The Boot Screen So I Can Test Stuff Faster, Same For AS
if BG != "//" or "TS" or "AS":
    if BG == "TS":
        TAVERN()
    elif BG == "AS":
        ECA()
        input("")
    time.sleep(1)
    if BG != "//":
        RNBP = random.randint(2,8)
        for i in range(RNBP):
            print("")
            print("")
            print("   Booting /")
            time.sleep(.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("   Booting -")
            time.sleep(.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("   Booting \ ")
            time.sleep(.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("   Booting | ")
            time.sleep(.3)
            os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("")
        print("    Booted!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ## Version Info And INDEV Info
        print("Game Version: V1.5")
        print("Use The Google Form Link To Report Bugs Or If You Have Any Suggestions")
        print("https://forms.gle/Z2s5MRe9VnWpf9Gk8")
        print("I Strongly Encourage You To Submit Forms So I Can Improve The Game Quicker")
        print("Press Enter To Continue")
        input("")
        os.system('cls' if os.name == 'nt' else 'clear')
        ## ASCII Art For Hall I Made By Hand :)
        for i in range(4):
            print("                    ")
            print(" __      __         _________          ___         ___")
            time.sleep(.1)
            print("/ ||    |||        / //    \ \         || |        || |")
            time.sleep(.1)
            print("| ||____|||       / //      \ \        || |        || |")
            time.sleep(.1)
            print("| | _____ |      / //________\ \       || |        || |")
            time.sleep(.1)
            print("| ||    |||     / /____________ \      || |        || |")
            time.sleep(.1)
            print("| ||    |||    / //            \ \     || |_____   || |_____")
            time.sleep(.1)
            print("|_||    |||   / //              \ \    ||_______|  ||_______|")
            time.sleep(.1)
        ## Basic Game Info On How To Play
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Basic Tips")
        time.sleep(.5)
        print("Every Meter You Walk You Take 1 Damage")
        time.sleep(.5)
        print("Make Sure You Use Your Potions And Food So You Dont Die")
        time.sleep(.5)
        input("Press Enter To Continue")
        os.system('cls' if os.name == 'nt' else 'clear')
## Starting Choice Fot The HUD
print(" [1] Hud Enabled")
print(" [2] Hud Disabled")
print(" You can always change this in the options menu")
HOOO = input("")
## If An Invalid Input Is Inputed, It Will Default TO HUD On
if HOOO != "1" and HOOO != "2":
    print(" No HUD Selected")
    time.sleep(.5)
    print(" Defaulting To HUD On")
    time.sleep(2)
    HOOO = "1"
## Main While Loop That Runs The Entire Game Mainly By Calling Definitions
while GC == 1:
    ## Level Up System
    if EXP >= EXPR:
        ## Takes Playes Total EXP And Subtracts The EXP Required To Level Up
        EXP = EXP - EXPR
        ## Chooses A Random Number T0 Increase The EXP Required To Level Up By
        EXPRVI = random.randint(50,70)
        ## Applies That Number
        EXPR = EXPR + EXPRVI
        print(" You Leveled Up! ")
        ## VLOC Is Used So That Incase The Player Entered An Invalid Input It Will Not Let Them Miss Out On This Level Up
        VLOC = 1
        CPL = CPL + 1
        print(" All stats increased by 3 Besides Critical Stats")
        # Increases All Player Stats
        PMH = PMH + 3
        PMA = PMA + 3
        PMINA = PMINA + 3
        PMD = PMD + 3
        PMIND = PMIND + 3
        ## This Is Where VLOC Is Used
        while VLOC == 1:
            print("")
            print(" /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ")
            print("  Choose one stat to increase")
            print("  [1] Attack Min +5 ")
            print("  [2] Attack Max +5 ")
            print("  [3] Defense Min +5 ")
            print("  [4] Defence Max +5 ")
            print("  [5] Max Health +5 ")
            print("  [6] Critical Hit Chance +3 ")
            print("  [7] Critical Hit Multiplier +1 ")
            print(" \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
            print("")
            LUC = input("")
            ## Lets Player Choose What To Put Their Level Up Into
            ## Makes Sure That The Player Min Attack Is Not Higher Than THeir Max Attack
            if LUC == "1" and PMINA + 5 <= PMA: 
                PMINA = PMINA + 5
                ## Turns VLOC Off So The Player Can Continue
                VLOC = 0
            ## Lets Player Know That They Cant Have Their Min Attack Higher Than Their Max Attack
            elif LUC == "1" and PMINA > PMA:
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(.5)
                print("")
                print("You can't have your minimum attack above your maximum!")
            elif LUC == "2":
                PMA = PMA + 5
                VLOC = 0
            ## Makes Sure That The Players Minimum Defence Is Not Above Their Maximum
            elif LUC == "3" and PMIND + 5 <= PMD:
                PMIND = PMIND + 5
                VLOC = 0
            elif LUC == "3" and PMIND > PMD:
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(.5)
                print("")
                print("You can't have your minimum defence above your maximum!")
            elif LUC == "4":
                PMD = PMD + 5
                VLOC = 0
            elif LUC == "5":
                PMH = PMH + 5
                VLOC = 0
            elif LUC == "6":
                CRTC = CRTC + 3
                VLOC = 0
            elif LUC == "7":
                CRTM = CRTM + .5
            ## Used To Repeat The Level Up Process In Combination With VLOC
            else:
                print("ERROR")
                input("Press Enter To Continue")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
    ## Calls The HUD Off/On Definitions For The Player Interface
    if HOOO == "1":
        HOOOF = 1
        HUDON()
    elif HOOO == "2":
        HOOOF = 0
        HUDOFF()
    ## PMMC Deals WIth What The Player Chooses To Do
    PMMC = input("")
    ## If They Choose "1" It Will Let Them Move Down The Hallway
    if PMMC == "1":
        ## The Player Has A 1 In 6 Chance Of Encountering Combat
        EC = random.randint(1,6)
        if EC == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("\~~~~~~~~~~~~~~~~~~/")
            time.sleep(1)
            print("!!!")
            time.sleep(1)
            print("You are being attacked!")
            time.sleep(.5)
            print("\~~~~~~~~~~~~~~~~~~/")
            CSCF = 1
            ECA()
            DJT = random.randint(1,3)
            print("You walked a total of " + str(DJT) + "M")
            DM = DM + DJT
            ## Deals With The Damage The Player Will Take When Moving
            PH = PH - DJT/2
            EXP = EXP + DJT
            input("Press Enter To Continue")
        ## Deals With All The Different Rooms The Player Will Encounter
        LC = random.randint(1,10)
        if LC == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("\~~~~~~~~~~~~~~~~/")
            time.sleep(1)
            print("!!!")
            time.sleep(1)
            print("You found a treasure room!")
            ## Generates A Random Amount Of EXP
            EXPG = random.randint(140,200)
            time.sleep(.5)
            print("The room had a strange glowing cube in it. You ignored it and gained " + str(EXPG) + " XP!" )
            DJT = random.randint(3,5)
            GGFC = random.randint(8,12)
            print("You Also Gained " +str(GGFC) + " Sepi's")
            PGT = PGT + GGFC
            time.sleep(.5)
            ## Gives The Player A 33% Chance To Get A Key For A Locked Chest
            LRKC = random.randint(1,3)
            if LRKC == 1:
                KEY = KEY + 1
            print("You also managed to walk " + str(DJT) + "M")
            DM = DM + DJT
            PH = PH - DJT/2
            EXP = EXP + DJT
            EXP = EXP + EXPG
            time.sleep(.5)
            input("Press Enter To Continue")
        ## This Is For The Supply Room, It Just Basically Calls The Supply Room Definition
        WR = random.randint(1,12)
        if WR == 1:
            WRR()
        TRC = random.randint(1,15)
        if TRC == 1:
            TAVERN()
        ## Determines If Nothing Happens When The Player Moves
        if EC != 1 and LC != 1 and WR!= 1 and TRC != 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("\~~~~~~~~~~~~~~~~/")
            time.sleep(.5)
            print("You just kept on walking...")
            time.sleep(.5)
            DJT = random.randint(3,5)
            print("And nothing happened but you walked " + str(DJT) + "M")
            PH = PH - DJT/2
            DM = DM + DJT
            EXP = EXP + DJT
            input("Press Enter To Continue")
    ## Rest Of The Player UI
    elif PMMC == "2":
        ## Calls The Stats Definition
        STATS()
    elif PMMC == "3":
        ## Calls The Inventory Definition
        INVENTORY()
    elif PMMC == "4":
        ## Calls The Options Definition
        OPTIONS()
    elif PMMC == "5":
        QM()
        
## For When The Game Ends, It Will Show This Exit Sequence
if GC == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(4):
        print("                    ")
        print(" __      __         _________          ___         ___")
        time.sleep(.1)
        print("/ ||    |||        / //    \ \         || |        || |")
        time.sleep(.1)
        print("| ||____|||       / //      \ \        || |        || |")
        time.sleep(.1)
        print("| | _____ |      / //________\ \       || |        || |")
        time.sleep(.1)
        print("| ||    |||     / /____________ \      || |        || |")
        time.sleep(.1)
        print("| ||    |||    / //            \ \     || |_____   || |_____")
        time.sleep(.1)
        print("|_||    |||   / //              \ \    ||_______|  ||_______|")
        time.sleep(.1)














    ##
    ## Example Save Code
    ## PMA200PMINA10PMD2000PMIND10PMH500PH198.55CRTC5CRTM2PGT5DM0CPL10PQIBP0PQIWK0WBPBCB0TOTTCQ0BOC0EXP50EXPR300SMLLP5MEDP2LARGEP1EMINA10EMA10EMH100FOOD5KEY2CCQ0
    ##
    ## End Of Code
    ##
    ##