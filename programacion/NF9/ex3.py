

def age_prove(user_age):
    of_age = 0

    if user_age >= 18:
        of_age = 1
    
    return of_age

def main():
    user_input = int(input("Introdueix la seba edat:\n"))
    of_age = age_prove(user_input)

    if of_age == 1:
        print("Ets major d'edat.")
    else:
        print("No ets major d'edat.")

if __name__ == "__main__":
    main()