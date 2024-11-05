# Task 1
## Define the class and initialize attributes.

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__updated_budget = allocated_budget

# Task 2
## Implement getters and setters. Ensure budget is positive.

    def get_category_name(self):
        return self.__category_name 

    def set_category_name(self, new_category):
        self.__category_name = new_category.lower()

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, anticipated_budget):
        if anticipated_budget >= 0:
            self.__allocated_budget = anticipated_budget
        else:
            print(f"{anticipated_budget} invalid. Budget must be positive.")

    def get_updated_budget(self):
        return self.__updated_budget

# Task 3
## Add Budget Functionality
    
    def track_expenses(self, amount):
        if 0 < amount <= self.__updated_budget:
            self.__updated_budget -= amount
            print(f"\n{amount} has been deducted from {self.__category_name}'s budget.")
        else:
            print("ERROR: Invalid expense amount or exceeds remaining budget.")


# Task 4
## Display Budget Details by category. Include the category name, allocated and remaining budgets.

    def display_category_details(self):
        print(f"\nCategory: {self.get_category_name()}")
        print(f"Original Budget: ${self.get_allocated_budget()}")
        print(f"Remaining Budget: ${self.get_updated_budget()}")










