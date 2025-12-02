# Unit converter KG to Lbs

while True:
    print("Enter your Choice to convert: ⚖️")
    print("")
    print("1️⃣  KG to Lbs ")
    print("2️⃣  Lbs to KG ")
    print("3️⃣  Km to Miles")
    print("4️⃣  Miles to Km ")
    print("5️⃣  Exit")
    print("")
    Choice = int(input("Enter Your Choice 📝 :-  "))
    print("--------------------------------")

    match Choice:
        case 1:
            Kg = float(input("Enter weight in KG: "))
            Lbs = Kg * 2.20462
            print("=========================||")
            print("👉 ",Kg, "KG 🟰 ", format(Lbs, ".2f"), "Lbs")
            print("=========================||")
        case 5:
            print("Sitaram 👋")
            break