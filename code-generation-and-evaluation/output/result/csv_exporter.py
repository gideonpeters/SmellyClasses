import pandas as pd
import json

# Open the file
with open('detailed_result.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)


# Transform the JSON structure
desired_json = []
for test_version, tasks in data.items():
    for task, classes in tasks.items():
        for classname, results in classes.items():
            new_dict = {}
            if 'EachTestResult' in results:
                new_dict.update({
                    "task": task, 
                    # "test_version": test_version, 
                    "classname": classname, 
                    'EachTestResult': results['EachTestResult'], 
                    'error': results['error'], 
                    'fail': results['fail'], 
                    'partial_success': results['partial_success'], 
                    'success': results['success']
                })
                
            desired_json.append(new_dict)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(desired_json)

# Remove the rows with all missing data
df = df.dropna(how='all')

# Remove the column headers
df = df.T.reset_index(drop=True).T

# Convert the DataFrame to a CSV file
df.to_csv('detailed_result_csv.csv', index=False, header=False)