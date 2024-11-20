import random
#tkinter is required for proper usage of icons
import tkinter
from tkinter import colorchooser
#guizero is required for the app to show / work
from guizero import App, MenuBar, Window, Text, TextBox, PushButton, Combo, Box, CheckBox
#Required for proper window / icon functioning
import os
import sys
#Enables Copy/Paste Functionality
import pyperclip

global mode_l
global mode_d
global mode_c
mode_1 = True
mode_d = False
mode_c = False

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
            'ProductionEfficiency': f'[{prodeff_box.value}]',
            'InvestInEconomyCost': f'[{invecon_box.value}]',
            'DevelopInfrastructureCost': f'[{invinf_box.value}]',
            'IncreaseGrowthRateCost': f'[{incgrco_box.value}]',
	    'LocalTaxEfficiency': f'[{loctaxeff_box.value}]',
	    'MaxInfrastructure': f'[{maxinf_box.value}]',
	    'ArmyMovementSpeed': f'[{armmovspd_box.value}]',
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

        pastebox_box.clear()
        pastebox_box.value = formatted_json
    
    except Exception as e:
        code_compiled.value = f"Something went wrong: {e}"

# GUI setup
app = App(title="AoH3 Building Editor", width=800, height=650)
root = app.tk
def get_resource_path(filename):
    #Get the absolute path to the resource, handling PyInstaller.
    if hasattr(sys, '_MEIPASS'):  # Check if running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.getcwd(), filename)


def lightmode():
    global mode_l, mode_d, mode_c
    mode_l = True
    mode_d = False
    mode_c = False
    if mode_l == True:
        app.bg = "white"
        app.text_color = "black"
    elif mode_l == False:
        return

def darkmode():
    global mode_l, mode_d, mode_c
    mode_d = True
    mode_l = False
    mode_c = False
    if mode_d == True:
        app.bg = "black"
        app.text_color = "white"
    elif mode_d == False:
        return

    
def customtheme():
    global mode_l, mode_d, mode_c, var_color_choice_bg, var_color_choice_txt
    global customtheme_window
    customtheme_window = Window(app,title="AoH3BE - Set Custom Theme")
    customtheme_window.focus()
    preview_custom_box = Box(customtheme_window, align="top")
    global preview_custom
    preview_custom = Text(preview_custom_box, text = "This is a Preview", align="top")
    background_custom = PushButton(customtheme_window, command=color_choice_bg, text="Choose Background Color")
    text_custom = PushButton(customtheme_window, command=color_choice_txt, text="Choose Text Color")
    cancel_custom = PushButton(customtheme_window, command=cancelcustomcolor, text="Cancel",align="bottom")
    confirm_custom = PushButton(customtheme_window, command=confirmcustomcolor, text="Confirm", align="bottom")
    if mode_l == True:
        customtheme_window.bg = "white"
        customtheme_window.text_color = "black"
    elif mode_d == True:
        customtheme_window.bg = "black"
        customtheme_window.text_color = "white"
    elif mode_c == True:
        customtheme_window.bg = var_color_choice_bg
        customtheme_window.text_color = var_color_choice_txt

def color_choice_bg():
    global var_color_choice_bg
    var_color_choice_bg = colorchooser.askcolor(title = "Choose a Background Color")[1]
    preview_custom.bg = var_color_choice_bg
    customtheme_window.focus()

def color_choice_txt():
    global var_color_choice_txt
    var_color_choice_txt = colorchooser.askcolor(title = "Choose a Text Color")[1]
    preview_custom.text_color = var_color_choice_txt
    customtheme_window.focus()

def confirmcustomcolor():
    global mode_l, mode_d, mode_c, var_color_choice_bg, var_color_choice_txt
    mode_c = True
    mode_l = False
    mode_d = False
    app.bg = var_color_choice_bg
    app.text_color = var_color_choice_txt
    customtheme_window.destroy()
     
def cancelcustomcolor():
    customtheme_window.destroy()
     
# Get the correct path to the icon
icon_path = get_resource_path("aoh3.ico")

try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Error setting the icon: {e}")

#Sets default BG
app.bg = "white"
app.text_color = "black"

#Widgets
welcome_message = Text(app, text="AoH3 - Building Editor", size=30, font="Times New Roman", color="black")
param = Box(app, layout="grid", width="fill", height="fill", align="left", border=False)
param2 = Box(app, layout="grid", width="fill", height="fill", align="left", border=False)
compile = Box(app, align="bottom")
copytext = Box(app, align="bottom")
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
prodeff = Text(param2, text="Production Efficiency",align="right", grid=[0,0])
prodeff_box = TextBox(param2, align="right", grid=[1,0])
invecon = Text(param2, text="Cost to Invest In Economy",align="right", grid=[0,1])
invecon_box = TextBox(param2, align="right", grid=[1,1])
invinf = Text(param2, text="Cost to Invest In Infrastructure",align="right", grid=[0,2])
invinf_box = TextBox(param2, align="right", grid=[1,2])
incgrco = Text(param2, text="Cost to Grow Income",align="right", grid=[0,3])
incgrco_box = TextBox(param2, align="right", grid=[1,3])
loctaxeff = Text(param2, text="Local Tax Efficiency",align="right", grid=[0,4])
loctaxeff_box = TextBox(param2, align="right", grid=[1,4])
maxinf = Text(param2, text="Maximum Infrastructure", align="right", grid=[0,5])
maxinf_box = TextBox(param2, align="right", grid=[1,5])
armmovspd = Text(param2, text="Army Movement Speed", align="right", grid=[0,6])
armmovspd_box = TextBox(param2, align="right", grid=[1,6])
unique = Text(param2, text="Unique to Capital?",align="right", grid=[0,7])
unique_box = Combo(param2, options=['true', 'false'],align="right", grid=[1,7])
seaacc = Text(param2, text="Is Sea Access Required?",align="right",grid=[0,8])
seaacc_box = Combo(param2, options=['true', 'false'],align="right",grid=[1,8])
pastebox = Box(app, width="fill", height="fill",border=True, align="right")
pastebox_box = TextBox(pastebox, width = "fill", height = "fill", multiline = True, scrollbar = True)

#Set the Theme
menubar = MenuBar(app,
                  toplevel=["Theme"],
                  options=[
                      [["Light Mode (Default)", lightmode], ["Dark Mode (Recommended)", darkmode], ["Custom Theme", customtheme]]
                      ])


#To handle accidental quitting of the app
def close_check():
    if app.yesno("Close", "Do you REALLY want to quit? All your progress will be lost."):
        app.destroy()

app.when_closed = close_check

#Copies Text to Clipboard when called
def copy_code_text():
    pyperclip.copy(pastebox_box.value)
    copy_text.text = "Code Copied!"
    copy_text.after(2000,revertcode_text)
    
def revertcode_text():
    copy_text.text = "Copy Code"
    
#Buttons that actually do things
compile_button = PushButton(compile, command=save_file, text="Compile My Code!")
code_compiled = Text(compile, text="", size=15, font="Times New Roman", color="black")

copy_text = PushButton(copytext, command=copy_code_text, text="Copy Code")



app.display()
