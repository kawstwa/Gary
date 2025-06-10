operations = {'customer': ['customer_option_1', 'customer_option_2', 'customer_option_3'],
              'project': ['project_option_1', 'project_option_2', 'project_option_3'],
              'item': ["item_option_1", "item_option_2", "item_option_3"],
              'work_center': ['work_center_option_1', 'work_center_option_2','work_center_option_3'],
               'purchase': ['purchase_option_1', 'purchase_option_2', 'purchase_option_4'],
               'do_work': ["do_work_option_1", "do_work_option_2", "do_work_option_3"],
               'spare1': ['spare1_option_1', 'spare1_option_2', 'spare1_option_3'],
               'spare2': ['spare2_option_1', 'spare2_option_2', 'spare2_option_3'],
               'spare3': ['spare3_option_1', 'spare3_option_2', 'spare3_option_3'],
              'admin': ['admin_option_1', 'admin_option_2', 'admin_option_3']}

string = ''

for key, value in operations.items():
    string += f"def {key}_func():\n"
    string += f"    clear_layout()\n"
    string += f"    widget.setFixedHeight({len(value)*90})\n"
    for item in value:
        string += f"    {item}Button = CreateButton('{item}')\n"
        string += f"    layout.addWidget({item}Button)\n"
    string += "    returnButton = CreateButton('Return')\n"
    string += "    returnButton.clicked.connect(mainMenu)\n"
    string += "    layout.addWidget(returnButton)\n"

string += "def mainMenu():\n"
string += f"    clear_layout()\n"
string += "    widget.setFixedHeight(650)\n"
for i, (key, value) in enumerate(operations.items()):
    string += f"    {key}Button = CreateButton('{i+1}. {key.title()}')\n"
    # string += f"    {key}Button.setFocusPolicy(Qt.StrongFocus)\n"
    string += f"    {key}Button.clicked.connect({key}_func)\n"
    string += f"    layout.addWidget({key}Button)\n"
string += "    adminButton.setText('0. Admin')\n"
string += "mainMenu()\n"
    
print(string)

