def main():
    logicalMessage = "The axiom of transitivity holds. Congrats! You acted rationally in this instance!"
    illogicalMessage = "You have violated the axiom of transitivity and have not acted rationally."
    answerList = ["coffee", "tea"]
    # first ask
    answer = input("Do you prefer coffee or tea? \n")
    while answer.lower() not in answerList:
        print("Invalid input. Try again.")
        answer = input("Do you prefer coffee or tea? \n")

    # second ask
    answerListCopy = answerList.copy()
    answerListCopy.remove(answer.lower())
    answerListCopy.append("hot chocolate")
    answer2 = input("Do you prefer " + answerListCopy[0] + " or hot chocolate? \n")
    while answer2.lower() not in answerListCopy:
        print("Invalid input. Try again.")
        answer2 = input("Do you prefer " + answerListCopy[0] + " or hot chocolate? \n")

    # final ask
    if answer2.lower() == "hot chocolate":    # user indicates possible indifference
        answerList3 = ["hot chocolate", "indifferent", answer.lower()]
        print("Do you prefer hot chocolate or " + answer.lower() + "?")
        answer3 = input("Or are you indifferent? \n")
        while answer3.lower() not in answerList3:
            print("Invalid input. Try again.")
            print("Do you prefer hot chocolate or " + answer.lower() + "?")
            answer3 = input("Or are you indifferent? \n")
        if answer3.lower() == "indifferent":
            logicCheck = True
            indifference = True
        else:
            logicCheck = True
            indifference = False

    else:    # no indifference, possible violation
        answerList3 = ["hot chocolate", answer.lower()]
        answer3 = input("Do you prefer hot chocolate or " + answer.lower() + "? \n")
        while answer3.lower() not in answerList3:
            print("Invalid input. Try again.")
            answer3 = input("Do you prefer hot chocolate or " + answer.lower() + "? \n")
        if answer3 == "hot chocolate":    # illogical choice violates transitivity
            logicCheck = False
            indifference = False
        else:
            logicCheck = True
            indifference = False

    # output
    if logicCheck and indifference:
        print(logicalMessage)
        print("You're indifferent between hot chocolate and", answer + ".")

    elif logicCheck and not indifference:
        print(logicalMessage)
        if answer2.lower() == "hot chocolate":    # user doesn't like coffee/tea
            if answer3.lower() == "hot chocolate":
                print("You prefer hot chocolate over", answer.lower())
            else:
                print("You prefer", answer3.lower(), "over hot chocolate.")
            if answer.lower() == "coffee":
                print("You aren't a big fan of tea.")
            elif answer.lower() == "tea":
                print("You aren't a big fan of coffee.")
        else:                                    # clear user preference
            print("You prefer", answer.lower(), "to", answer2.lower() + ",", answer2.lower(),
                  "to hot chocolate, and", answer.lower(), "to hot chocolate.")
    elif not logicCheck:
        print(illogicalMessage)
        print("You prefer", answer.lower(), "over", answer2.lower(), "and", answer2.lower(),
              "over", answer3.lower() + ". If behaving rationally, you would prefer",
              answer.lower(), "over hot chocolate.")


if __name__ == "__main__":
    main()
