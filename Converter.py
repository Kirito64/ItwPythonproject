import requests

class Converter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def Convert(self, fromC, toC, amount):
        intialamount = amount
        if(fromC != 'USD'):
            intialamount = intialamount/self.currencies[fromC]
        amount = round(intialamount*self.currencies[toC], 2)
        return amount

