from mebo.mebo import Mebo
# replace with IP of your mebo. You can probably get it from your router. Autodiscovery is coming
m = Mebo(ip='192.219.13.81')
# supported directions ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw',)
# velocity is how fast the wheels turn (yes, it's technically speed, but originally I had a sign on velocity.
# Then I discovered that there were cardinal direction api calls and had to change it
while(1):
    m.move('n', speed=255, duration=1000)
    time.sleep(20)
# dur is the value taken by the API. I'll clean it up soon - values < 1000 ms don't work
m.claw.open(dur=1000)