import sqlite3
import time
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id))

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `time_sup` = ? WHERE `user_id` = ?", (time_sub, user_id))

    def get_time_sup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sup` FROM `users` WHERE `user_id` = ?", (user_id)).fetchall()
            for row in result:
                time_sub = int(row[0])
            return time_sub

    def get_sup_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub > int(time.time()):
                return True
            else:
                return False

    def get_user_page(self, user_id):
        # Retrieve the current page for the user from the database
        with self.connection:
            self.cursor.execute("SELECT `page` FROM `users` WHERE `user_id` = ?", (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result else 1

    def set_user_page(self, user_id, page):
        # Set the current page for the user in the database
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `page` = ? WHERE `user_id` = ?", (page, user_id))
            self.connection.commit()

    def get_current_page(self, user_id, module='module1'):
        with self.connection:
            self.cursor.execute("SELECT page FROM `users` WHERE user_id = ? AND module = ?", (user_id, module))
            result = self.cursor.fetchone()
            return result[0] if result else 1

    def update_current_page(self, user_id, page, module='module1'):
        # Update the current page in the database for the specified module
        pass


    def set_invoice_message_id(self, user_id, message_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `invoice_message_id` = ? WHERE `user_id` = ?", (message_id, user_id))

    def get_invoice_message_id(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `invoice_message_id` FROM `users` WHERE `user_id` = ?",
                                         (user_id,)).fetchone()
            return result[0] if result else None

    def get_admin(self, user_id):

        with self.connection:
            result = self.cursor.execute("SELECT `admin` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchone()

            return result[0] == 1 if result else False

    def get_all_users(self):

        with self.connection:
            self.cursor.execute("SELECT * FROM `users`")

            return self.cursor.fetchall()

    def is_admin(self, user_id: int) -> bool:
        # Replace with your actual database query to check if the user is an admin
        # This is just a placeholder example
        with self.connection:
            result = self.cursor.execute("SELECT `admin` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchone()
            return result is not None and result[0] != 0

    # Function to get a list of users and their admin statuses
    def get_total_users(self) -> int:
        # Replace with your actual database query to get the total number of users
        # This is just a placeholder example
        with self.connection:
            result = self.cursor.execute("SELECT COUNT(*) FROM `users`").fetchone()
            return result[0] if result else 0

    # Function to get a list of users and their subscription statuses
    def get_subscribed_users(self) -> int:
        # Replace with your actual database query to get the number of subscribed users
        # This is just a placeholder example
        with self.connection:
            result = self.cursor.execute("SELECT COUNT(*) FROM `users` WHERE `time_sup` > 0").fetchone()
            return result[0] if result else 0
