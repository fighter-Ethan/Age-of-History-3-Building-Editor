import random
from guizero import App, Text, TextBox, PushButton, Combo, Box
import os

cwd = os.getcwd()

def save_file():
    try:
        building_json = {
            'Name': f'["{name_box.value}"]',
            'ImageID': f'[{imid_box.value}]',
            'GroupID': int(gid_box.value) if gid_box.value.isdigit() else gid_box.value,
            'CostGold': f'[{cost_box.value}]',
            'MaintenanceCost': f'[{maintenance_cost_box.value}]',
            'ConstructionTime': f'[{consttime_box.value}]',
            'TaxEfficiency': f'[{taxeff_box.value}]',
            'UniqueCapitalBuilding': unique_box.value.lower() == 'true',
            'RequiredTechID': f'[{techreq_box.value}]',
            'SeaAccessRequired': seaacc_box.value.lower() == 'true',
            'RecruitArmyCostInProvince': f'[{recruitcost_box.value}]',
            'MaximumManpower':  f'[{maxmanp_box.value}]',
            'ResearchPoints': f'[{researchpts_box.value}]',
            'MonthlyLegacy': f'[{monthlyleg_box.value}]',
            'MonthlyIncome': f'[{monthlyinc_box.value}]',
            'LocalGrowthRate': f'[{localgrow_box.value}]',
            'DiseaseDeathRate': f'[{diseasedeath_box.value}]',
            'DefenseBonus': f'[{defensebon_box.value}]',
            'IncreaseManpowerCost': f'[{increasemanpc_box.value}]',
            'Economy': f'[{econ_box.value}]',
            'AI': f'[{ai_box.value}]',
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
        formatted_json += '},'

        # Save the custom formatted string to a file
        with open(cwd + '\\CopyAndPasteToBuildingsJSON.json', 'w') as f:
            f.write(formatted_json)

        code_compiled.value = "Saved successfully! Check your folder for a file named 'CopyAndPasteToBuildingsJSON.json'."
    
    except Exception as e:
        code_compiled.value = f"Something went wrong: {e}"

# GUI setup
app = App(title="AoH3 Building Editor", width=800, height=650)

welcome_message = Text(app, text="Welcome to AoH3 - Building Editor!", size=30, font="Times New Roman", color="black")

param = Box(app, layout="grid", width="fill", align="top", border=True)

name = Text(param, text="Building Name", align="left",grid=[0,0])
name_box = TextBox(param, align="left",grid=[1,0])

imid = Text(param, text="Image ID", align="left",grid=[0,1])
imid_box = TextBox(param, align="left",grid=[1,1])

gid = Text(param, text="Group ID",align="left",grid=[0,2])
gid_box = TextBox(param,align="left",grid=[1,2])

cost = Text(param, text="Cost to Build (Gold)",align="left",grid=[0,3])
cost_box = TextBox(param,align="left",grid=[1,3])

maintenance_cost = Text(param, text="Maintenance Cost",align="left",grid=[0,4])
maintenance_cost_box = TextBox(param,align="left",grid=[1,4])

consttime = Text(param, text="Construction Time",align="left",grid=[0,5])
consttime_box = TextBox(param,align="left",grid=[1,5])

taxeff = Text(param, text="Tax Efficiency",align="left",grid=[0,6])
taxeff_box = TextBox(param,grid=[1,6])

techreq = Text(param, text="ID of Tech Needed to Build",align="left",grid=[0,7])
techreq_box = TextBox(param,align="left",grid=[1,7])

ai = Text(param, text="AI",align="left",grid=[0,8])
ai_box = TextBox(param,align="left",grid=[1,8])

recruitcost = Text(param, text="Cost to Recruit Army",align="left",grid=[0,9])
recruitcost_box = TextBox(param,align="left",grid=[1,9])

maxmanp = Text(param, text="Maximum Manpower",align="left",grid=[0,10])
maxmanp_box = TextBox(param,align="left",grid=[1,10])

researchpts = Text(param, text="Research Points",align="left",grid=[0,11])
researchpts_box = TextBox(param,align="left",grid=[1,11])

monthlyleg = Text(param, text="Monthly Legacy",align="left",grid=[0,12])
monthlyleg_box = TextBox(param,align="left",grid=[1,12])

monthlyinc = Text(param, text="Monthly Income",align="left",grid=[0,13])
monthlyinc_box = TextBox(param,align="left",grid=[1,13])

localgrow = Text(param, text="Local Growth Rate", align="left",grid=[0,14])
localgrow_box = TextBox(param, align="left", grid=[1,14])

diseasedeath = Text(param, text="Disease Death Rate",align="left",grid=[0,15])
diseasedeath_box = TextBox(param, align="left", grid=[1,15])

defensebon = Text(param, text="Defense Bonus",align="left",grid=[0,16])
defensebon_box = TextBox(param, align="left", grid=[1,16])

increasemanpc = Text(param, text="Increase Manpower Cost",align="left", grid=[0,17])
increasemanpc_box = TextBox(param, align="left", grid=[1,17])

econ = Text(param, text="Economy Change",align="left", grid=[0,18])
econ_box = TextBox(param, align="left", grid=[1,18])

unique = Text(param, text="Unique to Capital?",align="left", grid=[0,19])
unique_box = Combo(param, options=['true', 'false'],align="left", grid=[1,19])

seaacc = Text(param, text="Is Sea Access Required?",align="left",grid=[0,20])
seaacc_box = Combo(param, options=['true', 'false'],align="left",grid=[1,20])

compile_button = PushButton(app, command=save_file, text="Compile My Code!")
code_compiled = Text(app, text="", size=15, font="Times New Roman", color="black")

app.display()
