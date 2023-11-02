import re
import hashlib
import getpass
import os
import matplotlib.pyplot as plt 

# Function to check the validity of an email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to check the validity of a password
def is_valid_password(pwd):
    return len(pwd) >= 8 and any(char.isupper() for char in pwd) and any(char.islower() for char in pwd) and any(char.isdigit() for char in pwd) and any(not char.isalnum() for char in pwd)

# Function to save user credentials in the "Enregistrement.txt" file
def enregistrer_identifiants(email, password):
    with open("Enregistrement.txt", "a") as file:
        file.write(f"Email: {email}, Pwd: {password}\n")

# Function to authenticate the user
def authentifier():
    email = input("Entrez votre email : ")
    password = getpass.getpass("Entrez votre mot de passe : ")

    with open("Enregistrement.txt", "r") as file:
        credentials = file.readlines()

    for line in credentials:
        if f"Email: {email}, Pwd: {password}\n" in line:
            print("Authentification réussie.")
            afficher_menu_principal()
            return

    print("Identifiants incorrects. Vous devez vous enregistrer.")
    enregistrer()

# Function to hash a word using SHA-256
def hacher_mot():
    mot = getpass.getpass("Entrez le mot à hacher : ")
    hashed = hashlib.sha256(mot.encode()).hexdigest()
    print("Mot haché avec SHA-256:", hashed)

# Function to perform a dictionary attack
def attaquer_par_dictionnaire():
    mot_cible = getpass.getpass("Entrez le mot cible : ")
    with open("dictionnaire.txt", "r") as file:
        words = file.readlines()
        for word in words:
            if word.strip() == mot_cible:
                print("Mot trouvé dans le dictionnaire.")
                return
        print("Mot non trouvé dans le dictionnaire.")

# Function for Caesar cipher
def chiffrement_cesar():
    mot = input("Entrez le mot à chiffrer : ")
    decalage = int(input("Entrez le décalage (entier) : "))
    chiffre = ""
    for char in mot:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            chiffre += chr(((ord(char) - shift + decalage) % 26) + shift)
        else:
            chiffre += char
    print("Message chiffré :", chiffre)

# Function for Caesar cipher decryption
def dechiffrement_cesar():
    mot = input("Entrez le mot à déchiffrer : ")
    decalage = int(input("Entrez le décalage (entier) : "))
    dechiffre = ""
    for char in mot:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            dechiffre += chr(((ord(char) - shift - decalage) % 26) + shift)
        else:
            dechiffre += char
    print("Message déchiffré :", dechiffre)

# Function to collect a dataset
def collecter_dataset():
    print("Dataset sous forme de dictionnaire :")
    dataset = {
        "Lundi": 100,
        "Mardi": 200,
        "Mercredi": 150,
        "Jeudi": 300,
        "Vendredi": 250,
        "Samdi": 350,
        "Dimanche": 400,
    }
    for key, value in dataset.items():
        print(f"{key}: {value}")

# Function to display the main menu
def afficher_menu_principal():
    while True:
        print("\nMenu Principal :")
        print("A- Donnez un mot à hacher")
        print("B- Décalage par César")
        print("C- Collecter une Dataset")
        print("D- Quitter")

        choix = input("Choisissez une option : ")

        if choix == "A":
            afficher_sous_menu_a()
        elif choix == "B":
            afficher_sous_menu_b()
        elif choix == "C":
            afficher_sous_menu_c()
        elif choix == "D":
            break
        else:
            print("Option non valide. Veuillez choisir une option valide.")

# Function to display sub-menu A
def afficher_sous_menu_a():
    while True:
        print("\nSous-menu A :")
        print("a- Hacher le mot par SHA-256")
        print("b- Attaquer par dictionnaire le mot inséré")
        print("d- Revenir au menu principal")

        sous_choix = input("Choisissez une option : ")

        if sous_choix == "a":
            hacher_mot()
        elif sous_choix == "b":
            attaquer_par_dictionnaire()
        elif sous_choix == "d":
            break

# Function to display sub-menu B
def afficher_sous_menu_b():
    while True:
        print("\nSous-menu B :")
        print("a- Donnez un mot à chiffrer")
        print("b- Chiffrer le message (a)")
        print("c- Déchiffrer le message (b)")
        print("d- Revenir au menu principal")

        sous_choix = input("Choisissez une option : ")

        if sous_choix == "a":
            chiffrement_cesar()
        elif sous_choix == "b":
            dechiffrement_cesar()
        elif sous_choix == "c":
            continue
        elif sous_choix == "d":
            break

# Function to display charts
def afficher_courbes():
    # Sample data for the chart
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [10, 25, 15, 30]

    # Create a bar chart
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Sample Bar Chart')
    plt.show()
    
# Function to display sub-menu C
def afficher_sous_menu_c():
    while True:
        print("\nSous-menu C :")
        print("a- Afficher la dataset sous forme de dictionnaire")
        print("b- Afficher des courbes de votre choix")
        print("c- Revenir au menu principal")

        sous_choix = input("Choisissez une option : ")

        if sous_choix == "a":
            collecter_dataset()
        elif sous_choix == "b":
            afficher_courbes()  # Call the chart function
        elif sous_choix == "c":
            return  # Return to the main menu

# Function to register a new user
def enregistrer():
    email = input("Entrez votre email : ")
    password = getpass.getpass("Entrez votre mot de passe : ")

    if is_valid_email(email) and is_valid_password(password):
        enregistrer_identifiants(email, password)
        print("Enregistrement réussi.")
    else:
        print("Email ou mot de passe non valide. L'enregistrement a échoué.")

# Main program
if __name__ == "__main__":
    # Ensure "Enregistrement.txt" file exists
    if not os.path.exists("Enregistrement.txt"):
        open("Enregistrement.txt", "w").close()

    while True:
        print("\nBienvenue dans le système d'authentification et de chiffrement.")
        print("1- Authentification")
        print("2- S'enregistrer")
        print("3- Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            authentifier()
        elif choix == "2":
            enregistrer()
        elif choix == "3":
            break
        else:
            print("Option non valide. Veuillez choisir une option valide.")
