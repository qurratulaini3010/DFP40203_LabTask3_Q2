import os

staff = [
    {"Name": "MION",
     "Contact Info": "missqurratulaini@gmail.com",
     "position": "chief Manager",
     "Monthly sales": "RM 10000",
     "Comission": "RM 50",
     "yearly Bonus": "RM 840",
     "Total Incentive": "RM 890",
     }
]


def inputinfo():
    name = input("Please enter your Full Name: ")
    contact = input("Please enter your contact Info: ")
    position = input("Please enter your position: ")
    monthlysales = int(input("Please enter your monthlysales: "))

    comm, bonus, incentive = calculate(monthlysales)

    if name:
        staff1 = {"Name": name,
                  "Contact Info": contact,
                  "position": position,
                  "Monthly sales": monthlysales,
                  "Comission": comm,
                  "yearly Bonus": bonus,
                  "Total Incentive": incentive, }
        staff.append(staff1)
        recordstaff()
    print("Your Comission is ", comm)
    print("Your Yearly Bonus is ", bonus)
    print("Your Total Incentive is ",  incentive)


def calculate(sales):
    commission = int(sales * 0.05)
    bonus = int((sales * 12) * 0.07)
    incentive = int(commission + bonus)
    return commission, bonus, incentive


def recordstaff():
    if not os.path.exists("staff"):
        os.makedirs("staff")

    for emp in staff:
        filename = f"staff/{emp['Name']}.txt"
        with open(filename, "a") as f:
            f.write(f"Name: {emp['Name']}\n Contact Info: {emp['Contact Info']}\n Position: {emp['position']}\
            \nMonthly Sales: RM {emp['Monthly sales']}\
            \nComission: RM {emp['Comission']}\nYearly Bonus: RM {emp['yearly Bonus']}\nTotal Incentive: RM {emp['Total Incentive']}\n\n")


inputinfo()
