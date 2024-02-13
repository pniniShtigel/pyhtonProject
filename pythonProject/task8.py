import pandas as pd
import numpy as np
import os
import re
from typing import List

class UserManipulation:
    def __init__(self):
        self.usernames = []

    def read_users(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                self.usernames = [line.strip() for line in file]
        except FileNotFoundError:
            print(f"Error: Users file not found at '{file_path}'.")

    def get_first_10_percent(self) -> List[str]:
        return self.usernames[:int(len(self.usernames) * 0.1)]

    def process_usernames(self):
        pass

    def read_emails(self, file_path: str):
        pass

    def filter_gmail_addresses(self) -> List[str]:
        pass

    def check_email_username_relationship(self, email_list: List[str], username_list: List[str]) -> List[bool]:
        pass

    def convert_and_count_letter_A(self, name: str) -> int:
        pass

    def add_names_to_list(self, names: List[str]):
        pass


user_manipulator = UserManipulation()
user_manipulator.read_users("path/to/users.txt")
usernames_sample = user_manipulator.get_first_10_percent()
user_manipulator.process_usernames()
user_manipulator.read_emails("path/to/emails.txt")
gmail_addresses = user_manipulator.filter_gmail_addresses()
relationship_results = user_manipulator.check_email_username_relationship(gmail_addresses, usernames_sample)
converted_counts = [user_manipulator.convert_and_count_letter_A(name) for name in usernames_sample]
user_manipulator.add_names_to_list(usernames_sample)


