from helps.common.m_atto import Attohelps

class Femtohelps(Attohelps):
   def generateUniqueCode(self, pattern):
      # CMPTP-20240114123559618137
      return f'{pattern}-{self.getUniqueCodePattern()}'