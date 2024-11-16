import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import json
import os

# Product model
class Product:
    def __init__(self, id, name, quantity, price, customer_name='', phone_number=''):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.customer_name = customer_name
        self.phone_number = phone_number

# Bill model
class Bill:
    def __init__(self, id, product_name, quantity, total_price):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price

# Inventory Manager
class InventoryManager:
    def __init__(self, inventory_filename='inventory.json', bill_filename='bills.json'):
        self.inventory_filename = inventory_filename
        self.bill_filename = bill_filename
        self.products = self.load_inventory()
        self.bills = self.load_bills()

    def load_inventory(self):
        if os.path.exists(self.inventory_filename):
            with open(self.inventory_filename, 'r') as file:
                products_data = json.load(file)
                return [Product(**data) for data in products_data]
        return []

    def save_inventory(self):
        with open(self.inventory_filename, 'w') as file:
            json.dump([vars(product) for product in self.products], file)

    def load_bills(self):
        if os.path.exists(self.bill_filename):
            with open(self.bill_filename, 'r') as file:
                bills_data = json.load(file)
                return [Bill(**data) for data in bills_data]
        return []

    def save_bills(self):
        with open(self.bill_filename, 'w') as file:
            json.dump([vars(bill) for bill in self.bills], file)

    def add_product(self, product):
        self.products.append(product)
        self.save_inventory()

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]
        self.save_inventory()

    def add_bill(self, bill):
        self.bills.append(bill)
        self.save_bills()

# Home page (Splash Screen)
class HomePage:
    def __init__(self, root, switch_to_inventory, switch_to_billing, generate_bill_report):
        self.root = root
        self.switch_to_inventory = switch_to_inventory
        self.switch_to_billing = switch_to_billing
        self.generate_bill_report = generate_bill_report
        root.title("StockMate - Welcome")
        root.geometry("600x500")
        root.config(bg="#fff")

        # Title Font
        title_font = Font(family="Helvetica", size=28, weight="bold")
        subtitle_font = Font(family="Helvetica", size=14, slant="italic")

        # Container frame with border
        self.container_frame = tk.Frame(root, bg="#fff", highlightbackground="#34568B", highlightthickness=3, bd=3, relief=tk.RIDGE)
        self.container_frame.pack(pady=50, padx=30, fill=tk.BOTH, expand=True)

        # Logo area with border
        self.logo_label = tk.Label(self.container_frame, text="StockMate", font=title_font, fg="#34568B", bg="#fff")
        self.logo_label.pack(pady=40)

        # Tagline
        self.tagline_label = tk.Label(self.container_frame, text="Your Trusted Inventory Companion", font=subtitle_font, fg="#2b3d52", bg="#fff")
        self.tagline_label.pack(pady=10)

        # Start button with border
        self.start_button = tk.Button(self.container_frame, text="Enter Inventory System", command=self.switch_to_inventory, font=("Helvetica", 14), bg="#34568B", fg="#fff", width=25, relief=tk.RAISED, bd=3)
        self.start_button.pack(pady=10)

        # Billing button with border
        self.billing_button = tk.Button(self.container_frame, text="Go to Billing System", command=self.switch_to_billing, font=("Helvetica", 14), bg="#34568B", fg="#fff", width=25, relief=tk.RAISED, bd=3)
        self.billing_button.pack(pady=10)

        # Bill Report button with border
        self.bill_report_button = tk.Button(self.container_frame, text="Generate Bill Report", command=self.generate_bill_report, font=("Helvetica", 14), bg="#FF5733", fg="#fff", width=25, relief=tk.RAISED, bd=3)
        self.bill_report_button.pack(pady=10)

