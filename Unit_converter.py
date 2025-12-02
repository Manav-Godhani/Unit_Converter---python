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
            print("=========================|")
            print("👉 ",Kg, "KG 🟰 ", format(Lbs, ".2f"), "Lbs")
            print("=========================|")
        case 2:
            Lbs = float(input("Enter Weight in Lbs :"))
            Kg = Lbs / 2.20462
            print("=========================|")
            print("👉 ",Lbs, "Lbs 🟰 ", format(Kg, ".2f"), "Kg")
            print("=========================|")
        case 3:
            Km = float(input("Enter distance in Km: "))
            Miles = Km * 0.621371
            print("=========================|")
            print("👉 ",Km, "Km 🟰 ", format(Miles, ".2f"), "Miles")
            print("=========================|")
        case 4:
            Miles = float(input("Enter distance in Miles: "))
            Km = Miles / 0.621371
            print("=========================|")
            print("👉 ",Miles, "Miles 🟰 ", format(Km, ".2f"), "Km")
            print("=========================|")
        case 5:
            print("          Sitaram 👋")
            print("--------------------------------")
            break