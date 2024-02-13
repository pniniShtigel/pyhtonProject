from task1 import DataReader,DataWriter
import pandas as pd

def main():

    data_reader = DataReader()
    data_writer = DataWriter()


    user_data = data_reader.read_excel("C:/Users/user1/Desktop/תכנות/pyton/project/text.xlsx")

    if user_data is not None:
        print("User Data:")
        print(user_data.head())
        user_manipulator = DataWriter()
        usernames_sample = user_manipulator.get_first_10_percent()
        user_manipulator.process_usernames()
        user_manipulator.read_emails("C:/Users/user1/Desktop/תכנות/pyton/project/emails.txt")
        gmail_addresses = user_manipulator.filter_gmail_addresses()
        print("Filtered Gmail Addresses:")
        print(gmail_addresses)
        relationship_results = user_manipulator.check_email_username_relationship(gmail_addresses, usernames_sample)
        print("Email-Username Relationship Results:")
        print(relationship_results)

        converted_counts = [user_manipulator.convert_and_count_letter_A(name) for name in usernames_sample]
        print("Converted Counts:")
        print(converted_counts)

        user_manipulator.add_names_to_list(usernames_sample)

        data_writer.save_to_excel(usernames_sample, "C:/Users/user1/Desktop/תכנות/pyton/project/processed_data.xlsx")

if __name__ == "__main__":
    main()
