gravitational_constant = 6.67408E-11


def calculate_force(body, space_objects):

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        else:
            r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
            a=abs(body.y - obj.y)/r
            b=abs(body.x - obj.x)/r
            body.Fx += G*(body.m)*(obj.m)/(r*b)
            body.Fy += G*(body.m)*(obj.m)/(r*a)


def move_space_object(body, dt):

    ax = body.Fx/body.m
    body.Vx += ax*dt
    body.x += (body.Vx)*dt+((body.ax)*dt*dt)/2
    ay = body.Fy/body.m
    body.Vy += ay*dt
    body.y += (body.Vy)*dt+((body.ay)*dt*dt)/2


def recalculate_space_objects_positions(space_objects, dt):
    
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
