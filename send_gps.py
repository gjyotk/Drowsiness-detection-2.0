import os
import vonage 
import geocoder

def send_gps_coordinates():
    coordinates = geocoder.ip('IP_ADDRESS')
    if coordinates:

        #extract coordinates from ip address
        message = f"My current GPS coordinates are: \n"+str(coordinates.latlng[0])+"\n"+str(coordinates.latlng[1])+"\n"
        print(message)

        #setup 
        client = vonage.Client(key='KEY_VONAGE', secret='SECRET_VONAGE')
        sms = vonage.Sms(client)

        try:
            responseData = sms.send_message(
                {
                        "from": "Vonage APIs",
                        "to": "CONTACT",
                        "text": message,
                }
            )
            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")
    else:
        print("Unable to retrieve GPS coordinates.")

sender_name = "NAME"
recipient_number = "CONTACT"

if not 'KEY_VONAGE' or not 'SECRET_VONAGE':
    print("Vonage API credentials not set. Please set them in your environment variables.")
else:
    send_gps_coordinates()
