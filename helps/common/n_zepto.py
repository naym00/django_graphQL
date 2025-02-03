
from datetime import datetime, date, timedelta
import calendar
import json
import os

class Zeptohelps:

   def getUniqueCodePattern(self):
      return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]

   def conv_to_date(self, convert_date):
      return_date = None
      if isinstance(convert_date, str):
         try: return_date = datetime.strptime(convert_date, '%Y-%m-%d').date()
         except: pass
      else:
         if isinstance(convert_date, date): return_date = convert_date
      return return_date
   
   def getToday_Now(self):
      return datetime.now()
    
   def getToday(self):
      return date.today()
   
   def days_in_a_year(self, conv_to_date):
      days = 365
      try:
         year = conv_to_date.year
         if calendar.isleap(year): days = 366
      except: pass
      return days
   
   def days_in_a_month(self, year, month):
      days = 30
      try:
         _, days = calendar.monthrange(year, month)
      except: pass
      return days
   
   def save_file(self, path, data):
      with open(path, 'w') as outfile:
         outfile.write(json.dumps(data, indent=4))
   
   def read_file(self, path):
      with open(path, 'r') as file:
         data = json.load(file)
      return data
   
   def remove_file(self, path):
      flag = True
      try: os.remove(path)
      except: flag = False
      return flag