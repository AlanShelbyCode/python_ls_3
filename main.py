from models import Plant, Employee, Salon

while True:
    print(
        "Choose a menu item by number: \n" +
        "1. Add new Plant \n" +
        "2. Add new Employee \n" +
        "3. Add new Salon \n" +
        "4. Get plant by id \n" +
        "5. Get employee by id \n"+
        "6. Get salon by id \n"
    )
    try:
        menu_flag = int(input("Your choose: "))
    except ValueError:
        print("You need to write number of menu!")
        continue
    if menu_flag == 1:
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
       # print(plant)
        plant.save()
    elif menu_flag == 2:
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        salon_id = int(input("Salon id: "))
        employee = Employee(id, name, email, department_type, department_id, salon_id)
        employee.save()
    elif menu_flag == 3:
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        salon_director_id = int(input("Salon director ID: "))
        salon = Salon(id, location, name, salon_director_id)
        salon.save()
    elif menu_flag == 4:
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)
    elif menu_flag == 5:
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)
    elif menu_flag == 6:
        id = int(input("ID: "))
        salon = Salon.get_by_id(id)
        print(salon)
