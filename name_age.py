def question():
    while True:
        name = input('What is your name? ')
        print('Hello '+name)
        age = input('How old are you? ')
        print(age + ' years old? damn u old!')
        if name == 'stop' and age == 'stop':
            quit()
        else:
            continue
question()