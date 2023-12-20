import requests
import tkinter as tk
from datetime import datetime

def trackbitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + " $")
    labelTime.config(text="Updated at: " + time)

    canvas.after(1000, trackbitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")  # Corrected the typo here
canvas.title("BITCOIN TRACKER")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="Bitcoins Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

trackbitcoin()  # Added this line to start tracking immediately

canvas.mainloop()



# def trackbitcoin():
#     # API URL to get Bitcoin price in USD, JPY, and EUR
#     url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    
#     # Sending an HTTP GET request to the Cryptocompare API and converting the response to JSON format
#     response = requests.get(url).json()
    
#     # Extracting the price of Bitcoin in USD from the JSON response
#     price = response["USD"]
    
#     # Getting the current time in the "Hour:Minute:Second" format
#     time = datetime.now().strftime("%H:%M:%S")

#     # Updating the text of the labelPrice widget in the Tkinter GUI with the current Bitcoin price
#     labelPrice.config(text=str(price) + " $")
    
#     # Updating the text of the labelTime widget in the Tkinter GUI with the current time
#     labelTime.config(text="Updated at: " + time)

#     # Scheduling the trackbitcoin function to be called again after 1000 milliseconds (1 second)
#     canvas.after(1000, trackbitcoin)
