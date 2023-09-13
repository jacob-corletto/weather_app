from weather import *
data = {}
filename = 'w.dat'

while True:
  print('*** TUFFY TITAN WEATHER LOGGER MAIN MENU')
  print('1. Set data filename\n')
  print('2. Add weather data\n')
  print('3. Print daily report\n')
  print('4. Print historical report\n')
  print('9. Exit the program\n')

  choice = int(input('enter menue choice: '))

  if (choice ==1):
    filename = str(input('enter filename: '))
    data = read_data(filename)

  elif (choice ==2):
    date = input('Enter date (YYYYMMDD): ')
    time = input('Enter time (hhmmss): ')
    temp = int(input('Enter temperature: '))
    hum = int(input('Enter humidity: '))
    rain = int(input('Enter rainfall: '))

    data[date+time] = {"t": temp, "h": hum, "r": rain}
    write_data(data,filename)

  elif (choice ==3):
    date = input('Enter date (YYYYMMDD): ')
    print(report_daily(date,data))

  elif (choice ==4):
    print(report_historical(data))

  elif (choice ==9):
    break

  else:
    print('not valid index')