# Real-Time Currency Converter Web App

## Author
Dharani Saravanan

## Description
This project is an interactive currency converter web application built using Python and Streamlit.
Exchange rate data is retrieved from the [Frankfurter API](https://www.frankfurter.app/).
This application allows users to:

- Convert currency amounts between two different currencies (SGD, AUD, USD, EUR, JPY, etc.)
- Check past conversion rates by selecting historical dates
- View the trend of rates over the last 3 years

## Features
- Convert amount between two currencies (eg. AUD, SGD, USD, EUR, JPY, etc) 
- View real-time conversion rate and inverse rate
- View historical conversion rate for a selected date
- See the rate trend over the past 3 years in a graphical format
## Challenges Faced
    - Structuring the project into multiple Python files while keeping functions compatible with the provided skeleton
    - Formatting the results correctly (conversion rate, amount, inverse rate)
    - Making the streamlit app run smoothly with user inputs
## Future Features
    - Adding additional features to support extended conversion rate trend analysis
    - Adding a download feature to generate a CSV and PDF report of the conversions and graph
    - Ability to add multiple currencies to run at the same time 

## How to Set Up

### 1. Install Python
- Python **3.11** is recommended (Python **3.10** also supported)
- Verify your Python version:
```bash
python --version
# or
python3 --version
```
## 2. Create and Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```
## 3. Upgrade pip
```bash
python -m pip install --upgrade pip
```
## 4. Install Dependencies
```bash
pip install streamlit==1.38.0 requests==2.32.3 pandas matplotlib
```
## 5. Run the Application
```bash
streamlit run app.py
```
 - The application will open automatically in your default web browser.

## Screenshots
![FX Converter UI](screenshots/ui.png)
![Live FX Conversion](screenshots/live_conversion.png)
![Historical FX Trend](screenshots/trend.png)

