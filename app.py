import tkinter as tk


class AggregatePlanningChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize chatbot with default values
        self.chatbot = AggregatePlanningChatbot()

        # Create and set up GUI elements
        self.title("Aggregate Planning Chatbot")

        self.label_demand = tk.Label(self, text="Forecasted Demand:")
        self.entry_demand = tk.Entry(self)

        self.label_capacity = tk.Label(self, text="Production Capacity:")
        self.entry_capacity = tk.Entry(self)

        self.label_inventory = tk.Label(self, text="Inventory Levels:")
        self.entry_inventory = tk.Entry(self)

        self.label_subcontracting = tk.Label(
            self, text="Subcontracting Capacity:")
        self.entry_subcontracting = tk.Entry(self)

        self.label_workforce = tk.Label(self, text="Workforce Size:")
        self.entry_workforce = tk.Entry(self)

        self.label_part_time = tk.Label(self, text="Part-time Workers:")
        self.entry_part_time = tk.Entry(self)

        self.button_submit = tk.Button(
            self, text="Submit", command=self.get_user_input)

        # Pack elements into the layout
        self.label_demand.pack()
        self.entry_demand.pack()

        self.label_capacity.pack()
        self.entry_capacity.pack()

        self.label_inventory.pack()
        self.entry_inventory.pack()

        self.label_subcontracting.pack()
        self.entry_subcontracting.pack()

        self.label_workforce.pack()
        self.entry_workforce.pack()

        self.label_part_time.pack()
        self.entry_part_time.pack()

        self.button_submit.pack()

    def get_user_input(self):
        # Retrieve user input from the GUI
        self.chatbot.forecasted_demand = int(self.entry_demand.get())
        self.chatbot.capacity = int(self.entry_capacity.get())
        self.chatbot.inventory_levels = int(self.entry_inventory.get())
        self.chatbot.subcontracting = int(self.entry_subcontracting.get())
        self.chatbot.workforce_size = int(self.entry_workforce.get())
        self.chatbot.part_time_workers = int(self.entry_part_time.get())

        # Execute the main workflow
        self.chatbot.make_aggregate_plan()
        self.chatbot.provide_alternative_decisions()


class AggregatePlanningChatbot:
    def __init__(self):
        # Initialize chatbot with default values
        self.forecasted_demand = 0
        self.capacity = 0
        self.inventory_levels = 0
        self.subcontracting = 0
        self.workforce_size = 0
        self.part_time_workers = 0

        # Create and set up GUI elements
        self.title("Aggregate Planning Chatbot")

        self.label_demand = tk.Label(self, text="Forecasted Demand:")
        self.entry_demand = tk.Entry(self)

        self.label_capacity = tk.Label(self, text="Production Capacity:")
        self.entry_capacity = tk.Entry(self)

        self.label_inventory = tk.Label(self, text="Inventory Levels:")
        self.entry_inventory = tk.Entry(self)

        self.label_subcontracting = tk.Label(
            self, text="Subcontracting Capacity:")
        self.entry_subcontracting = tk.Entry(self)

        self.label_workforce = tk.Label(self, text="Workforce Size:")
        self.entry_workforce = tk.Entry(self)

        self.label_part_time = tk.Label(self, text="Part-time Workers:")
        self.entry_part_time = tk.Entry(self)

        self.button_submit = tk.Button(
            self, text="Submit", command=self.get_user_input)

        # Pack elements into the layout
        self.label_demand.pack()
        self.entry_demand.pack()

        self.label_capacity.pack()
        self.entry_capacity.pack()

        self.label_inventory.pack()
        self.entry_inventory.pack()

        self.label_subcontracting.pack()
        self.entry_subcontracting.pack()

        self.label_workforce.pack()
        self.entry_workforce.pack()

        self.label_part_time.pack()
        self.entry_part_time.pack()

        self.button_submit.pack()

    def get_user_input(self):
        # Retrieve user input from the GUI
        self.chatbot.forecasted_demand = int(self.entry_demand.get())
        self.chatbot.capacity = int(self.entry_capacity.get())
        self.chatbot.inventory_levels = int(self.entry_inventory.get())
        self.chatbot.subcontracting = int(self.entry_subcontracting.get())
        self.chatbot.workforce_size = int(self.entry_workforce.get())
        self.chatbot.part_time_workers = int(self.entry_part_time.get())

        # Execute the main workflow
        self.chatbot.make_aggregate_plan()
        self.chatbot.provide_alternative_decisions()


class AggregatePlanningChatbot:
    def __init__(self):
        # Initialize chatbot with default values
        self.forecasted_demand = 0
        self.capacity = 0
        self.inventory_levels = 0
        self.subcontracting = 0
        self.workforce_size = 0
        self.part_time_workers = 0

    def get_user_input(self):
        # Collect user input for key planning parameters
        print("Welcome to the Aggregate Planning Chatbot!")
        self.forecasted_demand = int(input("Enter forecasted demand: "))
        self.capacity = int(input("Enter production capacity: "))
        self.inventory_levels = int(input("Enter current inventory levels: "))
        self.subcontracting = int(input("Enter subcontracting capacity: "))
        self.workforce_size = int(input("Enter current workforce size: "))
        self.part_time_workers = int(input("Enter part-time workers: "))

    def make_aggregate_plan(self):
        # Calculate production shortfall and excess capacity
        shortfall = self.forecasted_demand - \
            (self.capacity + self.inventory_levels)

        if shortfall > 0:
            # If there is a production shortfall, handle it
            print(f"\nShortfall in production: {shortfall} units")
            self.handle_production_shortfall(shortfall)

        excess_capacity = self.capacity - self.forecasted_demand
        if excess_capacity > 0:
            # If there is excess production capacity, handle it
            print(f"\nExcess production capacity: {excess_capacity} units")
            self.handle_excess_capacity(excess_capacity)

    def handle_production_shortfall(self, shortfall):
        # Determine actions to address the production shortfall
        if shortfall > self.subcontracting:
            # If subcontracting is not enough, suggest options
            print(
                "Options: Increase subcontracting, hire more workers, or increase part-time workers.")
        else:
            # If subcontracting is sufficient, suggest other options
            print(
                "Options: Increase production capacity, hire more workers, or increase part-time workers.")

    def handle_excess_capacity(self, excess_capacity):
        # Determine actions to utilize excess production capacity
        if excess_capacity > self.inventory_levels:
            # If excess capacity is more than inventory, suggest options
            print(
                "Options: Reduce production, reduce workforce, or decrease subcontracting.")
        else:
            # If excess capacity is not significant, suggest other options
            print("Options: Maintain current capacity, increase inventory, or consider temporary workforce reduction.")

    def provide_alternative_decisions(self):
        # Ask the user whether they want to increase money or moderate expenses
        user_choice = input(
            "\nDo you want to increase money (I) or moderate (M)? ").upper()

        if user_choice == 'I':
            # Provide alternative decisions for increasing money
            print("To increase money, consider optimizing production, reducing inventory, or improving subcontracting efficiency.")
        elif user_choice == 'M':
            # Provide alternative decisions for moderating expenses
            print("To moderate, focus on balancing production, maintaining a stable workforce, and managing inventory effectively.")
        else:
            # Handle invalid user input
            print("Invalid choice. Please enter 'I' for increase or 'M' for moderate.")


if __name__ == "__main__":
    # Create an instance of the GUI
    chatbot_gui = AggregatePlanningChatbotGUI()
    chatbot_gui.mainloop()
