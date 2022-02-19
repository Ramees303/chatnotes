#it is same as urls in chat
from django.urls import re_path
'sometimes regular path doesnt meet our required ,'
'so we use advanced path'

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer.as_asgi()),
    # url location:-ws/chat
    #(?P<room_name>\w+):-capture the name of room
    # ie similar to room_name in urls.py
   #similar to views.room in chat.urls
    #w+:-anything after the chat/ is recongized and pickup for the room_name
    #it takes lower and upper ,alphabet,numbers etc
    #$:-after room_name/ it doesnt take it
]








