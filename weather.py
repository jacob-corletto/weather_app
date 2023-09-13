import json
import calendar

def read_data(filename):
  try:
    with open(filename,'r') as f:
      return json.load(f)
  
  except FileNotFoundError:

    print('file not found')
    return {}

def write_data(data, filename):
  with open(filename, "w") as outfile:
    json.dump(data, outfile)

def max_temperature(date,data):
  max = -100000

  for i in data.keys():
    if i[0:8] == date[0:8]:
      if data[i]['t'] > max:
        max = data[i]['t']

  return max

def min_temperature(date,data):
  min = 100000

  for i in data:
    if i[0:8] == date[0:8]:
      if data[i]['t'] < min:
        min = data[i]['t']

  return min

def min_humidity(date,data):
  min = 100000

  for i in data:
    if  i[0:8] == date[0:8]:
      if data[i]['h'] < min:
        min = data[i]['h']

  return min

def max_humidity(date,data):
  max = -100000

  for i in data.keys():
    if  i[0:8] == date[0:8]:
      if data[i]['h'] > max:
        max = data[i]['h']

  return max

def tot_rain(date,data):
  total = 0

  for i in data.keys():
    if i[0:8] == date[0:8]:
      total += data[i]['r']

  return total

def report_daily(date,data):
  temp = ""
  hum = ''
  rain = ''
  output = ''
  output+= f'========================= DAILY REPORT ======================== \nDate                     Time Temperature Humidity Rainfall \n==================== ======== =========== ======== ======== \n'
  for i in data.keys():
    if i[0:8] == date:
      temp = data[i]['t']
      hum = data[i]['h']
      rain = data[i]['r']
      month= calendar.month_abbr[int(date[4:6])]
      day = i[6:8]
      year = i[0:4]
      time = i[8:10]+":"+i[10:12]+":"+i[12:14]
      
      output += f'{month},{day},{year:13} {time}'
      output += f'{temp:12}{hum:9}{rain:9}\n'

  return output

def report_historical(data):
  temp = ""
  hum = ''
  rain = ''
  date = ''
  output = "============================== HISTORICAL REPORT =========================== \n                     Minimum     Maximum"
  output += "     Minumum  Maximum  Total\n"
  output += "Date                 Temperature Temperature Humidity Humidity Rainfall\n==================== =========== =========== ======== ======== ========\n"

  for i in data.keys():
    if i[0:8] == date:
      continue
    else:
      date = i[0:8]
      month = calendar.month_abbr[int(date[4:6])]
      day = date[6:8]
      year = date[0:4]
      output+= f'{month} {day} {year}'

      mintemp = min_temperature(i,data)
      maxtemp = max_temperature(date,data)
      minhum = min_humidity(date,data)
      maxhum = max_humidity(date,data)
      totrain = tot_rain(date,data)
      output+= f'{mintemp:21}{maxtemp:12}{minhum:9}{maxhum:9}{totrain:9}\n'
  return output
#       return (f"========================= DAILY REPORT ======================== \n
#       Date Time Temperature Humidity Rainfall
# ==================== ======== =========== ======== ========{date[0:8]}\n{max_temp}\n {min_temp}\n {max_hum}\n {min_hum}\n {tot_r}\n")