# Inventory Page
class InventoryPage:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.build_inventory_page()

    def build_inventory_page(self):
        self.clear_frame()
        self.root.title("StockMate - Inventory Management")
        self.root.geometry("700x600")
        self.root.config(bg="#eef2f5")

        # Title Font
        title_font = Font(family="Helvetica", size=22, weight="bold")

        # Create a back arrow button with border
        self.back_button = tk.Button(self.root, text="← Back", command=self.go_back_to_home, font=("Helvetica", 12), bg="#34568B", fg="#fff", relief=tk.RAISED, bd=3)
        self.back_button.pack(pady=10, anchor="w", padx=10)

        # Create title label
        self.title_label = tk.Label(self.root, text="Inventory Management", font=title_font, fg="#34568B", bg="#eef2f5")
        self.title_label.pack(pady=20)

        # Create a Frame for Product and Customer Information with border
        self.input_frame = tk.Frame(self.root, bg="#fff", highlightbackground="#34568B", highlightthickness=3, bd=3, relief=tk.RIDGE)
        self.input_frame.pack(pady=20, padx=20, fill=tk.X)

        # Product Section
        self.product_label = tk.Label(self.input_frame, text="Add Product Information", font=("Helvetica", 14), bg="#fff", fg="#2b3d52")
        self.product_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.name_label = tk.Label(self.input_frame, text="Product Name:", bg="#fff", fg="#2b3d52")
        self.name_label.grid(row=1, column=0, sticky=tk.W, padx=10)
        self.name_entry = ttk.Entry(self.input_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=10)

        self.quantity_label = tk.Label(self.input_frame, text="Quantity:", bg="#fff", fg="#2b3d52")
        self.quantity_label.grid(row=2, column=0, sticky=tk.W, padx=10)
        self.quantity_entry = ttk.Entry(self.input_frame, width=30)
        self.quantity_entry.grid(row=2, column=1, padx=10)

        self.price_label = tk.Label(self.input_frame, text="Price:", bg="#fff", fg="#2b3d52")
        self.price_label.grid(row=3, column=0, sticky=tk.W, padx=10)
        self.price_entry = ttk.Entry(self.input_frame, width=30)
        self.price_entry.grid(row=3, column=1, padx=10)

        # Add Product Button with border
        self.add_button = tk.Button(self.input_frame, text="Add Product", command=self.add_product, width=20, bg="#2b3d52", fg="#fff", relief=tk.RAISED, bd=3)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Product List frame with border
        self.list_frame = tk.Frame(self.root, bg="#fff", highlightbackground="#34568B", highlightthickness=3, bd=3, relief=tk.RIDGE)
        self.list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Create a scrollable listbox to show products
        self.product_list = tk.Listbox(self.list_frame, height=10, width=70, bg="#f4f6f8", fg="#2e2e2e", font=("Arial", 12))
        self.product_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.product_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.product_list.config(yscrollcommand=self.scrollbar.set)

        # Populate the product list with current inventory
        self.populate_product_list()

    def go_back_to_home(self):
        self.clear_frame()
        InventoryApp(self.root)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def populate_product_list(self):
        self.product_list.delete(0, tk.END)
        for product in self.manager.products:
            self.product_list.insert(tk.END, f"{product.name} - Qty: {product.quantity} - ${product.price:.2f}")

    def add_product(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            price = float(self.price_entry.get())
            if name and quantity >= 0 and price >= 0:
                product_id = len(self.manager.products) + 1  # Simple ID assignment
                new_product = Product(product_id, name, quantity, price)
                self.manager.add_product(new_product)
                self.populate_product_list()  # Refresh the product list
                self.name_entry.delete(0, tk.END)
                self.quantity_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                messagebox.showinfo("Product Added", f"{name} has been added to the inventory.")
            else:
                messagebox.showerror("Input Error", "Please enter valid product details.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for quantity and price.")

# Billing Page
class BillingPage:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.build_billing_page()

    def build_billing_page(self):
        self.clear_frame()
        self.root.title("StockMate - Billing System")
        self.root.geometry("700x600")
        self.root.config(bg="#eef2f5")

        # Title Font
        title_font = Font(family="Helvetica", size=22, weight="bold")

        # Create a back arrow button with border
        self.back_button = tk.Button(self.root, text="← Back", command=self.go_back_to_home, font=("Helvetica", 12), bg="#34568B", fg="#fff", relief=tk.RAISED, bd=3)
        self.back_button.pack(pady=10, anchor="w", padx=10)

        # Create title label
        self.title_label = tk.Label(self.root, text="Billing System", font=title_font, fg="#34568B", bg="#eef2f5")
        self.title_label.pack(pady=20)

        # Create a Frame for Product Selection with border
        self.product_frame = tk.Frame(self.root, bg="#fff", highlightbackground="#34568B", highlightthickness=3, bd=3, relief=tk.RIDGE)
        self.product_frame.pack(pady=20, padx=20, fill=tk.X)

        # Create a label for product selection
        self.select_label = tk.Label(self.product_frame, text="Select Product to Bill:", bg="#fff", fg="#2b3d52")
        self.select_label.pack(pady=10)

        # Create a Listbox for products
        self.product_list = tk.Listbox(self.product_frame, height=10, width=70, bg="#f4f6f8", fg="#2e2e2e", font=("Arial", 12))
        self.product_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the product list
        self.scrollbar = ttk.Scrollbar(self.product_frame, orient="vertical", command=self.product_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.product_list.config(yscrollcommand=self.scrollbar.set)

        # Populate the product list with current inventory
        self.populate_product_list()

        # Quantity Entry
        self.quantity_label = tk.Label(self.product_frame, text="Quantity to Bill:", bg="#fff", fg="#2b3d52")
        self.quantity_label.pack(pady=10)
        self.quantity_entry = ttk.Entry(self.product_frame, width=10)
        self.quantity_entry.pack(pady=10)

        # Create + and - buttons
        self.increment_button = tk.Button(self.product_frame, text="+", command=self.increment_quantity, bg="#34568B", fg="#fff", width=5)
        self.increment_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.decrement_button = tk.Button(self.product_frame, text="-", command=self.decrement_quantity, bg="#34568B", fg="#fff", width=5)
        self.decrement_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Billing Button with border
        self.bill_button = tk.Button(self.root, text="Create Bill", command=self.create_bill, width=20, bg="#2b3d52", fg="#fff", relief=tk.RAISED, bd=3)
        self.bill_button.pack(pady=20)

    def go_back_to_home(self):
        self.clear_frame()
        InventoryApp(self.root)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def populate_product_list(self):
        self.product_list.delete(0, tk.END)
        for product in self.manager.products:
            self.product_list.insert(tk.END, f"{product.name} - Qty: {product.quantity} - ${product.price:.2f}")

    def increment_quantity(self):
        selected_index = self.product_list.curselection()
        if selected_index:
            try:
                current_quantity = int(self.quantity_entry.get() or 0)
                if current_quantity < self.manager.products[selected_index[0]].quantity:
                    self.quantity_entry.delete(0, tk.END)
                    self.quantity_entry.insert(0, str(current_quantity + 1))
                else:
                    messagebox.showwarning("Quantity Limit", "Cannot exceed available stock.")
            except ValueError:
                self.quantity_entry.delete(0, tk.END)
                self.quantity_entry.insert(0, "1")  # Default to 1 if input is invalid

    def decrement_quantity(self):
        selected_index = self.product_list.curselection()
        if selected_index:
            try:
                current_quantity = int(self.quantity_entry.get() or 0)
                if current_quantity > 0:
                    self.quantity_entry.delete(0, tk.END)
                    self.quantity_entry.insert(0, str(current_quantity - 1))
                else:
                    messagebox.showwarning("Quantity Limit", "Quantity cannot be less than 0.")
            except ValueError:
                self.quantity_entry.delete(0, tk.END)
                self.quantity_entry.insert(0, "0")  # Default to 0 if input is invalid

    def create_bill(self):
        selected_index = self.product_list.curselection()
        if selected_index:
            selected_product = self.manager.products[selected_index[0]]
            try:
                quantity_to_bill = int(self.quantity_entry.get())
                if quantity_to_bill > 0 and quantity_to_bill <= selected_product.quantity:
                    total_price = selected_product.price * quantity_to_bill
                    # Deduct the billed quantity from the inventory
                    selected_product.quantity -= quantity_to_bill

                    # Create and save the bill
                    bill_id = len(self.manager.bills) + 1  # Simple ID assignment
                    new_bill = Bill(bill_id, selected_product.name, quantity_to_bill, total_price)
                    self.manager.add_bill(new_bill)

                    self.manager.save_inventory()  # Save updated inventory to the file
                    self.populate_product_list()  # Refresh the product list
                    messagebox.showinfo("Bill Created", f"Bill for {quantity_to_bill} of {selected_product.name} has been created.\nTotal: ${total_price:.2f}")
                else:
                    messagebox.showerror("Quantity Error", "Please enter a valid quantity.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for quantity.")
        else:
            messagebox.showerror("Selection Error", "Please select a product to bill.")

# Bill Report Page
class BillReportPage:
    def __init__(self, root, switch_to_home):
        self.root = root
        self.switch_to_home = switch_to_home
        self.build_report_page()

    def build_report_page(self):
        self.clear_frame()
        self.root.title("StockMate - Bill Report")
        self.root.geometry("700x600")
        self.root.config(bg="#eef2f5")

        # Title Font
        title_font = Font(family="Helvetica", size=22, weight="bold")

        # Create a back arrow button with border
        self.back_button = tk.Button(self.root, text="← Back", command=self.switch_to_home, font=("Helvetica", 12), bg="#34568B", fg="#fff", relief=tk.RAISED, bd=3)
        self.back_button.pack(pady=10, anchor="w", padx=10)

        # Create title label
        self.title_label = tk.Label(self.root, text="Bill Report", font=title_font, fg="#34568B", bg="#eef2f5")
        self.title_label.pack(pady=20)

        # Create a Frame for displaying the report
        self.report_frame = tk.Frame(self.root, bg="#fff", highlightbackground="#34568B", highlightthickness=3, bd=3, relief=tk.RIDGE)
        self.report_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create a Listbox to display the report
        self.report_list = tk.Listbox(self.report_frame, height=20, width=80, bg="#f4f6f8", fg="#2e2e2e", font=("Arial", 12))
        self.report_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the report list
        self.scrollbar = ttk.Scrollbar(self.report_frame, orient="vertical", command=self.report_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.report_list.config(yscrollcommand=self.scrollbar.set)

        # Load the bill report data
        self.load_report_data()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_report_data(self):
        if os.path.exists("bills.json"):
            with open("bills.json", 'r') as file:
                bills_data = json.load(file)
                for bill in bills_data:
                    self.report_list.insert(tk.END, f"Bill ID: {bill['id']} - {bill['product_name']} - Qty: {bill['quantity']} - Total: ${bill['total_price']:.2f}")

# Main Application
class InventoryApp:
    def __init__(self, root):
        self.manager = InventoryManager()
        self.root = root
        self.build_home_page()

    def build_home_page(self):
        self.clear_frame()
        HomePage(self.root, self.switch_to_inventory, self.switch_to_billing, self.show_bill_report)

    def switch_to_inventory(self):
        InventoryPage(self.root, self.manager)

    def switch_to_billing(self):
        BillingPage(self.root, self.manager)

    def show_bill_report(self):
        BillReportPage(self.root, self.build_home_page)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

