employees = [
    {"name": "Ahmed", "department": "IT", "salary": 3000},
    {"name": "Omar", "department": "HR", "salary": 3500},
    {"name": "Ali", "department": "Production", "salary": 4000},
    {"name": "Sara", "department": "Finance", "salary": 4500}
]

for index, (name, department, salary) in enumerate(zip(names, departments, salaries), start=1):
    if salary > 3500:
        print(f"{index} - {name} - {department} - {salary}")

