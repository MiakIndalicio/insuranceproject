import os
import csv

input_file_path = 'E:\\Cody\\Documents\\insurance project\\python-portfolio-project-starter-files\\insurance.csv'
output_file_path = 'E:\\Cody\\Documents\\insurance project\\python-portfolio-project-starter-files\\modified_insurance.csv'



with open(input_file_path, 'r') as file:
    input_file = csv.DictReader(file)
    for row in input_file:
        age = float(row['age'])
        sex = row['sex']
        bmi = row['bmi']
        children = row['children']
        smoker = row['smoker']
        region = row['region']
        costs = row['charges']
    
    
with open(input_file_path, 'r') as input_file:
    data = list(csv.DictReader(input_file))
    

    def average_age(data):
        total_age = 0
        count = 0
        for row in data:
            total_age += float(row['age'])
            count += 1
        return total_age / count

    print(f'The average age in this data set is: {average_age(data)}')

    def average_cost(data):
        total_cost = 0
        count = 0
        for row in data:
            total_cost += float(row['charges'])
            count += 1
        return total_cost / count
    
    print(f'The average cost of insurance is: {average_cost(data)}')


    def average_cost_for_smoker(data):
        filtered_data =  [float(row['charges']) for row in data if row['smoker ']== 'yes']
        if filtered_data:
            return sum(filtered_data) / len(filtered_data)
    
    print(f'The average cost for smokers is: {average_cost_for_smoker(data)}')

    def smokers_and_non_smokers(data):
        smoker = []
        non_smokers = []
        for row in data:
            if row['smoker'] == 'yes':
                smoker.append(row)
            else:
                non_smokers.append(row)
        return len(smoker), len(non_smokers)
    
    smoker_result = smokers_and_non_smokers(data)
    
    print(f'The number of smokers is: {smoker_result[0]} and the number of non smokers is: {smoker_result[1]}')

    def count_individuals_in_each_region(data):
        region_counts = {}
        for row in data:
            if 'region' in row:
                region = row['region']
                region_counts[region] = region_counts.get(region, 0) + 1
        return region_counts

    print(count_individuals_in_each_region(data))
    
    def people_with_children(data):
        with_children = []
        without_children = []
        for row in data:
            if float(row['children']) > 0:
                with_children.append(row)
            else:
                without_children.append(row)
        return len(with_children), len(without_children)
    
    children_result = people_with_children(data)
    
    print(f'The number of people with children is: {children_result[0]} and the number of people without children is: {children_result[1]}')
    
    def male_or_female(data):
        male = []
        female = []
        for row in data:
            if row['sex'] == 'male':
                male.append(data)
            else:
                female.append(data)
        return len(male), len(female)
    
    male_female_result = male_or_female(data)
    print(f'The amount of males in the data is: {male_female_result[0]} and the amount of females in the data is: {male_female_result[1]}')

# insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500 
# sex = 0 for female, 1 for male
# smoker = 0 for non smoker, 1 for smoker

def breakdown_insurance_cost(age, sex, bmi, num_of_children, smoker):
    # Coefficients
    age_coeff = 250
    sex_coeff = 128  # Assuming 128 for female, 0 for male
    bmi_coeff = 370
    children_coeff = 425
    smoker_coeff = 24000
    
    # Base cost
    base_cost = -12500
    
    # Breakdown components
    age_component = age_coeff * age
    sex_component = sex_coeff * sex
    bmi_component = bmi_coeff * bmi
    children_component = children_coeff * num_of_children
    smoker_component = smoker_coeff * smoker
    
    # Total breakdown
    total_breakdown = {
        'Age': age_component,
        'Sex': sex_component,
        'BMI': bmi_component,
        'Children': children_component,
        'Smoker': smoker_component,
        'Base Cost': base_cost
    }
    
    return total_breakdown

with open(input_file_path, 'r') as input_file:
    reader = list(csv.DictReader(input_file))
    data = list(reader)

fieldnames= ['id', 'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
with open(output_file_path, 'w', newline = '') as output_file:
    fieldnames = fieldnames
    writer = csv.DictWriter(output_file, fieldnames)
    writer.writeheader()
    id_counter = 1

    for row in data:
        row['id'] = id_counter
        id_counter += 1

    writer.writerows(data)
   
       
    
with open(output_file_path, 'r') as output_file:
    for row in output_file:
        print(row)
