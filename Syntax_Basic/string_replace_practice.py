greeting_template = '''

Assalam O Alaikum!

Dear <| name |>

Regards: 

<| author |>

'''
# replace will not modify original string

Name = input('Enter Name : ')
Author = input('Enter Sender Name : ')

greeting_template = greeting_template.replace('<| name |>',Name)
greeting_template = greeting_template.replace('<| author |>',Author)

print(greeting_template)