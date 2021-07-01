from mtgsdk import Card
import os

with open("SetCodes.txt", 'r') as setCodesFile:
    for setCode in setCodesFile:
        if setCode.isspace():
            continue
         
        setCode = setCode.strip('\n')
        setCards = Card.where(set=setCode).all()

        if len(setCards) == 0:
            continue

        setFilename = f"{setCode}.txt"
        with open(setFilename, 'w') as setFile:
            setCodeHaveFilename = f"{setCode}have.txt"
            haveNames = []

            if os.path.exists(os.path.join(os.getcwd(),setCodeHaveFilename)):
                with open(setCodeHaveFilename, 'r') as haveFile:
                    for line in haveFile:
                        haveNames.append(line)

            for card in setCards:
                if card.name.upper() in haveNames:
                    continue

                massEntryCode = f"1 {card.name} [{setCode}]"

                setFile.write(massEntryCode + '\n')