from functools import reduce

class Pants:
    
    """This class makes a pair of pants each time
    """
    
    def __init__(self, color, waist_size, length, price):
        
        """
        Arguments:
        
            color (str):
            waist_size (str):
            length (int):
            price (float): In LCY        
        """
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
        
    def change_price(self, new_price):
        """Return nothing
        
        Arguments:
        
            new_price (float): How much?
        
        Returns:
            float: New price
        """
        self.price = new_price
        return self.price
    
    def discount(self, discount):
        """Make things cheaper
        """
        return self.price * (1 - discount)



"""A Sales Person. They don't take much salary but they have huge commission, no shit.
"""
class SalesPerson:
    
    def __init__(self, first_name, last_name, employee_id, salary):
        
        """Make a person
        
        Arguments:
        
        Attributes:

            first_name (string): the first name of the salesperson
            last_name (string): the last name of the salesperson
            employee_id (int): the employee ID number like 5681923
            salary (float): the monthly salary of the employee
            pants_sold (list of Pants objects): pants that the salesperson has sold 
            total_sales (float): sum of sales of pants sold

        
        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0
        
    def sell_pants(self, pants):
        
        """Make money
        
        Arguments:
            pants (Pants):
        
        Returns:
            None
        """
        self.pants_sold.append(pants)

    def display_sales(self):

        """Report!

        Arguments: None
        Returns:
            None
        """
        print(''.join(map(
            lambda x: f"color: {x.color}, waist_size: {x.waist_size}, length: {x.length}, price: {x.price}\n", self.pants_sold
        )))

    
    
    def calculate_sales(self):
        """Calculate the performance.
        
        Arguments:
            None
            
        Returns:
            float: total_sales

        """
        self.total_sales = reduce(lambda x, y: x + y.price, self.pants_sold, 0)
        return self.total_sales
    
    def calculate_commission(self, percentage):
        """Calculate total commission based on sales.
        
        Arguments:
            percentage (float): commission rate
            
        Returns:
            float: Total comission
        """
        return self.calculate_sales() * percentage

def check_pants_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')


def check_sales_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
# check_results()
