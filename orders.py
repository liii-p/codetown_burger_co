import os

# TODO: change this file path before running. Please ensure you use forward slash / 
# DO NOT use backslash \
file = os.path.join(os.path.dirname(__file__), "orders.txt")


# defining order options
ENTRY1 = ["milk", "gluten free"]
ENTRY2 = ["tomato", "barbecue", "none"]
ENTRY3 = ["0", "1", "2", "3"]
ENTRY4 = ["0", "1", "2", "3"]
ENTRY5 = ["yes", "no"]
ENTRY6 = ["yes", "no"]
ENTRY7 = ["yes", "no"]


# defining error messages
LOWERCASE_ERROR = "All entries must be in lowercase. Please try again."
INCORRECT_ENTRY = "ERROR: Please ensure each line of orders.txt starts with the bun type (milk or gluten free), followed by a comma, then the sauce type (tomato, barbecue or none), followed by a comma, then the number of patties (0-3), followed by a comma, then the number of slices of cheese (0-3), followed by a comma, then whether tomato is included (yes or no), followed by a comma, then whether lettuce is included (yes or no), followed by a comma, then whether onion is included (yes or no).\n"

# defining extra costs for ingredients:
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


def convert_to_tuple(line):
   """
   Convert each line to a tuple, as long as each entry meets the requirements.
   """
   line = line.split(",")
   # Remove newline character \n before checking each entry
   line = list(map(lambda i:i.strip(), line))
   result = []
   try:
   # check if all elements are lowercase, if not return error and exit
      # if all values in the line are correct, convert to a tuple and return the tuple
      #for i in range(0, (len(line) - 1)):
         # First entry = "milk" or "gluten free",
      if line[0] in ENTRY1:
         result.append(line[0])
      else:
         raise ValueError
      # second entry = "tomato" or "barbecue" or "none"
      if line[1] in ENTRY2:
         result.append(line[1])
      else:
         raise ValueError
      # third entry = no. of patties (int)
      if line[2] in ENTRY3:
         if int(line[2]) > 3:
            raise ValueError
         elif int(line[2]) < 0:
            raise ValueError
         else:
            result.append(int(line[2]))
      else:
         raise ValueError
      if line[3] in ENTRY4:
         # fourth entry  = no. of cheese slices (int)
         if int(line[3]) > 3:
            raise ValueError
         elif int(line[3]) < 0:
            raise ValueError
         else:
            result.append(int(line[3]))
      else:
         raise ValueError
      if line[4] in ENTRY5:
         # fifth entry = True if tomato is included, else False
         if line[4] == "yes":
            result.append("True")
         else:
            result.append("False")
      else:
         raise ValueError
      if line[5] in ENTRY6:
         # sixth entry = True if lettuce is included, else False
         if line[5] == "yes":
            result.append("True")
         else:
            result.append("False")      
      else:
         raise ValueError
      if line[6] in ENTRY7:
         # seventh entry = True if onion is "yes", else False
         if line[6] == "yes":
            result.append("True")
         else:
            result.append("False")
      else:
         raise ValueError
   except (ValueError, TypeError):
      print(f"\n{INCORRECT_ENTRY}")
      return None
   return tuple(result)
      
# 1. Read from orders.txt
# 1.1 If an error occurs while reading the data, display error message and exit immediately
def read_file():
   """
   Read the file orders.txt line by and line and return a list of tuples containing the orders.
   """
   orders = []
   try:
      # open the file for reading
        with open(file) as file_in:
         for line in file_in:
            lines = convert_to_tuple(line)
            if lines == None:
               raise ValueError
            orders.append(lines)
            # read each line of the file and return it; .replace() is used to remove '\n' from the end of each line returned   
         return orders
   except (ValueError, PermissionError, FileExistsError, IsADirectoryError, FileNotFoundError):
       print("Error occurred while reading data from the file. Returning None. Please try again.")
       return None
 


# 3. Tuples ----> keys in dictionary which counts how frequently each burger order has occurred.
def count_burger_orders(line_tuple):
   """
   Takes in a tuple and counts the frequency of the burger orders then returns as a sorted dictionary.
   """
   freq = {}
   #line_dict = convert_to_dictionary(line_tuple, freq)
   for item in line_tuple:
      freq[item] = freq.get(item, 0) + 1
   # sort each key : value pair in the dictionary in reverse (descending) order
   result = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
   return result

def get_cost(line):
   """
   Get the cost of the burger order by iterating through each tuple entry and return the total cost for that order.
   """
   cost = BASE_BURGER_COST
   
   try:
      if line[0] == "gluten free":
         cost += GLUTEN_FREE_COST
      if line[2] > 1:
         cost += EXTRA_PATTY_COST * (line[2] - 1)
      if line[3] > 1:
         cost += EXTRA_CHEESE_COST * (line[3] - 1)
      if line[4] == "yes":
         cost += EXTRA_SALAD_COST
      if line[5] == "yes":
         cost += EXTRA_SALAD_COST
      if line[6] == "yes":
         cost += EXTRA_SALAD_COST
   except (TypeError, ValueError):
      print("Error occurred when counting cost.")
      return None
   return cost


def get_orders(orders_wanted):
   """
   Fetch the orders from read_file() and return the results with the tuple, frequency and cost in $
   """
   orders = read_file()
   # check to make sure read_file() has not returned None (indicating an error occurred)
   if orders == None:
      exit()
   result = count_burger_orders(orders)
   # to return the number of orders the user requests
   # will print as many results as in the dictionary called "result"
   for i, k in enumerate(result):
      if i == (orders_wanted):
         break
      print(f"{k}\t{result[k]}\t${get_cost(k)}")
      
# If there are less burger orders than user requests, display as many as possible
# 6.2 Cost of burger should be calculated by a function called get_cost(burger_order_tuple) and returns cost as integer.

def userprompt():
   """
      Prompt user for the number of top burger orders they wish to see
   """
   while True:
      try:
         user_answer = int(input("How many of the top burger orders would you like to see? "))
         if user_answer < 0:
            raise ValueError
      # If user enters a value which isn't a positive integer, prompt again
      except (ValueError, TypeError):
         print("Please enter a positive integer.")
         continue
      return user_answer


def main():
   """
   Main program to return the desired number of top burger orders
   """
   
   orders_wanted = userprompt()
   print(f"\nThe top burger orders were: ")
   get_orders(orders_wanted)


# Program entry point
if __name__ == "__main__":
    main()