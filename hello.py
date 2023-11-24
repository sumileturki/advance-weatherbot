# # import requests
# # from tkinter import *
# # from tkinter import messagebox
# # import geocoder

# # API_KEY = '712e2a8a4b4fd743f5ef09d373f4e009'
# # BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# # def get_weather_by_location(latitude, longitude):
# #     try:
# #         complete_url = f"{BASE_URL}lat={latitude}&lon={longitude}&appid={API_KEY}"
# #         response = requests.get(complete_url)
# #         data = response.json()

# #         if data["cod"] != "404":
# #             main_data = data["main"]
# #             temperature = main_data["temp"]
# #             pressure = main_data["pressure"]
# #             humidity = main_data["humidity"]
# #             return f"Temperature: {temperature} Kelvin\nAtmospheric Pressure: {pressure} hPa\nHumidity: {humidity}%", None
# #         else:
# #             return "Location not found.", None
# #     except Exception as e:
# #         return f"An error occurred: {e}", None

# # def get_weather_by_city(city_name):
# #     try:
# #         complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"
# #         response = requests.get(complete_url)
# #         data = response.json()

# #         if data["cod"] != "404":
# #             main_data = data["main"]
# #             temperature = main_data["temp"]
# #             pressure = main_data["pressure"]
# #             humidity = main_data["humidity"]
# #             return f"Temperature: {temperature} Kelvin\nAtmospheric Pressure: {pressure} hPa\nHumidity: {humidity}%", None
# #         else:
# #             return "City not found.", None
# #     except Exception as e:
# #         return f"An error occurred: {e}", None

# # def get_live_location():
# #     g = geocoder.ip('me')
# #     latitude, longitude = g.latlng
# #     result, _ = get_weather_by_location(latitude, longitude)
# #     messagebox.showinfo("Weather Info", result)

# # def get_weather_command():
# #     city_name = entry.get()
# #     result, _ = get_weather_by_city(city_name)
# #     messagebox.showinfo("Weather Info", result)

# # root = Tk()
# # root.title("Weather Bot")

# # label1 = Label(root, text="Enter city name: ")
# # label1.pack()

# # entry = Entry(root)
# # entry.pack()

# # button1 = Button(root, text="Get Weather by City", command=get_weather_command)
# # button1.pack()

# # button2 = Button(root, text="Get Live Location Weather", command=get_live_location)
# # button2.pack()

# # root.mainloop()
# import requests
# import tkinter as tk
# from tkinter import messagebox
# from geopy.geocoders import Nominatim

# API_KEY = '712e2a8a4b4fd743f5ef09d373f4e009'
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# def get_weather_by_city(city_name):
#     try:
#         complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"
#         response = requests.get(complete_url)
#         data = response.json()

#         if data["cod"] != "404":
#             main_data = data["main"]
#             temperature = main_data["temp"]
#             pressure = main_data["pressure"]
#             humidity = main_data["humidity"]
#             return f"Temperature: {temperature} Kelvin\nAtmospheric Pressure: {pressure} hPa\nHumidity: {humidity}%", None
#         else:
#             return "City not found.", None
#     except Exception as e:
#         return f"An error occurred: {e}", None

# def get_weather_by_coordinates(lat, lon):
#     try:
#         complete_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}"
#         response = requests.get(complete_url)
#         data = response.json()

#         if data["cod"] != "404":
#             main_data = data["main"]
#             temperature = main_data["temp"]
#             pressure = main_data["pressure"]
#             humidity = main_data["humidity"]
#             return f"Temperature: {temperature} Kelvin\nAtmospheric Pressure: {pressure} hPa\nHumidity: {humidity}%", None
#         else:
#             return "Weather data not available for the specified location.", None
#     except Exception as e:
#         return f"An error occurred: {e}", None

# def on_live_location_click():
#     geolocator = Nominatim(user_agent="weather_app")
#     location = geolocator.geocode("")

#     if location:
#         lat, lon = location.latitude, location.longitude
#         result, _ = get_weather_by_coordinates(lat, lon)
#         messagebox.showinfo("Weather Info", result)
#     else:
#         messagebox.showinfo("Location Error", "Unable to fetch the live location.")

# def on_location_submit_click():
#     city_name = location_entry.get()
#     result, _ = get_weather_by_city(city_name)
#     messagebox.showinfo("Weather Info", result)

# root = tk.Tk()
# root.title("Weather Bot")

# label = tk.Label(root, text="Enter city name:")
# label.pack()

# location_entry = tk.Entry(root)
# location_entry.pack()

# location_submit_button = tk.Button(root, text="Get Weather by Location", command=on_location_submit_click)
# location_submit_button.pack()

# live_location_button = tk.Button(root, text="Get Weather by Live Location", command=on_live_location_click)
# live_location_button.pack()

# root.mainloop()
import requests
import pygame
import time

API_KEY = '712e2a8a4b4fd743f5ef09d373f4e009'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weather Forecasting Bot")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

def get_weather(city_name):
    try:
        complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main_data = data["main"]
            weather_data = data["weather"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather_description = weather_data[0]["description"]
            icon_id = weather_data[0]["icon"]
            return f"Temperature: {temperature} Kelvin\nHumidity: {humidity}%\nDescription: {weather_description}", icon_id
        else:
            return "City not found.", None
    except Exception as e:
        return f"An error occurred: {e}", None

def get_icon_image(icon_id):
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
    icon_response = requests.get(icon_url, stream=True)
    if icon_response.status_code == 200:
        icon_response.raw.decode_content = True
        icon_image = pygame.image.load(icon_response.raw)
        return icon_image
    else:
        return None

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    city_name = input("Enter city name: ")
    result, icon_id = get_weather(city_name)
    print(result)

    icon_image = get_icon_image(icon_id)

    raining_percentage = 25  # Example raining percentage

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Display weather information
        draw_text(result, font, BLACK, screen, 50, 50)

        # Display raining percentage
        draw_text(f"Raining Percentage: {raining_percentage}%", font, BLACK, screen, 50, 150)

        # Display weather icon
        if icon_image:
            screen.blit(icon_image, (300, 50))

        pygame.display.update()
        time.sleep(1)  # Animation delay

    pygame.quit()

if __name__ == '__main__':
    main()
