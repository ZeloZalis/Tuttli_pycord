import requests
import datetime

def create_access_token(client_id, client_secret, region="us"):
    data = {'grant_type': 'client_credentials'}
    response = requests.post(
        'https://%s.battle.net/oauth/token' % region,
        data=data,
        auth=(client_id, client_secret)
    )
    return response.json()

eng_to_esp = {
    "days" : {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    },
    "months":{
        'January': 'enero',
        'February': 'febrero',
        'March': 'marzo',
        'April': 'abril',
        'May': 'mayo',
        'June': 'junio',
        'July': 'julio',
        'August': 'agosto',
        'September': 'septiembre',
        'October': 'octubre',
        'November': 'noviembre',
        'December': 'diciembre'
    }
}
mitoken = "US1mOj40w6n4xAVLaeyLzFdj6tHls3Q8Pu"
response = create_access_token("8aeaab33a28345fcbad773eed36ffd94", "wjQsDrt7XkJunDrTa6oF9qz5krPh1Q1i")
# print(response)
try:
    dataUS = requests.get(f"https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US&access_token={response['access_token']}")
    infoUS = dataUS.json()

    dataEU = requests.get("https://EU.api.blizzard.com/data/wow/token/index?namespace=dynamic-eu&locale=en_US&access_token=US1mOj40w6n4xAVLaeyLzFdj6tHls3Q8Pu")
    infoEU = dataEU.json()
    timestamp = infoUS['last_updated_timestamp'] / 1000
    date = datetime.datetime.fromtimestamp(timestamp)
    fecha = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    fecha_formateada = fecha.strftime('%A, %d de %B de %Y, %I:%M:%S %p')
    for eng, esp in eng_to_esp["days"].items():
        fecha_formateada = fecha_formateada.replace(eng, esp)
    for eng, esp in eng_to_esp["months"].items():
        fecha_formateada = fecha_formateada.replace(eng, esp)
    fecha_formateada = fecha_formateada.replace('AM', 'a.m.').replace('PM', 'p.m.')
    # print(fecha_formateada)
    # print(f"Precio en US: {infoUS['price']/10**7}")
    # print(response['access_token'])
    # print(f"Precio en EU: {infoEU}\nInformación recibida el: {date}")
    # print(str(date))
except Exception as e:
    print(f"Error: {e}")

#  https://us.api.blizzard.com/data/wow/US1mOj40w6n4xAVLaeyLzFdj6tHls3Q8Pu/index
