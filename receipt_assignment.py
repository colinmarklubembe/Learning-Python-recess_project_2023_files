import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class ReceiptApp:
    def __init__(self, master):
        self.master = master
        master.title("Receipt Printing Program by Lubembe Colin Wafula")

        # Create labels, entry fields, and buttons
        self.label_item = tk.Label(master, text="Item:")
        self.label_item.grid(row=0, column=0, padx=10, pady=10)
        self.entry_item = tk.Entry(master)
        self.entry_item.grid(row=0, column=1, padx=10, pady=10)

        self.label_price = tk.Label(master, text="Price:")
        self.label_price.grid(row=1, column=0, padx=10, pady=10)
        self.entry_price = tk.Entry(master)
        self.entry_price.grid(row=1, column=1, padx=10, pady=10)

        self.button_add = tk.Button(master, text="Add to Receipt", command=self.add_to_receipt)
        self.button_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.text_receipt = tk.Text(master)
        self.text_receipt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_print = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.button_print.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Initialize variables
        self.items = []
        self.prices = []

    def add_to_receipt(self):
        item = self.entry_item.get()
        price = self.entry_price.get()

        if item and price:
            self.items.append(item)
            self.prices.append(float(price))

            # Append item and price to the receipt text widget
            self.text_receipt.insert(tk.END, f"{item}: ${price}\n")

            # Clear the entry fields after adding to the receipt
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)

    def print_receipt(self):
        if not self.items:
            messagebox.showinfo("Error", "No items in the receipt.")
            return

        # Calculate subtotal, tax, and total
        subtotal = sum(self.prices)
        tax_rate = 0.1  # 10% tax rate
        tax = subtotal * tax_rate
        total = subtotal + tax

        # Generate receipt header with date/time
        receipt_header = f"Receipt\nDate/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        # Generate receipt items with prices
        receipt_items = ""
        for item, price in zip(self.items, self.prices):
            receipt_items += f"{item}: ${price:.2f}\n"

        # Generate receipt footer with subtotal, tax, and total
        receipt_footer = f"\nSubtotal: ${subtotal:.2f}\nTax ({tax_rate * 100}%): ${tax:.2f}\nTotal: ${total:.2f}\n"

        # Generate the complete receipt
        receipt = receipt_header + receipt_items + receipt_footer

        # Display the receipt in a message box
        messagebox.showinfo("Receipt", receipt)

        # Save the receipt to a file
        self.save_receipt(receipt)

        # Clear the receipt data and text widget
        self.items.clear()
        self.prices.clear()
        self.text_receipt.delete("1.0", tk.END)

    def save_receipt(self, receipt):
        filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(receipt)
        messagebox.showinfo("Receipt Saved", f"The receipt has been saved as {filename}.")


# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the ReceiptApp class
app = ReceiptApp(root)

# Run the Tkinter event loop
root.mainloop()
