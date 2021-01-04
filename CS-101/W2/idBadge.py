print("Please enter the following information:\n")

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
starting_month = input("Starting month: ")
advanced_training = input("Advanced training: ")

print("\nThe ID Card is:\n\
----------------------------------------\n" +
last_name.upper() + ", " + first_name.title() + "\n" +
job_title.title() + "\n" +
"ID: " + id_number + "\n\n" +
email_address.lower() + "\n" +
phone_number + "\n")
print(f"{'Hair: ' + hair_color.title():<20} Eyes: {eye_color.title()}")
print(f"{'Month: ' + starting_month.title():<20} Training: {advanced_training.title()}")
print("----------------------------------------")
