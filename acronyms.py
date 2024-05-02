def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False

    with open('acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break

    if not found: 
        print('The acronym was not found ')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + " - " + definition + '\n')
        
def main()