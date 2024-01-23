import requests, smtplib, time
from datetime import datetime

MY_LAT = 20.671955 # Your latitude
MY_LONG = -103.416504 # Your longitude

def is_currently_dark(lat, lng):
    parameters = {
        "lat": lat,
        "lng": lng,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

def is_ISS_close(lat, lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if abs(iss_longitude-lng) <= 5 and abs(iss_latitude-lat) <= 5:
        return True
    return False

def sent_email():
    my_email = "oslovdobrov@gmail.com"
    password = "qtcndteeboeibrwn"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="oslotesting7@gmail.com",
            msg=f"Subject:ISS can be viewed\n\nLook up!, now you can see the ISS above you"
        )
        connection.close()

def main():
    if is_currently_dark(lat=MY_LAT,lng=MY_LONG) and is_ISS_close(lat=MY_LAT,lng=MY_LONG):
        sent_email()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)




#Your position is within +5 or -5 degrees of the ISS position.



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



