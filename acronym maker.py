while True:
    acro = input("Enter a something you want to turn into a acronym. ")
    acro_fixed = acro.split()
    acro_new = ""
    reg_words = ["and", "or", "of", "&"]
    print("Your acronym is")
    for i in acro_fixed:
        if i in reg_words:
            acro_new += i.lower()[0]
        else:
            acro_new += i.upper()[0]
    print(acro_new)
