import requests
import folium
import webview
import os
import tkinter as tk
from tkinter import messagebox

def get_ip_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'fail':
            return None
        return {
            "lat": data["lat"],
            "lon": data["lon"],
            "city": data["city"],
            "region": data["regionName"],
            "country": data["country"]
        }
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get IP location: {e}")
        return None

def create_interactive_map(ip):
    location = get_ip_location(ip)
    if location:
        # Create an interactive map centered around the location
        map = folium.Map(location=[location["lat"], location["lon"]], zoom_start=10)
        folium.Marker([location["lat"], location["lon"]], popup=f"{location['city']}, {location['region']}, {location['country']}").add_to(map)

        # Save the interactive map to an HTML file
        map_file = "map.html"
        map.save(map_file)

        # Update location label in the Tkinter window
        location_label.config(text=f"State: {location['region']}, Country: {location['country']}")
        status_label.config(text="")

        # Open the HTML file in a new window (on the main thread)
        open_map_window(map_file)
    else:
        messagebox.showerror("Error", "Invalid IP address or unable to fetch location")
        status_label.config(text="")

def open_map_window(map_file):
    # Create and show the webview window on the main thread
    def show_map():
        webview.create_window("IP Location Map", f"file:///{os.path.abspath(map_file)}")
        webview.start()

    show_map()

def on_submit():
    # Show loading message
    status_label.config(text="Loading...")

    # Run create_interactive_map without threading (to handle UI updates on the main thread)
    ip = ip_entry.get()
    create_interactive_map(ip)

# Set up the Tkinter window
window = tk.Tk()
window.title("IP Locator")

tk.Label(window, text="Enter IP address:").pack(pady=10)
ip_entry = tk.Entry(window)
ip_entry.pack(pady=5)

tk.Button(window, text="Find Location", command=on_submit).pack(pady=10)

location_label = tk.Label(window, text="")
location_label.pack(pady=10)

status_label = tk.Label(window, text="")
status_label.pack(pady=10)

window.mainloop()
