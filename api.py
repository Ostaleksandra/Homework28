import requests

class CreateToken:

    def __init__(self):
        self.url = "https://restful-booker.herokuapp.com/auth"

    def create_auth_token():

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'username': 'admin',
            'password': 'password123'
        }

        res = requests.post(self.url, headers=headers, data=data)
        result = AuthToken(**res, json())
        status = res.status_code
        return result.token, status

create_token = CreateToken()

class CreateBooking:

    def __init__(self):
        self.url = "https://restful-booker.herokuapp.com/booking"

    def create_booking(create_auth_token):

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'firstname': 'Jim',
            'lastname': 'Brown',
            'totalprice': 111,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2018-01-01',
                'checkout': '2019-01-01'
            },
            'additionalneeds': 'Breakfast'
        }

        return requests.post(self.url, headers=headers, data=data)

create_booking = CreateBooking()