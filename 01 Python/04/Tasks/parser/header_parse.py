import csv
import openpyxl


with open('header.h', 'r') as file:
    file.seek(0)
    file_lines = file.readlines()
    
prototypes = []

i = -1
for ID, prototype in enumerate(file_lines, start = 1):
    prototype = prototype.rstrip('\n')

    
    prototype_dict = {
        'Function Prototype': prototype,
        'Unique ID': f"IDX{ID:03}"
    }

    prototypes.append(prototype_dict)



with open("prototypes.csv", 'w', newline = '\n') as file:
    writer = csv.writer(file, delimiter= ';')
    writer.writerow(prototypes[0].keys())

    for dic in prototypes:
        value = dic.values()
        writer.writerow(value)




workbook = openpyxl.Workbook()

new_sheet = workbook.create_sheet(title ='newSheet')

# remove the default sheet
default_sheet = workbook['Sheet']
workbook.remove(default_sheet)

# Write the header row
header = prototypes[0].keys()
new_sheet.append(list(header))

# Write data rows
for dic in prototypes:
    value = dic.values()
    new_sheet.append(list(value))

# Save the workbook
workbook.save('prototypes.xlsx')