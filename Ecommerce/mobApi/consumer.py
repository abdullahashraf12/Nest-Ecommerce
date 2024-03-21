from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
import requests

class Authentication(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == 'login':
            email = text_data_json.get('email')
            password = text_data_json.get('password')
            csrf_token = text_data_json.get('csrf_token')  # Get CSRF token
            # Perform authentication via POST request with CSRF token
            auth_response = self.authenticate_user(email, password, csrf_token)
            if auth_response:
                self.send(text_data=json.dumps({
                    'type': 'authentication',
                    'message': 'Authentication successful'
                }))
            else:
                self.send(text_data=json.dumps({
                    'type': 'authentication',
                    'error': 'Authentication failed'
                }))
        elif action == 'logout':
            csrf_token = text_data_json.get('csrf_token')  # Get CSRF token
            # Perform logout via POST request with CSRF token
            print(csrf_token)

            logout_response = self.logout_user(csrf_token)
            print(logout_response)
            if logout_response:
                self.send(text_data=json.dumps({
                    'type': 'logout',
                    'message': 'Logout successful'
                }))
            else:
                self.send(text_data=json.dumps({
                    'type': 'logout',
                    'error': 'Logout failed'
                }))
        else:
            message = text_data_json.get('message')
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

    def authenticate_user(self, email, password, csrf_token):
        # Make authentication POST request with CSRF token included as a cookie
        authentication_url = 'http://192.168.1.11:8080/mobApi/login_user_mob/'
        headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
        response = requests.post(authentication_url, data={'email': email, 'password': password}, headers=headers)
        return response.ok

    def logout_user(self, csrf_token):
        # Make logout POST request with CSRF token included as a cookie
        logout_url = 'http://192.168.1.11:8080/mobApi/logout_mob/'
        headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
        response = requests.post(logout_url, headers=headers)
        return response.ok
