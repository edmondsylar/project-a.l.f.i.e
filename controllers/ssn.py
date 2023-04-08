import random

def generate_random_number():
    first_part = str(random.randint(100, 999))
    second_part = str(random.randint(10, 99))
    third_part = str(random.randint(1000, 9999))
    return first_part + '-' + second_part + '-' + third_part

# print(generate_random_number())

def generate_ssn(pre_2011=True, state_code='NY'):
    area_codes = {
        'NY': '050-134',
        # ...
    }
    if pre_2011:
        area_number = random.randint(int(area_codes[state_code].split('-')[0]), int(area_codes[state_code].split('-')[1]))
        group_number = random.randint(1, 99)
        serial_number = random.randint(1, 9999)
        ssn = f'{area_number:03}-{group_number:02}-{serial_number:04}'
    else:
        ssn = f'{random.randint(1, 899):03}-{random.randint(1, 99):02}-{random.randint(1, 9999):04}'
    return ssn

print('Pre-2011 SSN:', generate_ssn(pre_2011=True, state_code='NY'))
print('Post-2011 SSN:', generate_ssn(pre_2011=False))