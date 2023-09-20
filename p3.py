# import matplotlib as mp
from matplotlib import pyplot as plt
name = ["Vasu", "Saksham", "Nancy", "Tushar"]
age = [20, 21, 2, 200]
# a = plt.bar(range(len(name)),age)
# b = plt.show()
plt.ylabel('age')
plt.xlabel('names')
plt.title('Friends')
plt.bar(name,age)
plt.show()