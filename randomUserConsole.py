from client import Client

def generateUser():

    client = Client()
    data = client.getData()
    print("NAME: " +data['name'])
    print("GENDER: "+data['gender'])
    print("USERNAME: "+data['username'])
    print("PASSWORD: "+data['password'])
    print("IMAGE: "+data['image_thumbnail'])
    print("EMAIL: "+data['email'])

while True:

    ask = input("Generate User? yY/nN?: ")

    if ask.lower == "y" or ask == "y":
        generateUser()
    else:
        break