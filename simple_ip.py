from djitellopy import Tello

tello = Tello(host='192.168.0.101')

tello.takeoff()

tello.land()

tello.end()