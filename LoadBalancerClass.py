

from DataSets import DataSets


class LoadBalancerItemCl:
  def __init__(self, code, value):
    self.code= code
    self.value = value

#incijalizovati listu koju dobijemo iz writera u ovo listItem

class LoadBalancerDescriptionCl:
      def __init__(self, id, listItem, DataSets):
            self.id = id
            self.list = listItem()
            self.dataSet = DataSets

#i fali lista descriptiona




lb1 = LoadBalancerItemCl("ANALOG", 23)

print(lb1.code)
print(lb1.value)