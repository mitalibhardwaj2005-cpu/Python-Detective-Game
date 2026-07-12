print("================================")
print("   DETECTIVEX INVESTIGATION")
print("================================")

detective_name = input("Enter your detective name: ")

evidence = []

suspects = {
    "Rahul": "I was sleeping at home.",
    "Ankit": "I was watching TV.",
    "Riya": "I was cooking in the kitchen."
}

criminal = "Rahul"   # hidden answer

while True:

    print("\n===== MAIN MENU =====")
    print("1. Examine Crime Scene")
    print("2. View Suspects")
    print("3. View Collected Evidence")
    print("4. Analyze Evidence")
    print("5. Solve Case")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Crime Scene
    if choice == "1":

        print("\nCrime Scene Evidence:")
        print("1. Bloody Knife")
        print("2. Footprints")
        print("3. Broken Phone")

        clue = input("Which evidence do you want to collect (1/2/3)? ")

        if clue == "1":
            if "Bloody Knife" not in evidence:
                evidence.append("Bloody Knife")
                print("✔ Bloody Knife collected!")
            else:
                print("Already collected!")

        elif clue == "2":
            if "Footprints" not in evidence:
                evidence.append("Footprints")
                print("✔ Footprints collected!")
            else:
                print("Already collected!")

        elif clue == "3":
            if "Broken Phone" not in evidence:
                evidence.append("Broken Phone")
                print("✔ Broken Phone collected!")
            else:
                print("Already collected!")

        else:
            print("Invalid choice!")

    # Suspects
    elif choice == "2":

        print("\nSuspects:")
        for name in suspects:
            print("-", name)

        suspect_name = input("\nEnter suspect name: ")

        if suspect_name in suspects:
            print("\nStatement:")
            print(suspects[suspect_name])
        else:
            print("Suspect not found.")

    # Evidence List
    elif choice == "3":

        print("\nCollected Evidence:")

        if len(evidence) == 0:
            print("No evidence collected yet.")
        else:
            for item in evidence:
                print("-", item)

    # Analysis
    elif choice == "4":

        print("\n===== LAB ANALYSIS =====")

        if len(evidence) == 0:
            print("No evidence available for analysis.")

        if "Bloody Knife" in evidence:
            print("• Fingerprints on the knife belong to Rahul.")

        if "Footprints" in evidence:
            print("• Footprints match Rahul's shoes.")

        if "Broken Phone" in evidence:
            print("• Threat messages from Rahul found on victim's phone.")

    # Solve Case
    elif choice == "5":

        print("\n===== FINAL VERDICT =====")
        print("Who is the criminal?")
        print("1. Rahul")
        print("2. Ankit")
        print("3. Riya")

        answer = input("Enter your choice: ")

        selected = ""
        if answer == "1":
            selected = "Rahul"
        elif answer == "2":
            selected = "Ankit"
        elif answer == "3":
            selected = "Riya"

        # LOGIC CHECK
        if selected == criminal:

            print("\n🎉 CASE SOLVED SUCCESSFULLY!")
            print("You proved that", criminal, "is the criminal.")

            print("\nEvidence Used:")
            for item in evidence:
                print("-", item)

            print("\n🏆 Detective Rating: EXCELLENT WORK!")
            break   # game ends here

        else:

            print("\n❌ WRONG ACCUSATION!")
            print("The real criminal escaped...")

            print("\n💀 GAME OVER")
            break   # game ends

    # Exit
    elif choice == "6":
        print("\nThank you for playing DetectiveX!")
        break

    else:
        print("Invalid choice. Please try again.")