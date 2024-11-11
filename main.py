import random
from guizero import App, Text, TextBox, PushButton, Combo
import os

cwd = os.getcwd()

def save_file():
    try:
        building_json = {
            'Name': f'["{name_box.value}"]',  # String values in brackets
            'ImageID': f'[{imid_box.value}]',  # Numeric values in brackets
            'GroupID': int(gid_box.value) if gid_box.value.isdigit() else gid_box.value,  # Keep numeric values as integers
            'CostGold': f'[{cost_box.value}]',  # Numeric values in brackets
            'MaintenanceCost': f'[{maintenance_cost_box.value}]',  # Numeric values in brackets
            'ConstructionTime': f'[{consttime_box.value}]',  # Numeric values in brackets
            'TaxEfficiency': f'[{taxeff_box.value}]',  # Numeric values in brackets
            'UniqueCapitalBuilding': unique_box.value.lower() == 'true',  # Boolean without quotes or brackets
            'RequiredTechID': f'[{techreq_box.value}]',  # Numeric values in brackets
            'SeaAccessRequired': seaacc_box.value.lower() == 'true',  # Boolean without quotes or brackets
            'AI': f'[{ai_box.value}]',  # Numeric values in brackets
        }

        # Manually format the JSON-like string
        formatted_json = "{\n"
        
        for key, value in building_json.items():
            if isinstance(value, str):  # For strings, keep them wrapped in brackets
                formatted_json += f'    {key}: {value},\n'
            else:  # For numeric or boolean values, do not wrap in brackets
                formatted_json += f'    {key}: {value},\n'

        # Remove the last comma and newline, and close the curly brace
        formatted_json = formatted_json.rstrip(',\n') + '\n'
        formatted_json += '}'

        # Save the custom formatted string to a file
        os.remove("CopyAndPasteToBuildingsJSON.json")
        with open(cwd + '\\CopyAndPasteToBuildingsJSON.json', 'w') as f:
            f.write(formatted_json)

        code_compiled.value = "Saved successfully! Check your folder for a file named 'CopyAndPasteToBuildingsJSON.json'."
    
    except Exception as e:
        code_compiled.value = f"Something went wrong: {e}"

# GUI setup
app = App(title="AoH3 Building Editor", width=800, height=650)
welcome_message = Text(app, text="Welcome to AoH3 - Building Editor!", size=30, font="Times New Roman", color="black")

name = Text(app, text="Building Name", align="center")
name_box = TextBox(app, align="center")

imid = Text(app, text="Image ID")
imid_box = TextBox(app)

gid = Text(app, text="Group ID")
gid_box = TextBox(app)

cost = Text(app, text="Cost to Build (Gold)")
cost_box = TextBox(app)

maintenance_cost = Text(app, text="Maintenance Cost")
maintenance_cost_box = TextBox(app)

consttime = Text(app, text="Construction Time")
consttime_box = TextBox(app)

taxeff = Text(app, text="Tax Efficiency")
taxeff_box = TextBox(app)

techreq = Text(app, text="ID of Tech Needed to Build")
techreq_box = TextBox(app)

ai = Text(app, text="AI")
ai_box = TextBox(app)

unique = Text(app, text="Unique to Capital?")
unique_box = Combo(app, options=['true', 'false'])

seaacc = Text(app, text="Is Sea Access Required?")
seaacc_box = Combo(app, options=['true', 'false'])

compile_button = PushButton(app, command=save_file, text="Compile My Code!")
code_compiled = Text(app, text="", size=15, font="Times New Roman", color="black")

app.display()
