from random import randint, choice
from time import sleep
#from sense_emu import SenseHat
from sense_hat import SenseHat
sense = SenseHat()

sense.clear()
cl_y = (255, 255, 0)
cl_yl = (100, 100, 0)
cl_yv= (55, 55, 0)
cl_m = (0,255,255)
cl_ml = (0,100, 100)
cl_mv = (0,55,55)
cl_i = (255,0,255)
cl_il = (100,0,100)
cl_iv = (55,0,55)
cl_s = (0,0,255)
cl_sl = (0,0,120)
cl_sv = (0,0, 55)
cl_g = (0,255,0)
cl_gl = (0,105,0)
cl_gv = (0,55,0)
cl_r = (255, 0,0)
cl_rl = (155, 0,0)
cl_rv = (55, 0,0)
cl_w = (255, 255, 255)
cl_wl = (105, 105, 105)
cl_wv = (55, 55,55)
cl_b = (0, 0,0)

#sense.show_message("dzien dobry Mrusiu", scroll_speed=0.02, text_colour=g, back_colour = s)
#sense.show_message(":)", scroll_speed=0.1, text_colour=w, back_colour = b)
#SenseHat().show_message(":)", scroll_speed=0.1, text_colour=w, back_colour = b)

#Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

def Bright(bri):
    bri+=1
    if bri>2:
        bri=1


def CalcAlt(lQNH, lPress, lTemp):
    if lPress == 0:
        return 0
    if lQNH == lPress:
        return 0
    return ((pow((lQNH / lPress), 1/5.257) - 1.0) * (lTemp + 273.15)) / 0.0065

print (CalcAlt (100,100,50))

sleep(1)
sense.clear()
i=0
while i<500:
    i+=1
    px=randint(0, 7)
    py=randint(0, 7)
    sense.set_pixel(px, py, pick_random_colour())
    sleep(0.01)

# Set up where each colour will display
creeper_pixels = [
    cl_g, cl_g, cl_g, cl_g, cl_g, cl_g, cl_g, cl_g,
    cl_g, cl_r, cl_r, cl_g, cl_g, cl_r, cl_r, cl_g,
    cl_r, cl_r, cl_r, cl_r, cl_r, cl_r, cl_r, cl_r,
    cl_r, cl_r, cl_r, cl_r, cl_r, cl_r, cl_r, cl_r,
    cl_g, cl_r, cl_r, cl_r, cl_r, cl_r, cl_r, cl_g,
    cl_g, cl_g, cl_r, cl_r, cl_r, cl_r, cl_g, cl_g,
    cl_g, cl_g, cl_g, cl_r, cl_r, cl_g, cl_g, cl_g,
    cl_g, cl_g, cl_g, cl_g, cl_g, cl_g, cl_g, cl_g
]
sense.set_pixels(creeper_pixels)

sleep(1)
creeper_pixels = [
    cl_y, cl_y,  cl_s, cl_m, cl_i, cl_i, cl_g, cl_g,
    cl_y, cl_y,  cl_s, cl_m, cl_i, cl_r, cl_g, cl_g,
    cl_yl, cl_yl, cl_sl, cl_ml, cl_il, cl_rl, cl_gl, cl_gl,
    cl_yl, cl_yl, cl_sl, cl_ml, cl_il, cl_rl, cl_gl, cl_gl,
    cl_yl, cl_yl, cl_sl, cl_ml, cl_il, cl_rl, cl_gl, cl_gl,
    cl_yv, cl_yv, cl_sv, cl_mv, cl_iv, cl_rv, cl_gv, cl_gv,
    cl_yv, cl_yv, cl_sv, cl_mv, cl_iv, cl_rv, cl_gv, cl_gv,
    cl_w, cl_w, cl_wl, cl_wl, cl_wv, cl_wv, cl_wv, cl_b

]


# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)

sleep(5)
sense.clear()
pressure=0
while pressure == 0:
    pressure = sense.get_pressure()
    Temp = sense.temp
    s_Temp='T '+ format(Temp, '.0f')
    s_press='P '+ format(pressure, '.0f')
    print(s_press, Temp)

#sense.show_message(s_press)
#sense.show_message(s_Temp)

QNH=1013
Alt='Alt '+ format(CalcAlt (QNH,pressure, Temp), '.0f')
#sense.show_message(Alt)

print(s_press, Temp, Alt)

cnt=0
step=120
y=x=0
r=g=b=0
while r <= 255:
    g=0
    while g <= 255:
        b=0
        while b <= 255:
#            sense.set_pixel(x,y,r,g,b)
            sense.set_pixel(3,3,r,g,b)
            sense.set_pixel(3,4,r,g,b)
            sense.set_pixel(4,3,r,g,b)
            sense.set_pixel(4,4,r,g,b)
            print(cnt,r,g,b)
            sleep(1)
            #br=cnt % 64
            #br=b % 11
            #if br == 0:
            #    sleep(5)
            cnt+=1
            y+=1
            if y == 8:
                y=0
                x+=1
                if x == 8:
                    x=0
            b+=step
        g+=step
    r+=step
sleep(5)
sense.show_letter("Z")
sleep(2)
sense.clear()