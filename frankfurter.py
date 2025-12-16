from api import get_url
import json
import datetime

base_url= "https://api.frankfurter.app"

def _load_json(status: int, text: str):
    if status != 200:
        return None
    try:
        return json.loads(text)
    except Exception:
        return None
    
#currencies
def get_currencies_list():
    """
    Calls Frankfurter API to get list of available currencies.
    Returns a list of codes (e.g., ['USD','EUR',...]) or None if error.
    """
    status, text = get_url(f"{base_url}/currencies")
    data = _load_json(status, text)
    if data is None:
        return None
    return sorted(list(data.keys()))

def get_latest_rates(from_currency, to_currency, amount):
    """
    Calls Frankfurter API to get latest FX conversion rate for given currencies.
    Returns (date, rate) or (None, None) if error.
    """
    url = f"{base_url}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    status, text = get_url(url)
    data= _load_json(status, text)
    if data is None:
        return None, None

#converted amount
    try:
        date = data.get("date")
        converted_amount = list(data["rates"].values())[0]
        rate_per_unit = float(converted_amount) / float(amount) if amount else None
        if rate_per_unit is None:
            return None, None
        return date, rate_per_unit
    except Exception:
        return None, None
    
def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Calls Frankfurter API to get FX conversion rate for a given date.
    Returns rate or None if error.
    """
    url = f"{base_url}/{from_date}?amount={amount}&from={from_currency}&to={to_currency}"
    status, text = get_url(url)
    data = _load_json(status, text)
    if data is None:
        return None

    try:
        converted_amount = list(data["rates"].values())[0]
        rate_per_unit = float(converted_amount) / float(amount) if amount else None
        return rate_per_unit
    except Exception:
        return None

def get_rate_trend(from_currency: str, to_currency: str, years: int)-> dict:
    """
    Fetches historical rates for the past N years on a quarterly basis.
    Returns a dict {date: rate}.
    """
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=years*365)

    url = f"{base_url}/{start_date}..{today}?from={from_currency}&to={to_currency}"
    status, text = get_url(url)
    data = _load_json(status, text)
    if data is None:
        return {}
    return data.get("rates", {})




