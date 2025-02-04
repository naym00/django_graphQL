from helps.common.m_atto import Attohelps

class Femtohelps(Attohelps):
   def generateUniqueCode(self, pattern):
      # CMPTP-20240114123559618137
      return f'{pattern}-{self.getUniqueCodePattern()}'
   
   def validate_values(self, value, type, error_message):
      invalid_messages = self.validation_messages()
      
      if type == 'email':
         is_valid = self.check_valid_email(value)
         if not is_valid:
            error_message.append(f"{invalid_messages[type]['message']} (Format: {', '.join(invalid_messages[type]['example'])})")