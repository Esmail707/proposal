import json
from check import check_for_error

def insert(obj, file):
    with open(f"{file}.ndjson", 'a') as file:
        file.write('\n')
        json.dump(obj, file)

def add_one_class():
    pass

def add_student():
    # keys = ['id', 'name', 'surname', 'age', 'undergraduate_year', 'classes']
    with open('students.ndjson', 'r') as file:
        students = [json.loads(line) for line in file if line.strip()]
    with open('classes.ndjson', 'r') as file:
        clss = [json.loads(line) for line in file if line.strip()]
    add_std = 'y'
    while add_std == 'y' or add_std == 'Y':
        try:
            id = int(input('Please enter an ID for the student \n'))
        except:
            print('chars are not allowd in ID \n')
            continue
        if id > 9999 or id < 0:
            print('ID must be >= 0 and <= 9999\n')
            continue
        cont = False
        for student in students:
            if int(student['id'][1:]) != id: continue
            print('The ID you choosed is already associated with one of the students pick another ID\n')
            cont = True
            break
        if cont: continue
        id = '#' + str(id)
        print('ID added \n')
        # --------------------------------------------------------------------
        name, surname, age, undergraduate_year, classes = "1", "1", -1, -1, []
        while len(name) == 0 or not name.isalpha():
            name = input('Please enter the student name, name must not be empty and must not contain any numbers\n')
        print('name added \n')
        # -------------------------------------------------
        while len(surname) == 0 or not surname.isalpha():
            surname = input('Please enter the student surname, surname must not be empty and must not contain any numbers\n')
        print('surname added \n')
        # -----------------------------------------------------
        while age < 16 or age > 90:
            try:
                age = int(input('Please enter the student age, age must be >= 16 and <= 90 \n'))
            except:
                print('chars are not allowd in age \n')
                continue
        print('age added \n')
        # ---------------------------------------------------
        while undergraduate_year < 1 or undergraduate_year > 4:
            try:
                undergraduate_year = int(input('Please enter the student undergraduate year, it must be >= 1 and <= 4\n'))
            except:
                print('chars are not allowd in age\n')
                continue
        print('undergraduate year added\n')
        # --------------------------------------------
        add_cls = "y"
        while add_cls == 'y' or add_cls == 'Y':
            class_name = input('Enter class name or ID to be added to the students classes\n')
            if len(class_name):
                in_classes = False
                for cls in clss:
                    if cls['name'] != class_name and cls['id'][1:] != class_name: continue
                    in_classes = True
                    classes.append(class_name)
                    break
                if not in_classes:
                    print(f'This {class_name} was not found in all the Classes\n')
                    create_class = input('Would you like to create This class (y/N)?\n')
                    if create_class == 'y' or create_class == 'Y':
                        cls = add_one_class()
                        clss.append(cls)
                        classes.append(class_name)
                        print('class Added successfully')
                else:
                    print('class Added succesfully')
            add_cls = input('Do you want to add anoteher class (y/N)?\n')
        # ------------------------------------------------------------------------
        obj = {'id': id, 'name': name, 'surname': surname, 'age': age, 'undergraduate_year': undergraduate_year, 'classes': classes}
        insert(obj, 'students')
        students.append(obj)
        add_std = input('Would you like to add another studend (y/N)?\n')
        # ----------------------------------------------------------------------------------

def main():
    add_student()

main()