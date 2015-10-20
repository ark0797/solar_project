from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):


    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue 
            object_type = line.split()[0].lower()
            if object_type == "star": 
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    
    A=line.split()
    star.R=int(A[1])
    star.color=A[2]
    star.m=A[3]
    star.x=A[4]
    star.y=A[5]
    star.Vx=A[6]
    star.Vy=A[7]
    
    

def parse_planet_parameters(line, planet):

    A=line.split()
    planet.R=int(A[1])
    planet.color=A[2]
    planet.m=A[3]
    planet.x=A[4]
    planet.y=A[5]
    planet.Vx=A[6]
    planet.Vy=A[7]


def write_space_objects_data_to_file(output_filename, space_objects):

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, obj.type, ' ', obj.R , ' ', obj.color, ' ', obj.m, obj.x, ' ', obj.y, ' ', obj.Vx, ' ', obj.Vy, ' '))

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...













if __name__ == "__main__":
