import random
import string
import hashlib
import json

class PasswordManager:
    def __init__(self):
        self.username = None
        self.passwords = {}

    def generate_random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        return password

    def is_strong_password(self, password):
        return (
            len(password) >= 8
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in string.punctuation for char in password)
        )

    def get_user_password(self):
        while True:
            password = input("Choisissez un mot de passe : ")

            if len(password) < 8:
                print("Le mot de passe doit contenir au moins huit caractères.")
            elif not any(char.isupper() for char in password):
                print("Le mot de passe doit contenir au moins une lettre majuscule.")
            elif not any(char.islower() for char in password):
                print("Le mot de passe doit contenir au moins une lettre minuscule.")
            elif not any(char.isdigit() for char in password):
                print("Le mot de passe doit contenir au moins un chiffre.")
            elif not any(char in string.punctuation for char in password):
                print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
            else:
                return password

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def save_password_to_file(self):
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}

        data[self.username] = self.passwords[self.username]

        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)  # Correction de l'indentation

    def main(self):
        self.username = input("Entrez votre nom d'utilisateur : ")
        password = self.get_user_password()

        hashed_password = self.hash_password(password)
        self.passwords[self.username] = hashed_password

        self.save_password_to_file()

        print("Mot de passe enregistré avec succès.")

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.main()

