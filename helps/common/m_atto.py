from helps.common.n_zepto import Zeptohelps
from datetime import datetime, date, timedelta

class Attohelps(Zeptohelps):
   def checkValidDate(self, year, month, date):
      flag = True
      try: datetime(year, month, date, 10, 10, 10)
      except: flag = False
      return flag
   
   def checkValidTime(self, hour, minute, second):
      flag = True
      try: datetime(2024, 5, 5, hour, minute, second)
      except: flag = False
      return flag

   def is_date_in_range(self, date_to_compare, start_date, end_date):
        flag = False
        date_to_compare = self.conv_to_date(date_to_compare)
        start_date = self.conv_to_date(start_date)
        end_date = self.conv_to_date(end_date)
        if date_to_compare != None and start_date != None and end_date != None: flag = True
        return flag
   
   def convert_STR_y_m_d_h_m_s_Dateformat(self, date_time):
      return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

   def convertDateformat_STR_y_m_d(self, date):
      return date.strftime('%Y-%m-%d')
    
   def convertTimeformat_STR_h_m_s(self, time):
      return time.strftime('%H:%M:%S')
   
   def convert_STRtime_Dateformat(self, strtime):
      return datetime.strptime(strtime, '%H:%M:%S').time()
   
   def getDuration(self, from_datetime, to_datetime, hour=False, minute=False):
      calulate_duration = (to_datetime - from_datetime).total_seconds()
      if hour: calulate_duration /= 3600
      elif minute: calulate_duration /= 60
      return calulate_duration
   
   def checkValidDateTime(self, year, month, date, hour, minute, second):
      flag = True
      try: datetime(year, month, date, hour, minute, second)
      except: flag = False
      return flag
   
   def convert_Date_to_month(self, convert_date):
      month_of_date = None
      convert_date = self.conv_to_date(convert_date)
      if convert_date != None: month_of_date = convert_date.strftime('%B')
      return month_of_date
    
   def convert_y_m_d_STR_day(self, convert_date):
      day_of_date = None
      convert_date = self.conv_to_date(convert_date)
      if convert_date != None: day_of_date = convert_date.strftime('%A')
      return day_of_date
   
   def getYear(self, target_date=None):
      method_date = date.today()
      if target_date != None:
         target_date = self.conv_to_date(target_date)
         if target_date != None: method_date = target_date
      return method_date.year
   
   def getMonth(self, target_date=None):
      method_date = date.today()
      if target_date != None:
         target_date = self.conv_to_date(target_date)
         if target_date != None: method_date = target_date
      return method_date.month
   
   def getDay(self, target_date=None):
      method_date = date.today()
      if target_date != None:
         target_date = self.conv_to_date(target_date)
         if target_date != None: method_date = target_date
      return method_date.day
   
   def get_year_month_day(self, target_date=None):
      method_date = date.today()
      if target_date != None:
         target_date = self.conv_to_date(target_date)
         if target_date != None: method_date = target_date
      return method_date.year, method_date.month, method_date.day