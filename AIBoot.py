import pywhatkit as kit
import datetime

# Get current time
now = datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute

# Add 1 minute to the current time
send_hour = current_hour
send_minute = current_minute + 1

# Adjust if minutes exceed 59
if send_minute >= 60:
    send_minute -= 60
    send_hour += 1

# Send the message
kit.sendwhatmsg("+917666473300", "Hello, this is an automated message!", send_hour, send_minute)
kit.sendwhatmsg("+918485058284", "Hello, this is an automated message!", send_hour, send_minute)