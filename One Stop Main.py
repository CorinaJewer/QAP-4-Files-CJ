# One Stop Insurance Company needs a program to enter and calculate new insurance policy information.
# Written By: Corina Jewer
# Date: July 24, 2023

# Libraries

import datetime
import time
import FormatValues as FV
from tqdm import tqdm

CurrDate = datetime.datetime.now()

# Open the defaults file and read the values into variables.

f = open("OSICDef.dat", "r")

NEXT_POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DIS = float(f.readline())
EXTRA_LIABILITY_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_COV = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())

f.close()

# Define Required Functions


def Validate_Format_Phone_Number(PhoneNum):

    if len(PhoneNum) != 10:
        print("Invalid - The phone number must contain 10 digits (9999999999).")
    elif PhoneNum == "":
        print("Invalid - The phone number cannot be blank.")
    elif not PhoneNum.isdigit():
        print("Invalid - The phone number must contain numeric values.")
    else:
        FormattedPhoneNum = f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"
        return FormattedPhoneNum


# Main Program

while True:

    CustFirst = input("Please enter the customer's first name (END to quit): ").title()
    if CustFirst == "End":
        break
    CustLast = input("Please enter the customer's last name: ").title()
    Address = input("Please enter the customer's street address: ").title()
    City = input("Please enter the city: ").title()

    ValidProvList = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    while True:
        Prov = input("Please enter the province: ").upper()
        if Prov == "":
            print("Error - Province cannot be left blank. Please enter a valid province.")
        elif Prov not in ValidProvList:
            print("Error - Province must be AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, or YT. Please re-enter")
        else:
            break
    PostalCode = input("Please enter the postal code: ").upper()
    PhoneNum = input("Please enter the customer's phone number (999-999-9999): ")
    Validate_Format_Phone_Number(PhoneNum)
    NumCars = int(input("Please enter the number of vehicles insured: "))
    ExtraLiability = input("Does the customer require extra liability up to $1,000,000 (Y/N)?: ").upper()
    OptionGlass = input("Does the customer require optional glass coverage (Y/N)? ").upper()

    OptionLoaner = input("Does the customer require an optional loaner car (Y/N)? ").upper()

    PayMethodList = ["Full", "Monthly"]
    while True:
        PayType = input("Would the customer like to pay in full or by monthly installments (Full or Monthly): ").title()
        if PayType == "":
            print("Error - Payment method cannot be left blank. Please enter a valid payment method.")
        elif PayType not in PayMethodList:
            print("Error - Payment Method must be Full or Monthly. Please re-enter")
        else:
            break

# Calculations

    if NumCars == 1:
        InsurancePrem = BASIC_PREM
    elif NumCars > 1:
        InsurancePrem = BASIC_PREM + ((BASIC_PREM - (BASIC_PREM * ADD_CAR_DIS)) * (NumCars - 1))
    else:
        print("Please enter the number of vehicles you would like to insure.")

    TotLiabilityChg = NumCars * EXTRA_LIABILITY_COV
    TotGlassChg = NumCars * GLASS_COV
    TotLoanerChg = NumCars * LOANER_COV

    TotExtraChg = TotLiabilityChg + TotGlassChg + TotLoanerChg

    TotInsurancePrem = InsurancePrem + TotExtraChg

    HST = TotInsurancePrem * HST_RATE

    TotalCost = TotInsurancePrem + HST

    MonthlyPay = (TotalCost + PROCESS_FEE)/8

    InvDate = CurrDate

    NextPayDate = (datetime.datetime.now().replace(day=1) +
                   datetime.timedelta(days=32)).replace(day=1).strftime("%Y-%m-%d")


# Display Receipt

    print()
    print("==== Insurance Information Receipt ====")
    print()
    print("Invoice Date:", datetime.datetime.now().strftime("%Y-%m-%d"))
    print()
    print(F"{CustFirst} {CustLast}")
    print(f"{Address}")
    print(f"{City}, {Prov}, {PostalCode}")
    print(f"{Validate_Format_Phone_Number(PhoneNum)}")
    print()
    print("======== Insurance Information ========")
    print()
    print(f"Policy Number:              {NEXT_POLICY_NUM:>11d}")
    print(f"Number of Vehicles Insured: {NumCars:>11d}")
    print(f"Extra Liability Coverage:   {ExtraLiability:>11s}")
    print(f"Optional Glass Coverage:    {OptionGlass:>11s}")
    print(f"Optional Loaner Car:        {OptionLoaner:>11s}")
    print(f"Payment Method:             {PayType:>11s}")
    print()
    print("======== Total Cost Breakdown =========")
    print()
    print(f"Insurance Premium:          {FV.FDollar2(InsurancePrem):>11s}")
    print(f"Total Extra Charges:        {FV.FDollar2(TotExtraChg):>11s}")
    print(f"HST:                        {FV.FDollar2(HST):>11s}")
    print(f"Total Cost:                 {FV.FDollar2(TotalCost):>11s}")
    print(f"Monthly Payment:            {FV.FDollar2(MonthlyPay):>11s}")
    print(f"Next Payment Date:          {NextPayDate:>11s}")
    print()
    print("=======================================")
    print()
    print("Thank you for choosing One Stop Insurance.")
    print()

# Progress Bar

    print("This will just take a moment - we're busy writing your data for future reference.")

    for _ in tqdm(range(50), desc="WritingData ", unit="ticks", ncols=100, bar_format="{desc}{bar}"):
        time.sleep(.1)
    print("Policy information processed and saved.")
    time.sleep(1)

# Write values to Policies.dat.

    f = open("Policies.dat", "a")

    f.write(f"{str(NEXT_POLICY_NUM)}, ")
    Date = CurrDate.strftime("%Y-%m-%d")
    f.write(f"{Date}, ")
    f.write(f"{CustFirst}, ")
    f.write(f"{CustLast}, ")
    f.write(f"{Address}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostalCode}, ")
    f.write(f"{Validate_Format_Phone_Number(PhoneNum)}, ")
    f.write(f"{str(NumCars)}, ")
    f.write(f"{ExtraLiability}, ")
    f.write(f"{OptionGlass}, ")
    f.write(f"{OptionLoaner}, ")
    f.write(f"{PayType}, ")
    f.write(f"{str(TotInsurancePrem)}\n")

    f.close()

# Update default values as per processing.

    NEXT_POLICY_NUM += 1

# Housekeeping

# Write Current Values Back to OSICDef.dat.

    f = open('OSICDef.dat', 'w')

    f.write(f"{NEXT_POLICY_NUM}\n")
    f.write(f"{BASIC_PREM}\n")
    f.write(f"{ADD_CAR_DIS}\n")
    f.write(f"{EXTRA_LIABILITY_COV}\n")
    f.write(f"{GLASS_COV}\n")
    f.write(f"{LOANER_COV}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")

    f.close()
