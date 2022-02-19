#it is same as urls file in setting
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
'This is used to find who is the user and  his  message in chatroom'
'it is also  used for login '
from channels.routing import ProtocolTypeRouter,URLRouter
'It is for using  routing'
import chat.routing

'When we get a ws request this is where to route it'
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        #'used for authentication'
        URLRouter(
            #for routing our url
            chat.routing.websocket_urlpatterns
            #we are connecting to the websocket url_pattern in routing
            #inside chat app
        )
    ),

})






