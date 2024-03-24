from datetime import datetime, date
import pytz

def convert_time(input_time, input_tz, target_tz):
    """
    Convert time from input time zone to target time zone.
    
    Args:
        input_time (str): Input time in HH:MM format (e.g., '08:00 PM').
        input_tz (str): Input time zone (e.g., 'Asia/Karachi').
        target_tz (str): Target time zone (e.g., 'America/New_York').
    
    Returns:
        tuple: Tuple containing:
            1. str: Formatted input date (formatted as '%d-%m-%Y').
            2. str: Converted time in target time zone (formatted as '%d-%m-%Y %H:%M:%S %Z').
    """
    # Get the current date
    input_date = date.today()

    # Parse input datetime string to datetime object
    input_datetime = datetime.strptime("{} {}".format(input_date, input_time), '%Y-%m-%d %I:%M %p')

    # Create timezone objects for input and target timezones
    input_timezone = pytz.timezone(input_tz)
    target_timezone = pytz.timezone(target_tz)

    # Localize input datetime to input timezone
    localized_input_datetime = input_timezone.localize(input_datetime)

    # Convert localized input datetime to target timezone
    converted_datetime = localized_input_datetime.astimezone(target_timezone)

    # Format the input date and converted datetime as strings
    formatted_date = input_date.strftime('%d-%m-%Y')
    formatted_time = converted_datetime.strftime('%d-%m-%Y %H:%M:%S %Z')

    # Return the formatted input date and converted time
    return formatted_date, formatted_time

# Example usage
if __name__ == "__main__":
    # Define input time, input timezone, and target timezone
    input_time = '08:00 PM'
    input_timezone = 'Asia/Karachi'
    target_timezone = 'America/New_York'
    # Call the convert_time function to convert time
    formatted_date, converted_time = convert_time(input_time, input_timezone, target_timezone)

# Print the converted time with input date
print("Converted time from {} {} {} to {}: {}".format(formatted_date, input_time, input_timezone, target_timezone, converted_time))
