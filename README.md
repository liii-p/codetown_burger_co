# Codetown Burger Co's ordering stuff

## About burger.py
This is a program created for Codetown Burger Co to take customers' burger orders.
Created as part of COSC110 at University of New England (UNE).  

### Options
- Bun (milk/gluten free)
- Sauce (tomato/barbecue/none)
- Patties (0-3)
- Cheese (0-3)
- Tomato
- Lettuce
- Onion

Base cost (milk, sauce, 1 patty, 1 slice of cheese, 1 salad item) = $5

### Running the program
You can run this program by executing this command:

```bash
python3 burger.py
```


## About orders.py
<p>This program has been designed for Codetown Burger Co. It reads a file of burger orders and counts the frequency and cost of each order, then restructures the orders based on the frequency. As a user, you can now enter how many of the top orders you wish to see and the program will display them for you.</p>

</br>

### How To Run
<p>To ensure the program can work as expected, please make sure your <em>orders.txt</em> file is in the <b>same directory/folder</b> as <em>orders.py</em>.</p>
<p>To start the program, open a bash terminal and simply enter:</p>

```bash
python3 orders.py
 ```

</br>

### Example Interaction
<h3>Example 1</h3>
<p>With the following contents in <em>orders.txt</em>:</p>

```
gluten free,tomato,2,1,yes,no,no
milk,barbecue,3,3,yes,yes,yes
gluten free,barbecue,2,1,no,yes,no
gluten free,barbecue,3,3,yes,yes,yes
gluten free,barbecue,1,0,no,yes,no
milk,barbecue,3,3,yes,yes,yes
milk,barbecue,3,3,yes,yes,yes
gluten free,tomato,2,1,yes,no,no
```

<p> Output:</p>

``` 
How many of the top burger orders would you like to see? 3

The top burger orders were:
('milk', 'barbecue', 3, 3, 'True', 'True', 'True')      3       $13
('gluten free', 'tomato', 2, 1, 'True', 'False', 'False')       2       $9
('gluten free', 'barbecue', 2, 1, 'False', 'True', 'False')     1       $9
```

<h3>Example 2</h3>
<p>If an <b>invalid</b> value is in the <em>orders.txt</em> file:</p>

```
gluten free,tomato,2,1,HELLO,no,no
milk,barbecue,3,3,yes,yes,yes
gluten free,barbecue,2,1,no,yes,no
gluten free,barbecue,3,3,yes,yes,yes
gluten free,barbecue,1,0,no,yes,no
milk,barbecue,3,3,yes,yes,yes
milk,barbecue,3,3,yes,yes,yes
gluten free,tomato,2,1,yes,no,no
```

<p>Output:</p>

```
How many of the top burger orders would you like to see? 3
The top burger orders were:

ERROR: Please ensure each line of orders.txt starts with the bun type (milk or gluten free), followed by a comma, then the sauce type (tomato, barbecue or none), followed by a comma, then the number of patties (0-3), followed by a comma, then the number of slices of cheese (0-3), followed by a comma, then whether tomato is included (yes or no), followed by a comma, then whether lettuce is included (yes or no), followed by a comma, then whether onion is included (yes or no).        

Error occurred while reading data from the file. Returning None. Please try again.
```

</br>

## About menu.py
### Codetown Burger Co's New Burger Menu
To assist in the launch of Codetown Burger Co's new burger options, this burger menu has been created to provide an accessible way for customers to view these new options.

The new burger options are:

Byte Burger, Ctrl Alt Delicious, Data Crunch, Code Cruncher

### How to Use
Type the following command into your local bash terminal to run the program:
```bash
python3 menu.py
```

Once running, you can choose to let the program cycle through the menu automatically or click on one of the buttons to choose the burger menu you wish to see. 

The menu will display the burger name, bun type, sauce type, number of patties, number of cheese slices, tomato, lettuce, onion and finally the total price of the burger.

When you are done, simply click the "X" (or the equivalent for your device) to close the program.


### Author
Lianna Pyman, 2024