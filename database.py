import psycopg2
from employee import Employee
from datetime import datetime
import random

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="employee",
            user="postgres",
            password="@Muhsin6996",
            host="localhost"
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            birth_date DATE NOT NULL,
            gender VARCHAR(10) NOT NULL
        );
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()
        print("Table created successfully.")

    def insert_employee(self, employee):
        insert_query = '''
        INSERT INTO employees (full_name, birth_date, gender) VALUES (%s, %s, %s)
        '''
        self.cursor.execute(insert_query, (employee.full_name, employee.birth_date, employee.gender))
        self.conn.commit()
        print(f"Employee {employee.full_name} added.")

    def print_employees(self):
        select_query = '''
        SELECT full_name, birth_date, gender FROM employees
        ORDER BY full_name;
        '''
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        for row in rows:
            full_name, birth_date, gender = row
            age = Employee.calculate_age(birth_date)
            print(f"Name: {full_name}, Birth Date: {birth_date}, Gender: {gender}, Age: {age}")

    def bulk_insert_employees(self):
        male_names = ["Ivan", "Petr", "Sergey", "Alex", "Fedor"]
        female_names = ["Anna", "Maria", "Olga", "Elena", "Sofia"]
        surnames = ["Ivanov", "Petrov", "Sidorov", "Fedorov", "Kuznetsov"]

        employees = []
        for _ in range(1000000):
            gender = "Male" if random.choice([True, False]) else "Female"
            first_name = random.choice(male_names) if gender == "Male" else random.choice(female_names)
            surname = random.choice(surnames)
            full_name = f"{surname} {first_name} {first_name[0]}."
            birth_date = datetime(1990 + random.randint(0, 30), random.randint(1, 12), random.randint(1, 28))
            employee = Employee(full_name, birth_date.strftime("%Y-%m-%d"), gender)
            employees.append(employee)
        
        # Insert employees in batches
        for i in range(0, len(employees), 1000):
            batch = employees[i:i+1000]
            insert_query = '''
            INSERT INTO employees (full_name, birth_date, gender) VALUES (%s, %s, %s)
            '''
            data = [(emp.full_name, emp.birth_date, emp.gender) for emp in batch]
            self.cursor.executemany(insert_query, data)
            self.conn.commit()
        print("1,000,000 employees inserted.")

    def find_employees_by_criteria(self):
        start_time = datetime.now()
        query = '''
        SELECT full_name, birth_date, gender FROM employees
        WHERE gender = 'Male' AND full_name LIKE 'F%';
        '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        for row in rows:
            full_name, birth_date, gender = row
            age = Employee.calculate_age(birth_date)
            print(f"Name: {full_name}, Birth Date: {birth_date}, Gender: {gender}, Age: {age}")
        
        print(f"Execution time: {execution_time} seconds")
        return execution_time

    def optimize_database(self):
        # Add an index to optimize search by gender and full_name
        print("Optimizing database...")
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_gender_fullname ON employees (gender, full_name);")
        self.conn.commit()
        print("Optimization complete.")

    def __del__(self):
        self.conn.close()
