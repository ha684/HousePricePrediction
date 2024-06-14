import tkinter as tk
from tkinter import ttk, messagebox
from prediction import predict_house_price,suggest_house_features
from PIL import Image, ImageTk

def open_suggest_features_window():
    
    global price_entry
    suggest_features_window = tk.Toplevel(root)
    suggest_features_window.title("Suggest House Features")
    suggest_features_window.resizable(True, True)

    image = Image.open(r"C:\Users\OS\Desktop\Workspace\hapt\fpt.png")
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(suggest_features_window, image=photo)
    image_label.image = photo
    image_label.grid(row=0, column=0, padx=5, pady=10,columnspan=2)
    price_label = tk.Label(suggest_features_window, text="Enter Target Price:")
    price_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    price_entry = tk.Entry(suggest_features_window)
    price_entry.grid(row=1, column=1, padx=5, pady=5)

    suggest_button = tk.Button(suggest_features_window, text="Suggest Features", command=suggest_features)
    suggest_button.grid(row=2, columnspan=2, padx=5, pady=10)
    
def open_predict_price_window():
    
    predict_price_window = tk.Toplevel(root)
    predict_price_window.title("Predict House Price")
    predict_price_window.resizable(True, True)
    
    image = Image.open(r"C:\Users\OS\Desktop\Workspace\hapt\fpt.png")
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(predict_price_window, image=photo)
    image_label.image = photo 
    image_label.grid(row=0, column=0, padx=5, pady=10,columnspan=2)

    labels = ["Area:", "Bedrooms:", "Bathrooms:", "Stories:", "Main Road:", "Guest Room:",
              "Basement:", "Hot Water Heating:", "Air Conditioning:", "Parking:", 
              "Preferred Area:", "Furnishing Status:"]
    for i, label_text in enumerate(labels):
        tk.Label(predict_price_window, text=label_text).grid(row=i+1, column=0, sticky="w", padx=5, pady=5)

    global area_entry, bedrooms_entry, bathrooms_entry, stories_entry, mainroad_var, guestroom_var
    global basement_var, hotwaterheating_var, airconditioning_var, parking_entry, prefarea_var, furnishingstatus_var
    global mainroad_entry, guestroom_entry, basement_entry, hotwaterheating_entry, airconditioning_entry
    global prefarea_entry, furnishingstatus_entry

    area_entry = tk.Entry(predict_price_window)
    area_entry.grid(row=1, column=1, padx=5, pady=5)
    bedrooms_entry = tk.Entry(predict_price_window)
    bedrooms_entry.grid(row=2, column=1, padx=5, pady=5)
    bathrooms_entry = tk.Entry(predict_price_window)
    bathrooms_entry.grid(row=3, column=1, padx=5, pady=5)
    stories_entry = tk.Entry(predict_price_window)
    stories_entry.grid(row=4, column=1, padx=5, pady=5)

    mainroad_var = tk.StringVar(value="yes")
    guestroom_var = tk.StringVar(value="yes")
    basement_var = tk.StringVar(value="yes")
    hotwaterheating_var = tk.StringVar(value="yes")
    airconditioning_var = tk.StringVar(value="yes")
    prefarea_var = tk.StringVar(value="yes")
    furnishingstatus_var = tk.StringVar(value="furnished")

    mainroad_entry = ttk.Combobox(predict_price_window, textvariable=mainroad_var, values=['yes', 'no'])
    mainroad_entry.grid(row=5, column=1, padx=5, pady=5)
    guestroom_entry = ttk.Combobox(predict_price_window, textvariable=guestroom_var, values=['yes', 'no'])
    guestroom_entry.grid(row=6, column=1, padx=5, pady=5)
    basement_entry = ttk.Combobox(predict_price_window, textvariable=basement_var, values=['yes', 'no'])
    basement_entry.grid(row=7, column=1, padx=5, pady=5)
    hotwaterheating_entry = ttk.Combobox(predict_price_window, textvariable=hotwaterheating_var, values=['yes', 'no'])
    hotwaterheating_entry.grid(row=8, column=1, padx=5, pady=5)
    airconditioning_entry = ttk.Combobox(predict_price_window, textvariable=airconditioning_var, values=['yes', 'no'])
    airconditioning_entry.grid(row=9, column=1, padx=5, pady=5)

    parking_entry = tk.Entry(predict_price_window)
    parking_entry.grid(row=10, column=1, padx=5, pady=5)

    prefarea_entry = ttk.Combobox(predict_price_window, textvariable=prefarea_var, values=['yes', 'no'])
    prefarea_entry.grid(row=11, column=1, padx=5, pady=5)
    furnishingstatus_entry = ttk.Combobox(predict_price_window, textvariable=furnishingstatus_var, values=['furnished', 'semi-furnished', 'unfurnished'])
    furnishingstatus_entry.grid(row=12, column=1, padx=5, pady=5)

    predict_button = tk.Button(predict_price_window, text="Predict", command=predict_price)
    predict_button.grid(row=13, column=0, padx=5, pady=10)

    clear_button = tk.Button(predict_price_window, text="Clear", command=clear_fields)
    clear_button.grid(row=13, column=1, padx=5, pady=10)
    area_entry.focus()
    
def suggest_features():
    
    try:
        user_price = int(price_entry.get())
        
        y,suggested_features = suggest_house_features(user_price)
        message = "Features corresponding to the closest price of $" + str(y) + "\n\n"
        message += "Suggested Features:\n" + str(suggested_features)
        messagebox.showinfo("Suggested Features", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric price.")

def predict_price():
    
    try:
        area = int(area_entry.get())
        bedrooms = int(bedrooms_entry.get())
        bathrooms = int(bathrooms_entry.get())
        stories = int(stories_entry.get())
        mainroad = mainroad_var.get()
        guestroom = guestroom_var.get()
        basement = basement_var.get()
        hotwaterheating = hotwaterheating_var.get()
        airconditioning = airconditioning_var.get()
        parking = int(parking_entry.get())
        prefarea = prefarea_var.get()
        furnishingstatus = furnishingstatus_var.get()
        if area < 1500 or area > 17000:
            messagebox.showerror("Error", "Can not predict")
            return
        
        value = [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                 hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]
        
        predicted_price = predict_house_price(value)
        
        messagebox.showinfo("Predicted Price", f"The predicted house price is: {predicted_price}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for all fields.")

def clear_fields():
    
    area_entry.delete(0, tk.END)
    bedrooms_entry.delete(0, tk.END)
    bathrooms_entry.delete(0, tk.END)
    stories_entry.delete(0, tk.END)
    mainroad_entry.set('')
    guestroom_entry.set('')
    basement_entry.set('')
    hotwaterheating_entry.set('')
    airconditioning_entry.set('')
    parking_entry.delete(0, tk.END)
    prefarea_entry.set('')
    furnishingstatus_entry.set('')

def main():
    global root
    root = tk.Tk()
    root.title("Main Menu")

    suggest_button = tk.Button(root, text="Suggest House Features", command=open_suggest_features_window)
    suggest_button.grid(row=1, column=0, padx=10, pady=10)

    predict_button = tk.Button(root, text="Predict House Price", command=open_predict_price_window)
    predict_button.grid(row=1, column=1, padx=10, pady=10)
    
    image = Image.open(r"C:\Users\OS\Desktop\Workspace\hapt\fpt.png")
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo)
    image_label.image = photo 
    image_label.grid(row=0, column=0, padx=5, pady=10,columnspan=2)
    root.mainloop()

main()