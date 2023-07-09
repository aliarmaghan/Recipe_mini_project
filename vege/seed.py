from faker import Faker
fake = Faker()
import random
from .models import *

def seed_db(n=10)-> None:
    try:

        for i in range(0, n):
            dept_objs = Department.objects.all()
            random_idx = random.randint(0, len(dept_objs)-1)
            student_id      = f'STU-0{random.randint(10, 99)}'
            department      = dept_objs[random_idx]
            student_name    = fake.name()
            student_email   = fake.email()
            student_age     = random.randint(19,30)
            student_address = fake.address()


            student_id_obj =  StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department  =  department,     
                student_id   =  student_id_obj ,    
                student_name =  student_name,   
                student_email=  student_email,  
                student_age  =  student_age, 
                student_address =  student_address,
            )
    except Exception as e:
        print(e)