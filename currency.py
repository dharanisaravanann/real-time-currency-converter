def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.
    """
    try:
        return round(float(rate),4)
    except (TypeError, ValueError):
        return rate

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.
    """
    try:
        r=float(rate)
        if r ==0:
            return 0.0
        return round (1.0/r,4)
    except (TypeError, ValueError):
        return 0.0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will format the text to be displayed in the Streamlit app.
    """
    try:
        rate = float(rate)
        amount = float(amount)
    except (TypeError, ValueError):
        return "Invalid inputs for rate or amount."

    rounded_rate = round_rate(rate)              
    converted_amount = round(amount * rate, 2) # upto 2 decimals
    inverse_rate = reverse_rate(rate) #inverse per-unit rate

    return(
        f"The conversion rate on {date} from {from_currency} to {to_currency} was {rounded_rate:.2f}. "
        f"So {amount:.1f} in {from_currency} correspond to {converted_amount:.1f} in {to_currency}. " 
        f"The inverse rate was {inverse_rate:.4f}.")