print("-*-*-*- Welcome to my Bank. -*-*-*-")
print("-*-*-*- How may I help you? -*-*-*-")
choice = input("Here is my menu:"
               "\n"
               "\nA. Send Money"
               "\nB. Buy Airtime"
               "\nC. Check Balance"
               "\nD. Bill Payment"
               "\nE. Change Pin"
               "\nYour response: ").title()
if choice == "A":
    def bank_type():
        bank = (input("\nWhat bank do you want to send money to?"
                      "\nA. UBA"
                      "\nB. Access Bank"
                      "\nC. First Bank"
                      "\nD. GTBank"
                      "\nE. Polaris Bank"
                      "\nF. Union Bank"
                      "\nG. Zenith Bank"
                      "\nYour response: ")).title()

        if bank == "A":
            int(input("Enter the UBA account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "B":
            int(input("Enter the Access Bank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "C":
            int(input("Enter the First Bank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "D":
            int(input("Enter the GTBank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "E":
            int(input("Enter the Polaris Bank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "F":
            int(input("Enter the Union Bank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        elif bank == "G":
            int(input("Enter the Zenith Bank account number: "))
            amount = int(input("How much do you want to send? "))
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").title()
            if destination == "Yes":
                def pin_code():
                    pin = int(input("Please enter your PIN: "))
                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").title()
                        if sent == "Yes":
                            bank_type()
                        elif sent == "No":
                            print("Thank you for banking with us")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "No":
                print("Transaction cancelled")
        else:
            print("There is no option " + bank + ", please select another option")


    bank_type()

elif choice == "B":
    def airtime():
        int(input("\nEnter the number you want to recharge: "))
        amount = int(input("Enter the amount of airtime you want to buy: "))

        def pin_airtime():
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                print("your recharge of ₦" + str(amount) + " is successful, do you want to buy more airtime?")
            elif pin != 1234:
                print("Incorrect PIN, please try again")
                pin_airtime()

        pin_airtime()
        rebuy = input("(yes/no): ").title()
        if rebuy == "Yes":
            airtime()
        elif rebuy == "No":
            print("Thank you for banking with us")


    airtime()

elif choice == "C":
    int(input("\nEnter your account number to check your balance: "))


    def pin_no():
        pin = int(input("Enter your PIN: "))
        if pin == 1234:
            print("Hello, XXXXXX, your available balance is ₦XXXXXX."
                  "\nThank you for banking with us")
        else:
            print("Incorrect PIN, Please try again")
            pin_no()


    pin_no()

elif choice == "D":
    bills = input("\nThese are the bills I can help you pay;"
                  "\nplease make a selection"
                  "\n"
                  "\nA. Cable TV"
                  "\nB. Electricity"
                  "\nYour response: ").title()
    if bills == "A":
        biller = input("\nPlease select your biller"
                       "\n"
                       "\nA. GOTV"
                       "\nB. DSTV"
                       "\nYour response: ").title()
        if biller == "A":
            option = input("Please select an option"
                           "\n"
                           "\nA. GOTV(JOLLI, Price: ₦2,460)"
                           "\nB. GOTV(JINJA, Price: ₦1,640)"
                           "\nC. GOTV(MAX, Price: ₦3,600)"
                           "\nYour response: ").title()
            if option == "A":
                int(input("Please give me your GOTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the GOtv Jolli package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your GOtv, the sum of ₦2,460 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "B":
                int(input("Please give me your GOTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the GOtv JINJA package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print(
                                "You have successfully credited your GOtv, the sum of ₦1,460 has been deducted from "
                                "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "C":
                int(input("Please give me your GOTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the GOtv MAX package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your GOtv, the sum of ₦3,600 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            else:
                print("Sorry, there is no option " + option)

        elif biller == "B":
            option = input("\nPlease select an option"
                           "\n"
                           "\nA. DSTV(PREMIUM, Price: ₦18,400)"
                           "\nB. DSTV(COMPACT PLUS, Price: ₦12,400)"
                           "\nC. DSTV(COMPACT, Price: ₦7,900)"
                           "\nD. DSTV(CONFAM, Price: ₦4,615)"
                           "\nE. DSTV(YANGA, Price: ₦2,565)"
                           "\nF. DSTV(PADI, Price: ₦1,850)"
                           "\nYour response: ").title()
            if option == "A":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV PREMIUM package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦18,400 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "B":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV COMPACT PLUS package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦12,400 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "C":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV COMPACT package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦7,900 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "D":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV CONFAM package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦4,615 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "E":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV YANGA package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦2,565 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "F":
                int(input("Please give me your DSTV SmartCard Number: "))
                sure_payment = input("Are you sure you want to pay for the DSTV PADI package? (yes/no)"
                                     "\nYour response: ").title()
                if sure_payment == "Yes":
                    def payment_pin():
                        pin = int(input("Enter your PIN: "))
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦1,850 has been deducted from "
                                  "your account.")
                        elif pin != 1234:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
        else:
            print("Sorry, there is no option " + biller)
    elif bills == "B":
        elect_biller = input("Please select your biller: "
                             "\n"
                             "\nA. Ikeja EDC"
                             "\nB. PHCN Eko"
                             "\nYour response: ").title()
        if elect_biller == "A":
            int(input("Please give me your Ikeja EDC Meter number: "))
            elect_amount = int(input("How much do you want to pay? "))
            elect_payment = input("Are you sure you want to pay the sum of ₦" + str(elect_amount) +
                                  " into your Meter? (yes/no): ").title()
            if elect_payment == "Yes":
                def elect_pin():
                    pin = int(input("Enter your PIN: "))
                    if pin == 1234:
                        print("You have successfully recharged your Meter, the sum of ₦" + str(elect_amount) +
                              " has been deducted from your account.")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        elect_pin()


                elect_pin()
            else:
                print("Sorry, the transaction was not successful")
        elif elect_biller == "B":
            int(input("Please give me your PHCN Eko Meter number: "))
            elect_amount = int(input("How much do you want to pay? "))
            elect_payment = input("Are you sure you want to pay the sum of ₦" + str(elect_amount) +
                                  " into your Meter? (yes/no): ").title()
            if elect_payment == "Yes":
                def elect_pin():
                    pin = int(input("Enter your PIN: "))
                    if pin == 1234:
                        print("You have successfully recharged your Meter, the sum of ₦" + str(elect_amount) +
                              " has been deducted from your account.")
                    elif pin != 1234:
                        print("Incorrect PIN, please try again")
                        elect_pin()


                elect_pin()
            else:
                print("Sorry, the transaction was not successful")
        else:
            print("Sorry, there is no option " + elect_biller)
    else:
        print("Sorry, there is no option " + bills)
elif choice == "E":
    def real_pin():
        current_pin = int(input("Please enter your current PIN: "))
        if current_pin == 1234:
            new_pin = int(input("Please enter your new PIN: "))
            confirm_pin = int(input("Please confirm your PIN: "))
            if new_pin == confirm_pin:
                print("You have successfully changed your PIN, your new PIN is " + str(new_pin))
            else:
                print("Sorry the PIN did not match, please try again")
        elif current_pin != 1234:
            print("Incorrect PIN, please try again")
            real_pin()


    real_pin()
else:
    print("Sorry, there is no option " + choice)
