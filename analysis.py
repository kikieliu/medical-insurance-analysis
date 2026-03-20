import csv 

# Columns as Dictionary
data = {
    "age": [],
    "sex": [],
    "bmi": [],
    "children": [],
    "smoker": [],
    "region": [],
    "charges": []
}

# Load the data into the dictionary  
with open('insurance.csv') as insurance_csv:
    reader = csv.DictReader(insurance_csv)
    for row in reader:
        data["age"].append(int(row["age"]))
        data["sex"].append(row["sex"])
        data["bmi"].append(float(row["bmi"]))
        data["children"].append(int(row["children"]))
        data["smoker"].append(row["smoker"])
        data["region"].append(row["region"])
        data["charges"].append(float(row["charges"]))

# Analysis 1: Average Calculator 
# Usable for age, bmi, children, charges
def calculate_average(column):
    total = 0
    for item in column:
        total += item
    average = total / len(column)
    return average

# Conduct Analysis 1
avg_age = round(calculate_average(data["age"]))
avg_bmi = round(calculate_average(data["bmi"]), 2)
avg_children = round(calculate_average(data["children"]))
avg_charges = round(calculate_average(data["charges"]), 2)
print("The average age of the people in this data set is {}, the average BMI is {}, the average number of " \
"children people have is {}, and the average charge is ${}.".format(avg_age, avg_bmi, avg_children, avg_charges))

# Analysis 2: Insurance Charge Comparison for Smoker/ Non-Smokers
def compare_smoking_charges():
    smoker_count = 0
    non_smoker_count = 0
    smoker_charge = 0
    non_smoker_charge = 0
    for i in range(len(data["smoker"])):
        if data["smoker"][i] == "yes":
            smoker_count += 1
            smoker_charge += data["charges"][i]
        else:
            non_smoker_count += 1
            non_smoker_charge += data["charges"][i]
    smoker_avg_charge = round((smoker_charge / smoker_count), 2) 
    non_smoker_avg_charge = round((non_smoker_charge / non_smoker_count), 2) 
    return "The average charge for a smoker is ${} and the average charge for a non-smoker is ${}.".format(smoker_avg_charge, non_smoker_avg_charge)

# Run Analysis 2
print(compare_smoking_charges())

# Analysis 3: Number of people in each region 
def region_count():
    region_dict = {}
    for i in range(len(data["region"])):
        current_region = data["region"][i]
        if current_region not in region_dict:
            region_dict[current_region] = 1
        else:
            region_dict[current_region] += 1
    return region_dict

# Run Analysis 3
print("Number of people in each region:\n" + str(region_count()))

# Analysis 4: Categorize BMI scores and returns a second dictionary with replaced values
# Underweight (<18.5), Healthy Weight (18.5–24.9), Overweight (25–29.9), and Obesity (30+)
data_bmi_update = {key: value[:] for key, value in data.items()}
def categorize_bmi(update):
    for i in range(len(update["bmi"])):
        if data["bmi"][i] < 18.5:
            update["bmi"][i] = "Underweight"
        elif data["bmi"][i] < 25:
            update["bmi"][i] = "Healthy"
        elif data["bmi"][i] < 30:
            update["bmi"][i] = "Overweight"
        else:
            update["bmi"][i] = "Obesity"
    return update

# Categorize and verify correctness with small sample
categorize_bmi(data_bmi_update)
print("Original Data Sample: " + str(data["bmi"][:10]))
print("Updated Data Sample: " + str(data_bmi_update["bmi"][:10]))

# Analysis 5: Compares charges in different age ranges; returns a dictionary of age ranges and average charge
# 18-30, 31-45, 46-60, 61+
def compare_age_charges():
    age_count = {
        "18-30": 0,
        "31-45": 0,
        "46-60": 0,
        "61+": 0
    }

    age_total = {
        "18-30": 0,
        "31-45": 0,
        "46-60": 0,
        "61+": 0
    }

    for i in range(len(data["age"])):
        current_age = data["age"][i]
        current_charge = data["charges"][i]
        if current_age < 31:
            age_count["18-30"] += 1
            age_total["18-30"] += current_charge
        elif current_age < 46:
            age_count["31-45"] += 1
            age_total["31-45"] += current_charge
        elif current_age < 61:
            age_count["46-60"] += 1
            age_total["46-60"] += current_charge
        else:
            age_count["61+"] += 1
            age_total["61+"] += current_charge

    avg_charge_age = {
        "18-30": 0,
        "31-45": 0,
        "46-60": 0,
        "61+": 0
    }

    for age_range in age_total:
        avg_charge_age[age_range] = round((age_total[age_range] / age_count[age_range]), 2) 
    
    return avg_charge_age

# Run Analysis 5
print("Comparison of charges by age range: " + str(compare_age_charges()))