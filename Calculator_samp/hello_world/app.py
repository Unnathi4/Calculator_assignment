import json



def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    def sum():
        return number1 + number2
    def product():
        return number1 * number2
    def difference():
        return abs(number1 - number2)
    def quotient():
        return number1 / number2
    
