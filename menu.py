from tkinter import *
from tkinter import ttk

# root
root = Tk()
root.title("Welcome to Codetown Burger Co")
# Set height and width of root to 500
root.config(height=500, width=500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# frame
frame = ttk.Frame(root, padding="12 12")
frame.grid(column=0, row=0, sticky=(N, S, E, W), columnspan=3, rowspan=3)
# Make sure the frame, with all the widgets, remains in the centre of the window even when maximised.
# relx and rely give a position relative to the window.
frame.place(relx=0.5, rely=0.5, anchor='center')

# BURGER COST
# The base cost of a burger
BASE_BURGER_COST = 5

# The extra charge for a gluten free burger
GLUTEN_FREE_COST = 1

# The extra charge for an extra patty
EXTRA_PATTY_COST = 3

# The extra charge for an extra slice of cheese
EXTRA_CHEESE_COST = 1

# The extra charge for an extra salad item
EXTRA_SALAD_COST = 1

# defining functions

def calculate_cost(burger_order):
    salad_count = 0
    burger_cost = BASE_BURGER_COST
    if burger_order[0] == "gluten free" :
        burger_cost += GLUTEN_FREE_COST
    if burger_order[2] > 1:
        burger_cost += EXTRA_PATTY_COST * (burger_order[2] - 1)
    if burger_order[3] > 1:
        burger_cost += EXTRA_CHEESE_COST * (burger_order[3] - 1)
    if burger_order[4] == "Yes":
        salad_count += 1
    if burger_order[5] == "Yes":
        salad_count += 1
    if burger_order[6] == "Yes":
        salad_count += 1
    if salad_count > 1:
       burger_cost += EXTRA_SALAD_COST * (salad_count - 1)

    return burger_cost

# burger orders
byte_burger = ["Milk bun", "Tomato", 1, 0, "No", "Yes", "No"]
ctrl_alt_delicious = ["Milk bun", "Barbecue", 2, 2, "Yes", "Yes", "Yes"]
data_crunch = ["Gluten free", "Tomato", 0, 0, "Yes", "Yes", "Yes"]
code_cruncher = ["Milk bun", "Tomato", 3, 3, "Yes", "Yes", "Yes"]

# defining labels
burger_name = StringVar()
bun = StringVar()
sauce = StringVar()
patties = IntVar()
cheese = IntVar()
tomato = StringVar()
lettuce = StringVar()
onion = StringVar()
price = StringVar()


# modify above StringVars with byte_burger list
def byte_burger_menu():
  burger_name.set("Byte Burger")
  bun.set(byte_burger[0])
  sauce.set(byte_burger[1])
  patties.set(byte_burger[2])
  cheese.set(byte_burger[3])
  tomato.set(byte_burger[4])
  lettuce.set(byte_burger[5])
  onion.set(byte_burger[6])
  price.set(f"${calculate_cost(byte_burger)}")

# modify above StringVars with ctrl_alt_delicious list
def ctrl_alt_delicious_menu():
  burger_name.set("Ctrl Alt Delicious")
  bun.set(ctrl_alt_delicious[0])
  sauce.set(ctrl_alt_delicious[1])
  patties.set(ctrl_alt_delicious[2])
  cheese.set(ctrl_alt_delicious[3])
  tomato.set(ctrl_alt_delicious[4])
  lettuce.set(ctrl_alt_delicious[5])
  onion.set(ctrl_alt_delicious[6])
  price.set(f"${calculate_cost(ctrl_alt_delicious)}")

# modify above StringVars with data_crunch list
def data_crunch_menu():
  burger_name.set("Data Crunch")
  bun.set(data_crunch[0])
  sauce.set(data_crunch[1])
  patties.set(data_crunch[2])
  cheese.set(data_crunch[3])
  tomato.set(data_crunch[4])
  lettuce.set(data_crunch[5])
  onion.set(data_crunch[6])
  price.set(f"${calculate_cost(data_crunch)}")

# modify above StringVars with code_cruncher list
def code_cruncher_menu():
  burger_name.set("Code Cruncher")
  bun.set(code_cruncher[0])
  sauce.set(code_cruncher[1])
  patties.set(code_cruncher[2])
  cheese.set(code_cruncher[3])
  tomato.set(code_cruncher[4])
  lettuce.set(code_cruncher[5])
  onion.set(code_cruncher[6])
  price.set(f"${calculate_cost(code_cruncher)}")

# displaying default burger menu - byte burger
default = byte_burger_menu()

name_label = ttk.Label(frame, text="Burger name: ")
name_label.grid(column=4, row=0, sticky=SE)

name_output = ttk.Label(frame, textvariable=burger_name)
name_output.grid(column=6, row=0, sticky=(W, E))

# displaying bun type
bun_label = ttk.Label(frame, text="Bun type:")
bun_label.grid(column=4, row=2, sticky=(W,E))

bun_output = ttk.Label(frame, textvariable=bun)
bun_output.grid(column=6, row=2, sticky=(W,E))

# displaying sauce type
sauce_label = ttk.Label(frame, text="Sauce type:")
sauce_label.grid(column=4, row=4, sticky=(W,E))

sauce_output = ttk.Label(frame, textvariable=sauce)
sauce_output.grid(column=6, row=4, sticky=(W,E))

# displaying patties
patties_label = ttk.Label(frame, text="Patties:")
patties_label.grid(column=4, row=6, sticky=(W,E))

patties_output = ttk.Label(frame, textvariable=patties)
patties_output.grid(column=6, row=6, sticky=(W,E))

# displaying cheese 
cheese_label = ttk.Label(frame, text="Cheese:")
cheese_label.grid(column=4, row=8, sticky=(W,E))

cheese_output = ttk.Label(frame, textvariable=cheese)
cheese_output.grid(column=6, row=8, sticky=(W,E))

# displaying tomato
tomato_label = ttk.Label(frame, text="Tomato:")
tomato_label.grid(column=4, row=10, sticky=(W,E))

tomato_output = ttk.Label(frame, textvariable=tomato)
tomato_output.grid(column=6, row=10, sticky=(W,E))

# displaying lettuce
lettuce_label = ttk.Label(frame, text="Lettuce:")
lettuce_label.grid(column=4, row=12, sticky=(W,E))

lettuce_output = ttk.Label(frame, textvariable=lettuce)
lettuce_output.grid(column=6, row=12, sticky=(W,E))

# displaying onion
onion_label = ttk.Label(frame, text="Onion:")
onion_label.grid(column=4, row=14, sticky=(W,E))

onion_output = ttk.Label(frame, textvariable=onion)
onion_output.grid(column=6, row=14, sticky=(W,E))

# displaying price
price_label = ttk.Label(frame, text="Price:")
price_label.grid(column=4, row=16, sticky=(W,E))

price_output = ttk.Label(frame, textvariable=price)
price_output.grid(column=6, row=16, sticky=(W,E))

# BURGER BUTTONS
""" When a burger button is clicked, the associated burger menu is displayed and a button_clicked function is triggered, 
telling the program that a button has been clicked. """
# byte burger 
bb_button = ttk.Button(frame, text="Byte Burger", command=lambda: [byte_burger_menu(), button_clicked()])
bb_button.grid(column=0, row=18, sticky=(W, E), columnspan=3)

# ctrl alt delicious
cad_button = ttk.Button(frame, text="Ctrl Alt Delicious", command=lambda: [ctrl_alt_delicious_menu(), button_clicked()])
cad_button.grid(column=3, row=18, sticky=(W, E), columnspan=3)

# data crunch
dc_button = ttk.Button(frame, text="Data Crunch", command=lambda: [data_crunch_menu(), button_clicked()])
dc_button.grid(column=6, row=18, sticky=(W, E), columnspan=3)

# code cruncher
cc_button = ttk.Button(frame, text="Code Cruncher", command=lambda: [code_cruncher_menu(), button_clicked()])
cc_button.grid(column=9, row=18, sticky=(W, E), columnspan=3)

for child in frame.winfo_children():
    child.grid_configure(padx=0, pady=10)

buttonClicked = False

# To detect if button has been clicked or not
def button_clicked():
   buttonClicked = True

def reset_button_clicked():
   buttonClicked = False


def cycle_menu():
    if buttonClicked == False:
        root.after(5000, ctrl_alt_delicious_menu)
        root.after(10000, data_crunch_menu)
        root.after(15000, code_cruncher_menu)
        root.after(20000, byte_burger_menu)
        root.after(20000, cycle_menu)
    elif buttonClicked == True:
        root.after(5000, reset_button_clicked)
        root.after(5000, cycle_menu)

root.after(0, cycle_menu)
while True:
    root.mainloop()