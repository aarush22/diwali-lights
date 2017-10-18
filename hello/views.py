from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import paho.mqtt.client as mqtt
#import urlparse

topic = '/lights'

# Define event callbacks
def on_publish(client, obj, mid):
    print("mid: " + str(mid))
'''
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)
'''

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def on(request):

    global topic
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_publish = on_publish
    '''
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    '''

    mqttc.username_pw_set("dfxukbgb", "lq_IHyYetOBV")
    mqttc.connect("m20.cloudmqtt.com", 14917)

    mqttc.publish(topic, "on")
    return render(request, 'on.html')

def off(request):

    global topic
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_publish = on_publish
    '''
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    '''

    mqttc.username_pw_set("dfxukbgb", "lq_IHyYetOBV")
    mqttc.connect("m20.cloudmqtt.com", 14917) #"24917")

    mqttc.publish(topic, "off")
    return render(request, 'off.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
