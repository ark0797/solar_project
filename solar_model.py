gravitational_constant = 6.67408E-11


def calculate_force(body, space_objects):

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        else:
            r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
<<<<<<< HEAD
            a=(obj.y - body.y)/r
            b=(obj.x - body.x)/r
            body.Fx += b*gravitational_constant*(body.m)*(obj.m)/(r**2)
            body.Fy += a*gravitational_constant*(body.m)*(obj.m)/(r**2)
=======
            a=abs(body.y - obj.y)/r
            b=abs(body.x - obj.x)/r
            body.Fx += G*(body.m)*(obj.m)/(r*b)**2
            body.Fy += G*(body.m)*(obj.m)/(r*a)**2
>>>>>>> cd803b1524e3e667a94ed4cde8ae8248e43b6cc1


def move_space_object(body, dt):

    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.Vx += ax*dt
    body.Vy += ay*dt
    body.x += body.Vx *dt
    body.y += body.Vy *dt

def recalculate_space_objects_positions(space_objects, dt):
    
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
