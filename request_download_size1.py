import requests
response = requests.head('https://drive.google.com/file/d/1C9Q5qU_Wu_gj78H5G3TT2thGA-hKheVf/view?usp=drive_link')
print(type(response.headers))
print(response.headers['Content-Length'])