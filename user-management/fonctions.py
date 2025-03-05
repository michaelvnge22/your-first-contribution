

def register(email: str, password: str):
    with open(file_name, "a") as f:
        f.write(f"\n Email: {email} \n Password: {password}:USER")
        print("Inscription réussie !")