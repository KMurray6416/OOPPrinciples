
from personal_budget_app import BudgetCategory

food_category = BudgetCategory("Food", 500)
food_category.track_expenses(100)
food_category.display_category_details()

utilities_category = BudgetCategory("Utilities", 450)
utilities_category.track_expenses(375)
utilities_category.display_category_details()

entertainment_category = BudgetCategory("Entertainment", 775)
entertainment_category.track_expenses(500)
entertainment_category.display_category_details()