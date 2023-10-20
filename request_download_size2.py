
import requests



inputDictionary = {'gdrive': 'https://drive.google.com/file/d/1Ew7rQT0VNBqJW1AUrOrOP2IJKSJS7Uoy/view?usp=sharing'}
#print(inputDictionary['Hello'])

print(inputDictionary.values())
liste = list(inputDictionary.values())
print(liste[0])


response = requests.head(liste[0])
print(type(response.headers))
print(response.headers['Content-Length'])
