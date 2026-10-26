# 1) Import tkinter modules:
#    a) Import `tkinter as tk` to create the GUI window and canvas.
#    b) Import `ttk` for styled widgets like Frame, Label, Button, Combobox.
#    c) Import `messagebox` to show popup messages.

# 2) Create a class `RestaurantOrderManagement` to build and run the application.

# 3) Define the constructor `__init__(self, root)`:
#    a) Store the main window in `self.root`.
#    b) Set the window title to "Restaurant Management App".

# 4) Create a dictionary `self.menu_items` to store menu item names and their prices (in USD).

# 5) Set an exchange rate `self.exchange_rate = 82`
#    to convert USD prices into INR when required.

# 6) Call `self.setup_background(root)` to load and display a background image.

# 7) Create a `ttk.Frame` and place it at the center of the window:
#    (This frame holds all the order widgets.)

# 8) Add a heading label "Restaurant Order Management" using `ttk.Label(...)`.

# 9) Create two empty dictionaries:
#    a) `self.menu_labels` to store label widgets for each menu item.
#    b) `self.menu_quantities` to store entry widgets for quantities.

# 10) Use a loop to create menu item rows:
#     a) For each item and price in `self.menu_items`:
#        i) Create a label showing item name and price.
#        ii) Create an entry box to input quantity.
#        iii) Store label references in `self.menu_labels`.
#        iv) Store entry references in `self.menu_quantities`.

# 11) Create a currency selection section:
#     a) Create a `StringVar` called `self.currency_var`.
#     b) Add a "Currency:" label.
#     c) Add a dropdown (`ttk.Combobox`) with options "USD" and "INR".
#     d) Set default selection to "USD".
#     e) Attach a trace to `self.currency_var` so when currency changes,
#        it automatically calls `self.update_menu_prices`.

# 12) Add a "Place Order" button:
#     a) When clicked, it runs `self.place_order()`.

# 13) Define `setup_background(self, root)`:
#     a) Create a Canvas of size 800x600.
#     b) Load the background image file `background.png` using `tk.PhotoImage`.
#     c) Resize it approximately using `.subsample(...)`.
#     d) Place the image on the canvas using `create_image(...)`.
#     e) Store the image reference (`canvas.image`) to prevent garbage collection.

# 14) Define `update_menu_prices(self, *args)`:
#     a) Read the selected currency from `self.currency_var`.
#     b) Set currency symbol:
#        - INR -> "₹"
#        - USD -> "$"
#     c) Set conversion rate:
#        - INR -> exchange rate
#        - USD -> 1
#     d) Update every menu label text to show the converted price.

# 15) Define `place_order(self)`:
#     a) Initialize `total_cost = 0` and `order_summary` message text.
#     b) Determine currency symbol and conversion rate (same as above).
#     c) Loop through each menu item entry:
#        i) Read quantity using `entry.get()`.
#        ii) If quantity is a digit, convert it to int.
#        iii) Compute price (converted), item cost, and add to total.
#        iv) If quantity > 0, add line details to `order_summary`.
#     d) If `total_cost > 0`, show the order summary in a messagebox.
#     e) Else, show an error message asking the user to order at least one item.

# 16) In the main block (`if __name__ == "__main__":`):
#     a) Create the main window using `root = tk.Tk()`.
#     b) Create the app object `app = RestaurantOrderManagement(root)`.
#     c) Set the window size to 800x600.
#     d) Start the GUI loop using `root.mainloop()`.