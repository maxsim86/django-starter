from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import json
from .models import *

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
    self.user = self.scope['user']
    self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name'] 
    self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
    self.accept()