# Weather Forecast Application

This is a Python-based weather forecast application built using the `customtkinter` library for the graphical user interface (GUI) and the `requests` library to fetch weather data from the OpenWeatherMap API.

## Features
- **User Authentication**: Login and sign-up screens for user authentication.
- **Weather Forecast**: Fetch and display weather forecasts for a specified city and number of days (up to 5 days).
- **User-Friendly Interface**: A clean and intuitive GUI designed with `customtkinter`.

## Requirements
To run this application, you need the following Python libraries:
- `customtkinter`
- `requests`

You can install the required libraries using pip:

  ```bash
  pip install customtkinter requests

## How to Use

Clone this repository to your local machine:

  ```bash
  git clone https://github.com/deerws/weather-report.git

Navigate to the project directory:

  ```bash
  cd your-repo-name

Run the application:

  ```bash
  python main.py

Use the application:

Login Screen: Enter your username and password to log in.

Sign-Up Screen: Create a new account if you don't have one.

Weather Forecast: After logging in, enter a city name and the number of days (up to 5) to get the weather forecast.

## Code Overview
The application is structured as follows:

Main Application Class (App): Handles the GUI and user interactions.

conf_windown_start(): Configures the main window settings.

background(): Sets the appearance mode and color theme.

login_screen(): Displays the login and sign-up screens.

forms(): Displays the weather forecast input form.

forms2(): Displays the sign-up form.

open(): Fetches and displays the weather forecast data.

API Key
The application uses the OpenWeatherMap API to fetch weather data. You need to replace the API_KEY variable in the code with your own API key from OpenWeatherMap.

python:

  API_KEY = "your_api_key_here"
  Screenshots
  Login Screen
  Weather Forecast Screen

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

