import requests,pyfiglet,os

api_key='360e4bc3865e745ec844bd7ec054ca11'
city="kochi"
choice="y"
while choice=="y":
    ascii_banner = pyfiglet.figlet_format("Open Weather",font="digital")
    print(ascii_banner)
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)
    data=response.json()
    print("City:",city)
    print('')
    print("Weather:",data['weather'][0]['description'])
    print(" ")
    print("Temperature")
    print("*"*12)
    print("Temperature: ",data['main']['temp'])
    print("Maximum Temperature: ",data['main']['temp_max'])
    print("Minimum Temperature: ",data['main']['temp_min'])
    print('')
    choice=input("Do you want to continue or not y or n: ")
    print('')
    if choice=='y':
        city=input("Enter your city: ")
        os.system('clear')
    else:
        print("Thank you for visiting Open Weather")
        break

