def haupt_menu():
    while True:
        print("\nHAUPTMENÜ")
        print("1 = Training eintragen")
        print("2 = Trainingsdaten mutieren")
        print("3 = Trainingsdaten löschen")
        print("4 = Historie einsehen")
        print("0 = Beenden")
        choice = input("Wähle eine Option: ").strip()

        if choice == "1":
            add_training(data)
        elif choice == "2":
            menu_mutieren()
        elif choice == "3":
            menu_löschen()
        elif choice == "4":
            show_history(data)
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option! Bitte erneut eingeben.")

if __name__=="__main__":
    haupt_menu()