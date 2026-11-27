
employees = [
    {"name": "Ahmed", "department": "IT", "salary": 3000},
    {"name": "Omar", "department": "HR", "salary": 3500},
    {"name": "Ali", "department": "Production", "salary": 4000},
    {"name": "Sara", "department": "Finance", "salary": 4500},
	{"name": "Nada", "department": "Finance", "salary": 5000}
	
]

for index, employee  in enumerate(employees , start=1):
        print(f"{index} - {employee ['name']} - {employee ['department']} - {employee ['salary']}")

print("please enter the department name to search its employee's")
dept=input()

def find_by_department(dept):
	for index, employee  in enumerate(employees , start=1):
		if employee ["department"]==dept:
			print(f"{index} - {employee ['name']} - {employee ['department']} - {employee ['salary']}")
	return()
find_by_department(dept)

def calculate_total_salary():
	total_salaries=0
	for employee in employees:
		total_salaries += employee ["salary"]
	return total_salaries

print(f"total salaries, {calculate_total_salary()}")

for employee in employees:
	if employee ["salary"] > 3500:
		print(f"{employee["name"]}, Has salary more than 3500")

department_list=[]
for employee in employees:
	if employee["department"]not in department_list:
		department_list.append(employee["department"])

def get_dept():
	dept_list=[]
	for employee in employees:
		if employee ["department"] not in dept_list:
			dept_list.append(employee ["department"])

	return dept_list



			
			
			
		
print(get_dept())
	
	
employees_salary=[]
for employee in employees:
	employees_salary.append(employee["salary"])

for department , salary in zip(department_list, employees_salary):
	print(f"{department},{salary}")




newind=0
for index in enumerate (employees, start=1):
		newind=index[0]

print(f"new employee id is: {newind+1}")
employees.append(newind+1)



print("please enter employee name")
name=input()
print ("please enter employee department")
department=input()
print ("please enter employee salary")
salary=int(input())
employees.append({"name": name, "department": department, "salary": salary})

for index, employee  in enumerate(employees , start=1):
        print(f"{index} - {employee ['name']} - {employee ['department']} - {employee ['salary']}")






		
		
