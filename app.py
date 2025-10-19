import tkinter as tk

# Step 1: Create a window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Step 2: Labels and entry fields
tk.Label(root, text="Bill Amount ($):", bg="#f0f0f0").pack(pady=5)
entry_bill = tk.Entry(root)
entry_bill.pack(pady=5)

tk.Label(root, text="Tip Percentage (%):", bg="#f0f0f0").pack(pady=5)
entry_tip = tk.Entry(root)
entry_tip.pack(pady=5)

tk.Label(root, text="Number of People:", bg="#f0f0f0").pack(pady=5)
entry_people = tk.Entry(root)
entry_people.pack(pady=5)

# Result label
label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 11, "bold"))
label_result.pack(pady=10)

# Step 3: Calculate function
def calculate_tip():
    try:
        bill_amount = float(entry_bill.get())
        tip_percent = float(entry_tip.get())
        people = int(entry_people.get())

        tip_amount = bill_amount * (tip_percent / 100)
        total_amount = bill_amount + tip_amount
        amount_per_person = total_amount / people

        result = f"Tip: ${tip_amount:.2f}\nTotal: ${total_amount:.2f}\nPer Person: ${amount_per_person:.2f}"
        label_result.config(text=result)
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Step 4: Calculate button
tk.Button(root, text="Calculate", command=calculate_tip, bg="#4CAF50", fg="white").pack(pady=10)

# Run the app
root.mainloop()
