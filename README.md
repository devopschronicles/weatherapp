
# **Weather App - Flask Version**

This Weather App provides real-time weather forecasts based on user input. It uses the **OpenWeatherMap API** to fetch weather data and displays it in a modern and responsive dashboard interface.

## **Features**

- **Current Weather:**
  - Displays the temperature, humidity, wind speed, and weather conditions.
  - Shows the weather icon associated with the current conditions.
  
- **Hourly Forecast:**
  - Provides a 5-time-slot forecast for the day (next few hours) with temperature, weather conditions, and wind speed.
  
- **User-Friendly Interface:**
  - Built using **Flask**, **Bootstrap**, and a responsive layout for desktop and mobile devices.

## **Tech Stack**

- **Backend:**
  - Python 3
  - Flask
  - Requests library (for API calls)
  
- **Frontend:**
  - HTML
  - Bootstrap (for responsive design)
  
- **API:**
  - OpenWeatherMap API (for weather data)

## **Setup & Installation**

Follow these steps to get your app up and running locally.

### 1. **Clone the Repository**

```bash
git clone <repository-url>
cd weather-app
```

### 2. **Install Python and Dependencies**

Make sure you have **Python 3** installed. If not, download and install it from [python.org](https://www.python.org/).

Next, create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
.env\Scriptsctivate  # For Windows
```

Now, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following contents:

```
Flask==2.1.2
requests==2.26.0
```

### 3. **Obtain Your OpenWeatherMap API Key**

1. Go to [OpenWeatherMap](https://openweathermap.org/).
2. Sign up (or log in if you have an account).
3. Create a new API key by following the instructions.
4. Replace the `API_KEY` variable in `app.py` with your new API key.

### 4. **Run the Application**

After installing dependencies and updating the API key, run the Flask application:

```bash
python app.py
```

This will start the Flask development server at `http://127.0.0.1:5000`. Open this URL in your browser to access the Weather App.

### 5. **Interacting with the App**

1. Open the app in your browser.
2. Enter the name of any city in the provided input field.
3. Click **"Get Weather"** to see the current weather and forecast.
4. The app will display:
   - **Current weather:** temperature, humidity, wind speed, weather description, and an icon.
   - **Hourly forecast:** a 5-time-slot forecast with temperature, description, and wind speed.

### 6. **Stopping the Application**

To stop the Flask server, press `CTRL + C` in your terminal.

---

## **Folder Structure**

```plaintext
weather-app/
├── app.py               # Main Python application file
├── templates/           # HTML files
│   └── index.html       # Main frontend HTML
├── requirements.txt     # Python dependencies
└── README.md            # This README file
```

---

## **Detailed Description of Files**

### `app.py`

This is the main Python application file that runs the Flask web server. It contains:

- **Flask Routes:**
  - `/`: The homepage route, which renders the main form to enter the city name.
  - `/weather`: A POST request that gets the weather information from OpenWeatherMap API and displays it.

- **API Interaction:**
  - The application sends a request to OpenWeatherMap using the provided city name and API key.
  - If the API returns valid data, it is processed and passed to the frontend.

- **Error Handling:**
  - If the city is not found or the API fails, an error message is displayed.

### `index.html`

This file is the frontend of the application. It contains:

- **HTML Form:**
  - A simple input field to enter the city name and a button to submit the form.
  
- **Weather Display:**
  - If weather data is available, it displays the current weather (temperature, humidity, wind speed, description, and icon).
  - It also displays the 5-time-slot forecast for the day with relevant weather details.
  
- **Responsive Layout:**
  - Built with **Bootstrap** for a clean, responsive UI that adjusts across different screen sizes (desktop, tablet, mobile).

---

## **Improvements and Future Features**

- **Search History:**
  - Save previously searched cities and display them for easy access.

- **Advanced Forecasting:**
  - Display a more detailed forecast for multiple days or more hourly slots.

- **Error Handling Enhancements:**
  - Provide more specific error messages for users when the API fails (e.g., invalid API key, rate limit exceeded, etc.).

- **Mobile App Version:**
  - Develop a mobile version of the app or integrate it with a PWA (Progressive Web App) for offline access.

---

## **Contributing**

If you wish to contribute to the app, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

---

## **License**

This project is open-source and available under the [MIT License](LICENSE).

