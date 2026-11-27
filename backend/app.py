employees = [
    {"name": "Ahmed", "department": "IT", "salary": 3000},
    {"name": "Omar", "department": "HR", "salary": 3500},
    {"name": "Ali", "department": "Production", "salary": 4000},
    {"name": "Sara", "department": "Finance", "salary": 4500}
]

for index, employee  in enumerate(employees , start=1):
        print(f"{index} - {employee ['name']} - {employee ['department']} - {employee ['salary']}")

print("please enter the department name to search its employee's")
dept=input()
def find_by_department(dept):
	for employee in employees:
    		print("HHHHHHHHHHH")
