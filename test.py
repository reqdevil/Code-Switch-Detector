import os

punctuations = '''!():[]{};’'"…“””,<>./?@#$%^&*_~'''
specialCharacters = '''çğöüişı'''
PATH = "files/speechFiles/"


def learnEnglishWords():
    englishWordArray = []
    with open("files/languageFiles/english_word_list.txt", "r", encoding="utf8") as englishFile:
        lines = englishFile.readlines()

        for word in lines:
            for char in word:
                if char == "\n":
                    word = word.replace(char, "")

            englishWordArray.append(word.lower())

    englishFile.close()

    return englishWordArray


def lineSeparation(line):
    newLine = []

    for li in line:
        if li == f"{name1Identifier}:" or li == f"{name2Identifier}:" or li == f"{name3Identifier}:" or li == f"{name4Identifier}:" or li == f"{name5Identifier}:":
            continue

        if li == "(gülme)" or li == "(köpeğe)":
            continue

        for char in li:
            if char in punctuations:
                li = li.replace(char, "")
            elif char == "\n":
                li = li.replace(char, "")
            elif char == "-":
                li = li.split("-")[0]
            elif char == " ":
                li = li.replace(char, "")

        newLine.append(li.lower())

    for li in newLine:
        if not li:
            newLine.remove(li)

    return newLine


def wordSeparation(fileName):
    with open(f"{fileName}", "r", encoding="utf8") as speechFile:
        lines = speechFile.readlines()

        for line in lines:
            line = line.split(" ")

            if f"{name1Identifier}:" in line:
                for li in lineSeparation(line):
                    person1Temp.append(li)
            elif f"{name2Identifier}:" in line:
                for li in lineSeparation(line):
                    person2Temp.append(li)
            elif f"{name3Identifier}:" in line:
                for li in lineSeparation(line):
                    person3Temp.append(li)
            elif f"{name4Identifier}:" in line:
                for li in lineSeparation(line):
                    person4Temp.append(li)
            elif f"{name5Identifier}:" in line:
                for li in lineSeparation(line):
                    person5Temp.append(li)

    speechFile.close()


def wordDetection(words, wordCounter=0):
    personSwitch = []

    for word in words:
        if word in englishWords:
            # print(word)
            switchedWords.append(word)
            personSwitch.append(word)
            wordCounter += 1
        else:
            originalWords.append(word)

        # found = False
        #
        # if word in englishWords:
        #     switchedWords.append(word)
        #     wordCounter += 1
        # elif word in turkishWords:
        #     originalWords.append(word)
        # else:
        #     for line in tfl:
        #         if word == line.replace("\n", ""):
        #             found = True
        #
        #     if not found:
        #         found = False
        #         for char in word:
        #             if char in specialCharacters:
        #                 found = True
        #
        #         if found:
        #             tf.write(f"{word}\n")
        #         else:
        #             add = input(f"{word} is a new type of word. Is it English(E/e) or Turkish(T/t): ")
        #
        #             if add == "T" or add == "t":
        #                 tf.write(f"{word}\n")
        #                 originalWords.append(word)
        #             elif add == "E" or add == "e":
        #                 ef.write(f"{word}\n")
        #                 switchedWords.append(word)
        #             else:
        #                 print("Wrong input entered. Word will not be entered to a list.")

    return wordCounter, personSwitch


def calculateFrequency():

    with open("files/excelFiles/switchedWords.csv", "r+", encoding="utf8") as swf:
        swf.write("Word,Frequency")

        switchedWords.sort()

        temp = ""
        for switchedWord in switchedWords:
            wordCounter = 0

            if temp != switchedWord:
                temp = switchedWord
            else:
                continue

            for swd in switchedWords:
                if swd == temp:
                    wordCounter += 1

            swf.write(f"\n{temp},{wordCounter}")
    swf.close()

    with open("files/excelFiles/turkishWords.csv", "r+", encoding="utf8") as twf:
        twf.write("Word,Frequency")

        originalWords.sort()

        temp = ""
        for originalWord in originalWords:
            wordCounter = 0

            if temp != originalWord:
                temp = originalWord
            else:
                continue

            for tw in originalWords:
                if tw == temp:
                    wordCounter += 1

            twf.write(f"\n{temp},{wordCounter}")
    twf.close()


def calculateSwitchFrequency(name, switchArray):
    with open(f"files/personFiles/{name}.csv", "w+", encoding="utf8") as f:
        f.write("Word,Frequency\n")

        switchArray.sort()

        temp = ""
        for swa in switchArray:
            wordCounter = 0

            if temp != swa:
                temp = swa
            else:
                continue

            for s in switchArray:
                if s == temp:
                    wordCounter += 1

            f.write(f"{temp},{wordCounter}\n")
    f.close()


