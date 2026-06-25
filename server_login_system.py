# P.S.) This Project-System took me a whole day, 5+ hours (noon until evening), to get to the correct System-architecture (flows), for making it work correctly.
# It was mentally daunting, not going away until I cracked the correct Logic behind it and build it fully correctly.
# It was terribly amazing!


users = {
    "lauren" : "secret123",
    "louise" : "psswrd3215",
    "matteusz" : "water33PP"
}

def verify_login(username, password):
    
    if username in users:

        correct_password = users[username]

        if password == correct_password:
            return "Login successful"
        else:
            return "Password incorrect"
        
    else:
        return "User unknown"
    

given_name = input("Give your name: ")
given_pass = input("Give your password: ")


verification_check = verify_login(given_name, given_pass)
print(verification_check)
