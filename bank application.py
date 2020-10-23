#!/usr/bin/python3

print("-*-*-*- Welcome to my Bank. -*-*-*-")
print("-*-*-*- How may I help you? -*-*-*-")
choice = input("Here is my menu:"
               "\n"
               "\nA. Send Money"
               "\nB. Buy Airtime"
               "\nC. Check Balance"
               "\nD. Bill Payment"
               "\nE. Change Pin"
               "\nYour response: ").lower()
if choice == "a":
    def bank_type():
        bank = (input("\nWhat bank do you want to send money to?"
                      "\nA. UBA"
                      "\nB. Access Bank"
                      "\nC. First Bank"
                      "\nD. GTBank"
                      "\nE. Polaris Bank"
                      "\nF. Union Bank"
                      "\nG. Zenith Bank"
                      "\nYour response: ")).lower()

        if bank == "a":
            validity = False

            while validity == False:
                acct_no = input("Enter the UBA account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "b":
            validity = False

            while validity == False:
                acct_no = input("Enter the Access Bank account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "c":
            validity = False

            while validity == False:
                acct_no = input("Enter the First Bank account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "d":
            validity = False

            while validity == False:
                acct_no = input("Enter the GTBank account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "e":
            validity = False

            while validity == False:
                acct_no = input("Enter the Polaris Bank account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "f":
            validity = False

            while validity == False:
                acct_no = input("Enter the Union Bank account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        elif bank == "g":
            validity = False

            while validity == False:
                acct_no = input("Enter the Zenith account number: ")
                try:
                    acct_no = int(acct_no)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                else:
                    validity = True

            validity = False

            while validity == False:
                amount = input("How much do you want to send? ")
                try:
                    amount = int(amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if amount < 100:
                    print("Sorry you can not transfer any amount below ₦100")
                    continue
                elif amount > 1000000:
                    print("Sorry you can not transfer any amount above ₦1000000")
                    continue
                else:
                    validity = True
            destination = input("Are you sure you want to send ₦" + str(amount) + " to XXXXXX? (yes/no): ").lower()
            if destination == "yes":
                def pin_code():
                    pin = input("Please enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers are accepted")

                    if pin == 1234:
                        sent = input("You have successfully sent ₦" + str(amount) +
                                     " to XXXXXX\nDo you want to send more money? (yes/no): ").lower()
                        if sent == "yes":
                            bank_type()
                        else:
                            print("Thank you for banking with us")
                    else:
                        print("Incorrect PIN, please try again")
                        pin_code()

                pin_code()
            elif destination == "no":
                print("Transaction cancelled")
            else:
                print("I don't understand your request, please start all over")
        else:
            print("There is no option " + bank + ", please select another option")


    bank_type()

elif choice == "b":
    def airtime():
        valid = False

        while valid == False:
            number = input("\nEnter the number you want to recharge: ")
            try:
                number = int(number)
            except:
                print("Invalid input, only numbers accepted")
                continue
            else:
                valid = True

        valid = False

        while valid == False:
            amount = input("Enter the amount of airtime you want to buy: ")
            try:
                amount = int(amount)
            except:
                print("Invalid input, only numbers are accepted")
                continue
            if amount < 100:
                print("Please enter an amount greater than ₦100")
            elif amount > 10000:
                print("Exceeds limit of ₦10000. Try lower amount")
            else:
                valid = True

        def pin_airtime():
            pin = input("Enter your PIN: ")
            try:
                pin = int(pin)
            except:
                print("Invalid input, only numbers are accepted")
            if pin == 1234:
                print("your recharge of ₦" + str(amount) + " is successful, do you want to buy more airtime?")
            else:
                print("Incorrect PIN, please try again")
                pin_airtime()

        pin_airtime()
        rebuy = input("(yes/no): ").lower()
        if rebuy == "yes":
            airtime()
        elif rebuy == "no":
            print("Thank you for banking with us")
        else:
            print("Sorry I don't understand your request")


    airtime()

elif choice == "c":
    valid = False

    while valid == False:
        balance = input("\nEnter your account number to check your balance: ")
        try:
            balance = int(balance)
        except:
            print("Invalid input, only numbers are accepted")
            continue
        else:
            valid = True


    def pin_no():
        pin = input("Enter your PIN: ")
        try:
            pin = int(pin)
        except:
            print("Invalid input, only numbers are accepted")
        if pin == 1234:
            print("Hello, XXXXXX, your available balance is ₦XXXXXX."
                  "\nThank you for banking with us")
        else:
            print("Incorrect PIN, Please try again")
            pin_no()


    pin_no()

elif choice == "d":
    bills = input("\nThese are the bills I can help you pay;"
                  "\nplease make a selection"
                  "\n"
                  "\nA. Cable TV"
                  "\nB. Electricity"
                  "\nYour response: ").lower()
    if bills == "a":
        biller = input("\nPlease select your biller"
                       "\n"
                       "\nA. GOTV"
                       "\nB. DSTV"
                       "\nYour response: ").lower()
        if biller == "a":
            option = input("Please select an option"
                           "\n"
                           "\nA. GOTV(JOLLI, Price: ₦2,460)"
                           "\nB. GOTV(JINJA, Price: ₦1,640)"
                           "\nC. GOTV(MAX, Price: ₦3,600)"
                           "\nYour response: ").lower()
            if option == "a":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your GOTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the GOtv Jolli package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your GOtv, the sum of ₦2,460 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "b":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your GOTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the GOtv JINJA package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print(
                                "You have successfully credited your GOtv, the sum of ₦1,460 has been deducted from "
                                "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "c":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your GOTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the GOtv MAX package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your GOtv, the sum of ₦3,600 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            else:
                print("Sorry, there is no option " + option)

        elif biller == "b":
            option = input("\nPlease select an option"
                           "\n"
                           "\nA. DSTV(PREMIUM, Price: ₦18,400)"
                           "\nB. DSTV(COMPACT PLUS, Price: ₦12,400)"
                           "\nC. DSTV(COMPACT, Price: ₦7,900)"
                           "\nD. DSTV(CONFAM, Price: ₦4,615)"
                           "\nE. DSTV(YANGA, Price: ₦2,565)"
                           "\nF. DSTV(PADI, Price: ₦1,850)"
                           "\nYour response: ").lower()
            if option == "a":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV PREMIUM package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦18,400 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "b":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV COMPACT PLUS package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦12,400 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "c":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV COMPACT package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦7,900 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "d":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV CONFAM package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦4,615 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "e":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV YANGA package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦2,565 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
            elif option == "f":
                valid = False

                while valid == False:
                    smartcard = input("Please give me your DSTV SmartCard Number: ")
                    try:
                        smartcard = int(smartcard)
                    except:
                        print("Invalid input, only numbers accepted")
                        continue
                    else:
                        valid = True
                sure_payment = input("Are you sure you want to pay for the DSTV PADI package? (yes/no)"
                                     "\nYour response: ").lower()
                if sure_payment == "yes":
                    def payment_pin():
                        pin = input("Enter your PIN: ")
                        try:
                            pin = int(pin)
                        except:
                            print("Invalid input, only numbers accepted")
                        if pin == 1234:
                            print("You have successfully credited your DSTV, the sum of ₦1,850 has been deducted from "
                                  "your account.")
                        else:
                            print("Incorrect PIN, please try again")
                            payment_pin()


                    payment_pin()
                else:
                    print("Sorry, the transaction was not successful")
        else:
            print("Sorry, there is no option " + biller)
    elif bills == "b":
        elect_biller = input("Please select your biller: "
                             "\n"
                             "\nA. Ikeja EDC"
                             "\nB. PHCN Eko"
                             "\nYour response: ").lower()
        if elect_biller == "a":
            valid = False
            while valid == False:
                meter_no = input("Please give me your Ikeja EDC Meter number: ")
                try:
                    meter_no = int(meter_no)
                except:
                    print("Invalid input, only numbers accepted")
                    continue
                else:
                    valid = True

            validity = False

            while validity == False:
                elect_amount = input("How much do you want to pay? ")
                try:
                    elect_amount = int(elect_amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if elect_amount < 1000:
                    print("Please enter an amount greater than ₦1000")
                    continue
                elif elect_amount > 20000:
                    print("Exceeds limit of ₦20000. Try lower amount")
                    continue
                else:
                    validity = True

            elect_payment = input("Are you sure you want to pay the sum of ₦" + str(elect_amount) +
                                  " into your Meter? (yes/no): ").lower()
            if elect_payment == "yes":
                def elect_pin():
                    pin = input("Enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers accepted")
                    if pin == 1234:
                        print("You have successfully recharged your Meter, the sum of ₦" + str(elect_amount) +
                              " has been deducted from your account.")
                    else:
                        print("Incorrect PIN, please try again")
                        elect_pin()


                elect_pin()
            else:
                print("Sorry, the transaction was not successful")
        elif elect_biller == "b":
            valid = False
            while valid == False:
                meter_no = input("Please give me your PHCN EKO Meter number: ")
                try:
                    meter_no = int(meter_no)
                except:
                    print("Invalid input, only numbers accepted")
                    continue
                else:
                    valid = True

            validity = False

            while validity == False:
                elect_amount = input("How much do you want to pay? ")
                try:
                    elect_amount = int(elect_amount)
                except:
                    print("Invalid input, only numbers are accepted")
                    continue
                if elect_amount < 1000:
                    print("Please enter an amount greater than ₦1000")
                    continue
                elif elect_amount > 20000:
                    print("Exceeds limit of ₦20000. Try lower amount")
                    continue
                else:
                    validity = True
            elect_payment = input("Are you sure you want to pay the sum of ₦" + str(elect_amount) +
                                  " into your Meter? (yes/no): ").lower()
            if elect_payment == "yes":
                def elect_pin():
                    pin = input("Enter your PIN: ")
                    try:
                        pin = int(pin)
                    except:
                        print("Invalid input, only numbers accepted")
                    if pin == 1234:
                        print("You have successfully recharged your Meter, the sum of ₦" + str(elect_amount) +
                              " has been deducted from your account.")
                    else:
                        print("Incorrect PIN, please try again")
                        elect_pin()


                elect_pin()
            else:
                print("Sorry, the transaction was not successful")
        else:
            print("Sorry, there is no option " + elect_biller)
    else:
        print("Sorry, there is no option " + bills)
elif choice == "e":
    def real_pin():
        current_pin = input("Please enter your current PIN: ")
        try:
            current_pin = int(current_pin)
        except:
            print("Invalid input, only numbers accepted")
        if current_pin == 1234:
            new_pin = input("Please enter your new PIN: ")
            try:
                new_pin = int(new_pin)
            except:
                print("Invalid input, only numbers accepted")
            confirm_pin = input("Please confirm your PIN: ")
            try:
                confirm_pin = int(confirm_pin)
            except:
                print("Invalid input, only numbers accepted")
            if new_pin == confirm_pin:
                print("You have successfully changed your PIN, your new PIN is " + str(new_pin))
            else:
                print("Sorry the PIN did not match, please try again")
        else:
            print("Incorrect PIN, please try again")
            real_pin()


    real_pin()
else:
    print("Sorry, there is no option " + choice)
