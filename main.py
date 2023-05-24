import os

# Define the filename for the staff record file
staffrecord_filename = "staffrecord.txt"

# Define the commission and bonus percentages
commission_percent = 0.05
bonus_percent = 0.07


# Function to calculate the staff's monthly commission
def calculate_monthly_commission(monthly_sales):
    return monthly_sales * commission_percent


# Function to calculate the staff's yearly bonus
def calculate_yearly_bonus(yearly_sales):
    return yearly_sales * bonus_percent


# Function to prompt the user for staff information and calculate incentives
def prompt_for_staff_info():
    full_name = input("Enter the staff's full name: ")
    contact_info = input("Enter the staff's contact info: ")
    position = input("Enter the staff's position: ")
    monthly_sales = float(input("Enter the staff's monthly sales: "))
    yearly_sales = monthly_sales * 12

    monthly_commission = calculate_monthly_commission(monthly_sales)
    yearly_bonus = calculate_yearly_bonus(yearly_sales)
    total_incentive = monthly_commission + yearly_bonus

    return {
        "full_name": full_name,
        "contact_info": contact_info,
        "position": position,
        "monthly_sales": monthly_sales,
        "yearly_sales": yearly_sales,
        "monthly_commission": monthly_commission,
        "yearly_bonus": yearly_bonus,
        "total_incentive": total_incentive
    }


# Function to save staff information and incentives to the staff record file
def save_staff_info(staffs_info):
    with open(staffrecord_filename, "a") as staffrecords_file:
        staffrecords_file.write(
            f"{staffs_info['full_name']},{staffs_info['contact_info']},{staffs_info['position']},{staffs_info['monthly_sales']},"
            f"{staffs_info['yearly_sales']},{staffs_info['monthly_commission']},{staffs_info['yearly_bonus']},{staffs_info['total_incentive']}\n"
        )


# Main program loop
while True:
    print("\nWelcome to the staff Bonus Calculations!")

    print()
    user_choice = input("1 to add a new staff record\n2 to view all staff records \n3 quit\nPlease enter the "
                        "following number to do: ")

    if user_choice == "1":
        for i in range(10):
            staff_info = prompt_for_staff_info()
            save_staff_info(staff_info)
            print("Staff record saved.")

    elif user_choice == "2":
        if os.path.isfile(staffrecord_filename):
            with open(staffrecord_filename, "r") as staffrecord_file:
                staff_records = staffrecord_file.readlines()
                if staff_records:
                    print("Staff Records:")
                    for record in staff_records:
                        record_parts = record.strip().split(",")
                        print(
                            f"Full Name: {record_parts[0]}, Contact Info: {record_parts[1]}, Position: {record_parts[2]}, "
                            f"Monthly Sales: {record_parts[3]}, Yearly Sales: {record_parts[4]}, Monthly Commission: {record_parts[5]}, "
                            f"Yearly Bonus: {record_parts[6]}, Total Incentive: {record_parts[7]}")
                else:
                    print("No staff records found.")
        else:
            print("No staff records found.")

    elif user_choice == "3":
        break

    else:
        print("Invalid choice")

