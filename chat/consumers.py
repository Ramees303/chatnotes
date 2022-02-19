import json
# our application must be asynchronous
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        #async change it behaviour
 # calling it will return co-routine objects which say i can run the co-routine
        #with the arguments you called and i can also return the results
        #when you await me
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #scope defines where the variable can be accessed or referred
        #kwargs allow to pass keyword  arguments (keyword agrument:-are values that,when passed into a
        #into a function,are identifiable by specific parameter name) to a function
        #eg:- def add (a,b=5) :return (a+b)
        #we are getting url route and we are selecting the room_name from it
        self.room_group_name='chat_%s' % self.room_name
        #putting room name inside room group name ie creating a group


        #constructing a new group and that will be utilizing all the functionality
        # from the above class
        #channel layer allow to talk between different instance of an application
        #instance is an object that belongs to  a class
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
            #channel_name contain a pointer to the channel layer instance and
            #channel_name that will reach the consumer ie it allow to reiterate (repeat)
        )



        await self.accept()
        # for accepting  the connection is need for ws for work
        #after accepting only we can send messages



        #sending message to group
        # await self.channel_layer.group_send(
        #     self.room_group_name, #sending message inside  groups
        #     # for knowing which group to snd we use room_group_name
        #     { #defining what message to snd
        #         'type' : 'tester_message', #key value
        #         'tester' : 'hello world',
        #     }
        # )
        #
        #
        # async def tester_message(self,event): #the function name is same
        #     #as type
        #     tester = event['tester'] #collecting the data
        #
        #     #sending data across through websocket
        #     #json-dumps to create new key value
        #     await self.send(text_data=json.dumps({
        #         'tester': tester,
        #     }))



            #receiving the data and pass as text_data
    async def receive(self, text_data=None, bytes_data=None):
  #text data is the json string
        text_data_jason=json.loads(text_data)
            #loads method is used to parse a valid jason string into python dictionary
            #taking  the data from text_data and put it in  text_data_jason
        message = text_data_jason['message']
           # username = text_data_jason['username']
            #we put it inside  message

        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':json.dumps(message),
                    #'username':username,
                }
            )
    async def chat_room(self,event):


        message = event['message']
               # username = event['username']

        await self.send(json.dumps(
                    {
                        'message':message,
                        #'username':username,
                    }
            #json dumps -converting to json
                ))


    async def disconnect(self,close_code):


        await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
                #discard(removing) room_group_name,channel_name for
                #disconnecting the chat
            )








