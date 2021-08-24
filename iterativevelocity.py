GlowScript 3.0 VPython

### iterative modeling###
#constant velocity # denotes for velocity part1 ##
#constant acceleration ### denotes acc part2# but,rabbit part3
## x=-0.31*t*t + 7.2*t +28
##y=0.22*t*t -9.1*t +30

#...set scene...#
scene=canvas(background_color=color.white)

## define your origin ##
origin=sphere(opacity=0.8)

## axis defining my axis##
x_axis=curve(pos=[vector(-15,0,0),vector(15,0,0)],color=color.blue)
y_axis=curve(pos=[vector(0,-15,0),vector(0,15,0)],color=color.red)
z_axis=curve(pos=[vector(0,0,-15),vector(0,0,15)],color=color.green)

## create an object ##
##boxer=box(pos=vector(2,0,0),color=color.blue)
##boxer=box(pos=vector(5,3,0),color=color.blue,make_trail=True)
rabbit=sphere(pos=vector(28,30,0),color=color.white,make_trail=True)
print("The initial position is ",rabbit.pos)
rab_pos= arrow(axis=rabbit.pos,opacity=0.8,color=color.red)

## create variables##
#acc=vector(0,-9.8,0)
#vel= vector(4,14,0)
dt=0.1
t=0

v_x=-0.62*t+ 7.2
v_y=0.44*t-9.1
vel=vector(v_x,v_y,0)
rab_veclocity=arrow(pos=rabbit.pos,axis=vel,color=color.green,opacity=0.4)
acc=vector(-0.62,0.44,0)
rab_acc=arrow(pos=rabbit.pos,axis=acc,color=color.blue,opacity=0.4)

## iteration to change positions##
while t<31:
 rate(100)
 x=-0.31*t*t + 7.2*t +28
 y=0.22*t*t -9.1*t +30
 rabbit.pos = vector(x,y,0)
 v_x=-0.62*t+ 7.2
 v_y=0.44*t-9.1
 vel=vector(v_x,v_y,0)
 rab_velocity.pos=rabbit.pos  
 rab_veocity.axis=vel
 ##rabbit acceleration vector
 rab_acc.pos=rabbit.pos
 
 
 
 #vel = vel + acc*dt
 #boxer.pos = boxer.pos + vel * dt + 0.5*acc*dt*dt
 t=t+dt
print("The final position is ",rabbit.pos)

