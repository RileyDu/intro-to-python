contacts = {
    'number' : 4,
    'students': 
        [
            {'name':'Riley DuBord', 'email':'rileydu@example.com'},
            {'name':'Harry Potter', 'email':'harry@example.com'},
            {'name':'Ron Weasley', 'email':'ron@example.com'},
            {'name':'Hermione Granger', 'email':'hermione@example.com'},
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])