def outputWrite(name, totalWord, counter, wordPercentage, totalPercentage):
    print(f"{name} {totalWord} kelimede, farklı dilde {counter} tane  kelime kullandı. (%{wordPercentage})")
    print(f"{name} katılımcısının konuşmadaki katkısı %{totalPercentage}\n")

    with open(f"files/outputFiles/{file}.txt", "a+", encoding="utf8") as outputFiles:
        outputFiles.write(f"{name} {totalWord} kelimede, farklı dilde {counter} tane  kelime kullandı. (%{wordPercentage})\n")
        outputFiles.write(f"{name} katılımcısının konuşmadaki katkısı %{totalPercentage}\n\n")


if __name__ == '__main__':
    number = int(input("Kişi sayısını giriniz: "))

    name3Identifier = ""
    name4Identifier = ""
    name5Identifier = ""
    name3 = ""
    name4 = ""
    name5 = ""

    name1 = input("Birinci kişinin adını giriniz: ")
    name1Identifier = input("Birinci kişinin tanımını giriniz: ")
    name2 = input("İkinci kişinin adını giriniz: ")
    name2Identifier = input("İkinci kişinin tanımını giriniz: ")
    if number >= 3:
        name3 = input("Üçüncü kişinin adını giriniz: ")
        name3Identifier = input("Üçüncü kişinin tanımını giriniz: ")
    if number >= 4:
        name4 = input("Dördüncü kişinin adını giriniz: ")
        name4Identifier = input("Dördüncü kişinin tanımını giriniz: ")
    if number >= 5:
        name5 = input("Beşinci kişinin adını giriniz: ")
        name5Identifier = input("Beşinci kişinin tanımını giriniz: ")

    file = input("Dosya klasörünün adını giriniz: ")
    PATH += f"{file}"

    person1 = []
    person2 = []
    person3 = []
    person4 = []
    person5 = []

    person1Counter = 0
    person2Counter = 0
    person3Counter = 0
    person4Counter = 0
    person5Counter = 0

    switch1 = []
    switch2 = []
    switch3 = []
    switch4 = []
    switch5 = []

    switchedWords = []
    originalWords = []

    fileList = os.listdir(PATH)
    # print(fileList)

    for index in range(0, len(fileList)):
        person1Temp = []
        person2Temp = []
        person3Temp = []
        person4Temp = []
        person5Temp = []

        englishWords = learnEnglishWords()
        wordSeparation(PATH+f"/{fileList[index]}")

        count, switch = wordDetection(person1Temp)
        person1Counter += count
        for pt in person1Temp:
            person1.append(pt)
        for sw in switch:
            switch1.append(sw)

        count, switch = wordDetection(person2Temp)
        person2Counter += count
        for pt in person2Temp:
            person2.append(pt)
        for sw in switch:
            switch2.append(sw)

        if number >= 3:
            count, switch = wordDetection(person3Temp)
            person3Counter += count
            for pt in person3Temp:
                person3.append(pt)
            for sw in switch:
                switch3.append(sw)

        if number >= 4:
            count, switch = wordDetection(person4Temp)
            person4Counter += count
            for pt in person4Temp:
                person4.append(pt)
            for sw in switch:
                switch4.append(sw)

        if number >= 5:
            count, switch = wordDetection(person5Temp)
            person5Counter += count
            for pt in person5Temp:
                person5.append(pt)
            for sw in switch:
                switch5.append(sw)

    outputWrite(name1, len(person1), person1Counter, round(person1Counter * 100 / len(person1), 2),
                round(len(person1) * 100 / (len(person1) + len(person2) + len(person3) + len(person4) + len(person5)),
                      2))
    calculateSwitchFrequency(name1, switch1)

    outputWrite(name2, len(person2), person2Counter, round(person2Counter * 100 / len(person2), 2),
                round(len(person2) * 100 / (len(person1) + len(person2) + len(person3) + len(person4) + len(person5)),
                      2))
    calculateSwitchFrequency(name2, switch2)

    if number >= 3:
        outputWrite(name3, len(person3), person3Counter, round(person3Counter * 100 / len(person3), 2), round(
            len(person3) * 100 / (len(person1) + len(person2) + len(person3) + len(person4) + len(person5)), 2))
        calculateSwitchFrequency(name3, switch3)
    if number >= 4:
        outputWrite(name4, len(person4), person4Counter, round(person4Counter * 100 / len(person4), 2), round(
            len(person4) * 100 / (len(person1) + len(person2) + len(person3) + len(person4) + len(person5)), 2))
        calculateSwitchFrequency(name4, switch4)
    if number >= 5:
        outputWrite(name5, len(person5), person5Counter, round(person5Counter * 100 / len(person5), 2), round(
            len(person5) * 100 / (len(person1) + len(person2) + len(person3) + len(person4) + len(person5)), 2))
        calculateSwitchFrequency(name5, switch5)

    calculateFrequency()
