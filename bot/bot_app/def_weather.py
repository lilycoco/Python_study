import requests

# r = requests.get('http://book.impress.co.jp/')
# print(r.status_code)

def weather_command():
  base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
  city_code = '130010'
  url = '{}?city={}'.format(base_url, city_code)
  r = requests.get(url)
  weather_data = r.json()
  city = weather_data['location']['city']
  label = weather_data['forecasts'][0]['dateLabel']
  telop = weather_data['forecasts'][0]['telop']

  response = '{}{}の天気は{}'.format(city, label, telop)
  return response

