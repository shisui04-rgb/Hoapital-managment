from datetime import datetime

def validate_date(date_str):
    """Validate the date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
         return False

def validate_mobile_number(mobile_str):
    """Validate the mobile number (should be numeric and of a specific length)."""
    return mobile_str.isdigit() and len(mobile_str) == 10 #Adjust the length as nedded

def validate_batch_number(batch_str):
    """validate that the batch nimber is numeric"""
    return batch_str.isdigit()

def get_patient_details():
    """Collect and validate patient details"""
    Name = input("Enter Patient Name:").strip()


    DoB = input("Enter Date of Birth (YYYY-MM-DD):").strip()
    while not validate_date(DoB):
        print("Invalid date formate.Enter correct date format")
        DoB = input("Enter Date of Birth(YYYY-MM-DD):").strip()


    Mobile_No = input("Enter Mobile Number:").strip()
    while not validate_mobile_number(Mobile_No):
        print("Invalid mobile number.Please Enter valid mobile number:")
        Mobile_No = input("Enter Mobile Number:").strip()


    Batch_No = input("Enter Batch No.:").strip()
    while not validate_batch_number(Batch_No):
        print("Invalid batch number.please Enter a numeric value")
        Batch_No = input("Enter Batch No.:").strip()

    return {
    "Name" : Name,
    "Date of Birth" : DoB,
    "Mobile Number" : Mobile_No,
    "Batch Number" : int(Batch_No)   #convert to integer after validation
    } 
def main():
    "Main function to run the patient managment system"
    print("Welcome to the peitent Managment System")
    patient_data = get_patient_details()

    ## Chechking if my all data is entered
    if all(patient_data.values()):
        print("All data entered successfully.")
        for key, value in patient_data.items():
            print(f"{key}: {value}")
    else:
        print("some error found in the data entered")


if __name__ == "__main__":
   main()
