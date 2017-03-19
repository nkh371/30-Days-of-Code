  def computeDifference(self):
          size = len(self.__elements)
          self.maximumDifference = 0
          for i in range(1, size):
              for j in range(0 , i ):
                  a = abs(self.__elements[j] - self.__elements[i])
                  if self.maximumDifference < a:
                      self.maximumDifference = a
