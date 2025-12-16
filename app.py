import streamlit as st
import datetime
import pandas as pd

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output
from api import get_url


#title of app
st.title ("FX Converter")

#currency dropdown menu
currencies=get_currencies_list()
# to handle error if API fails
if currencies is None:
    st.error("Failed to load currency list. Please try again later.")
    st.stop()

#user inputs
amount = st.number_input("Enter the amount to be converted:", value=80.0, step=1.0)
from_currency = st.selectbox("From Currency:", options=currencies)
to_currency = st.selectbox("To Currency:", options=currencies)

#latest rate button
if st.button("Get Latest Rate", key="latest"):
    date, rate_per_unit = get_latest_rates(from_currency, to_currency, amount)
    if not date or rate_per_unit is None:
        st.error("Could not fetch latest rate.")
    else:
        st.write(format_output(date, from_currency, to_currency, rate_per_unit, amount))


#date and historical rate button
hist_date = st.date_input("Select a date for historical rates")
if st.button("Conversion Rate", key="hist"):
    date_str = hist_date.isoformat()
    rate_per_unit = get_historical_rate(from_currency, to_currency, date_str, amount)
    if rate_per_unit is None:
        st.error("Could not fetch historical rate.")
    else:
        st.write(format_output(date_str, from_currency, to_currency, rate_per_unit, amount))

    #add chart over last 3 years 
    st.subheader("Rate Trend Over the Last 3 years")

    today=datetime.date.today()
    three_years_ago=today-datetime.timedelta(days=3*365)
    endpoint = f"/{three_years_ago.strftime('%Y-%m-%d')}..{today}?from={from_currency}&to={to_currency}"
    url = f"https://api.frankfurter.app{endpoint}"
    status, text = get_url(url)
    if status == 200:
            import json
            trend_data = json.loads(text)
            df = pd.DataFrame(trend_data["rates"]).T
            df.index = pd.to_datetime(df.index)
            df.columns = [to_currency]
            st.line_chart(df)
    else:
            st.error("Could not fetch trend data.")
    
   

