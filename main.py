# from turkishnlp import detector
import enchant

# obj = detector.TurkishNLP()
dictionary = enchant.Dict("en_US")

punctuations = '''!()-[]{};'"…“””,<>./?@#$%^&*_~'''
firstPersonName = ""
secondPersonName = ""


def getText():
    firstPerson = []
    secondPerson = []

    firstPersonCounter = 0
    secondPersonCounter = 0

    with open("files/speechFiles/kudret.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            line = line.split(" ")

            if "K1:" in line:
                for l in line:
                    if l == "K1:":
                        continue

                    for char in l:
                        if char in punctuations:
                            l = l.replace(char, "")
                        elif char == "\n":
                            l = l.replace(char, "")

                    firstPerson.append(l)

            else:
                for l in line:
                    if l == "K2:":
                        continue

                    for char in l:
                        if char in punctuations:
                            l = l.replace(char, "")
                        elif char == "\n":
                            l = l.replace(char, "")

                    secondPerson.append(l)

    # print(firstPerson)
    # print(secondPerson)

    for _ in firstPerson:
        for f in firstPerson:
            if not f:
                firstPerson.remove(f)

    # print(firstPerson)

    for f in firstPerson:
        if dictionary.check(f):
            print(f)

    print(f"{firstPersonName} used {firstPersonCounter} english word in {len(firstPerson)}\n")

    # for s in secondPerson:
    #     if not obj.is_turkish(s):
    #         secondPersonCounter += 1
    #
    # print(f"{secondPersonName} used {secondPersonCounter} english word in {len(secondPerson)}")


if __name__ == "__main__":
    firstPersonName = input("Enter first person name: ")
    secondPersonName = input("Enter second person name: ")

    print(f"\nDownloading Word Set")
    # obj.download()
    # obj.create_word_set()

    getText()
