from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
import requests
from mobApi.models import PushNotification
from userauths.models import UserToken
from channels.generic.websocket import WebsocketConsumer
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

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
            auth_response = self.authenticate_user(email, password,csrf_token)
            if 'token' in auth_response:
                self.send(text_data=json.dumps({
                    'type': 'authentication',
                    'message': 'Authentication successful',
                    'token': auth_response['token']  # Send token to client
                }))
            else:
                self.send(text_data=json.dumps({
                    'type': 'authentication',
                    'error': 'Authentication failed'
                }))
          
          
          
          
          
          
          
          
          
          
          
          
            # Perform authentication via POST request with CSRF token
            # auth_response = self.authenticate_user(email, password, csrf_token)
            # if auth_response:
            #     self.send(text_data=json.dumps({
            #         'type': 'authentication',
            #         'message': 'Authentication successful'
            #     }))
            # else:
            #     self.send(text_data=json.dumps({
            #         'type': 'authentication',
            #         'error': 'Authentication failed'
            #     }))
        elif action == 'logout':
            email = text_data_json.get('email')

            csrf_token = text_data_json.get('csrf_token')  # Get CSRF token
            # Perform logout via POST request with CSRF token
            print(csrf_token)

            logout_response = self.logout_user(csrf_token,email)
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
        elif action == 'register':
            # Handle register action
            username = text_data_json.get("username")
            email = text_data_json.get('email')
            password = text_data_json.get('password')
            csrf_token = text_data_json.get('csrf_token')
            register_response = self.register_user(email, username, password,  csrf_token)
            self.send(text_data=json.dumps(register_response))
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

    # def authenticate_user(self, email, password, csrf_token):
    #     # Make authentication POST request with CSRF token included as a cookie
    #     authentication_url = 'http://192.168.1.11:8080/mobApi/login_user_mob/'
    #     headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
    #     response = requests.post(authentication_url, data={'email': email, 'password': password}, headers=headers)
    #     return response.ok
    def authenticate_user(self, email, password,csrf_token):
        # Make authentication POST request with email and password
        headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
        authentication_url = 'http://192.168.1.7:8080/mobApi/login_user_mob/'
        response = requests.post(authentication_url, data={'email': email, 'password': password}, headers=headers)
        if response.status_code == 200:
            return response.json()  # Assuming the response contains the user token
        else:
            return {'error': 'Authentication failed'}

    def logout_user(self, csrf_token,email):
        # Make logout POST request with CSRF token included as a cookie
        logout_url = 'http://192.168.1.7:8080/mobApi/logout_mob/'
        headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
        
        response = requests.post(logout_url,data={"email":email}, headers=headers)
        return response.ok
    def register_user(self,  email, username, password,  csrf_token):
        headers = {'X-CSRFToken': csrf_token, 'Cookie': f'csrftoken={csrf_token}'}
        register_url = 'http://192.168.1.7:8080/mobApi/register_user_mob/'
        response = requests.post(register_url, data={"username":username,'email': email, 'password': password}, headers=headers)
        if response.status_code == 200:
            return response.json()  # Assuming the response contains the user token
        else:
            return response.json()



class PushNotificationConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer = get_channel_layer()

    def connect(self):
        user_token = self.scope['url_route']['kwargs']['user_token']
        user_token_exists = UserToken.objects.filter(token=user_token).exists()

        if user_token_exists:
            self.room_group_name = str(user_token)

            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            # Accept the connection
            self.accept()
            push_notifications = PushNotification.objects.filter(token_value=user_token)
            print(list(push_notifications.values()))

            if push_notifications.exists():
                self.send(text_data=json.dumps(list(push_notifications.values())))

        else:
            # Reject the connection
            self.close()

    def receive(self, text_data):
        pass

    def send_notification(self, event):
        message = event['message']
        self.send(text_data=message)

@receiver(post_save, sender=PushNotification)
def push_notification_handler(sender, instance, created, **kwargs):
    if created:
        # data =  list(instance.objects.filter(token_value=instance.token_value).values())
        # print(data);
        # print(json.dumps(list(instance.values())))
        user_token = instance.token_value
        dict = {
            'id':instance.id,
            'message':instance.message
        }
        group_name = str(user_token)
        async_to_sync(get_channel_layer().group_send)(
            group_name,
            {
                'type': 'send_notification',
                'message': json.dumps(dict)
            }
        )






# class PushNotificationClass(WebsocketConsumer):
#     def connect(self):
#         user_token = self.scope['url_route']['kwargs']['user_token']
#         user_token_exists = UserToken.objects.filter(token=user_token).exists()

#         if user_token_exists:
#             self.room_group_name = str(user_token)

#             async_to_sync(self.channel_layer.group_add)(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             # Accept the connection
#             self.accept()
#             push_notifications = PushNotification.objects.filter(token_value=user_token)
#             print(list(push_notifications.values()))

#             if push_notifications.exists():
#                 self.send(text_data=json.dumps(list(push_notifications.values())))

#         else:
#             # Reject the connection
#             self.close()

#     def receive(self, text_data):
#         pass


# @receiver(post_save, sender=PushNotification)
# def push_notification_handler(sender, instance, created, **kwargs):
#     if created:
#         user_token = instance.token_value
#         group_name = str(user_token)
#         async_to_sync(PushNotificationClass.channel_layer.group_send)(
            
#             group_name,
#             {
#                 'type': 'send_notification',
#                 'message': json.dumps(instance.to_dict())
#             }
#         )


# class PushNotificationClass(WebsocketConsumer):
#     def connect(self):
#         user_token = self.scope['url_route']['kwargs']['user_token']
#         user_token_exists = UserToken.objects.filter(token=user_token).exists()

#         if user_token_exists:
#             self.room_group_name = str(user_token)

#             async_to_sync(self.channel_layer.group_add)(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             # Accept the connection
#             self.accept()
#             push_notifications = PushNotification.objects.filter(token_value=user_token)
#             print(list(push_notifications.values()))

#             if push_notifications.exists():
#                 self.send(text_data=json.dumps(list(push_notifications.values())))

#         else:
#             # Reject the connection
#             self.close()

#     def receive(self, text_data):
#         pass

#     def send_notification(self, event):
#         message = event['message']
#         self.send(text_data=message)





































# class PushNotificationClass(WebsocketConsumer):
#     def connect(self):
#         user_token = self.scope['url_route']['kwargs']['user_token']
#         user_token_exists = UserToken.objects.filter(token=user_token).exists()

       
#         if user_token_exists:
#             user_token_obj = UserToken.objects.filter(token=user_token).first()
#             self.room_group_name = str(user_token)

#             async_to_sync(self.channel_layer.group_add)(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             # Accept the connection
#             self.accept()
#             push_notifications = PushNotification.objects.filter(token_value=user_token)

#             print(list(push_notifications.values()))

#             if push_notifications.exists():
#                 self.send(text_data=json.dumps(list(push_notifications.values())));            

#         else:
#             # Reject the connection
#             self.close()
#     def receive(self, text_data):        
#         pass

    

