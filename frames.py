
from union_of_rectangles import Rectangle, perimeter_of_union_of_rectangles, measure_of_union_of_rectangles, contour_of_union_of_rectangles 

def read_rectangles_from_text_file(filename):
    with open(filename, 'r') as f:
       rectangle_list = [ Rectangle(int(x[0]), int(x[2]), int(x[1]), int(x[3])) for x in [ line.strip('\n').split(' ') for line in f.readlines()] ] 
    return rectangle_list

def main():

    frame_filename = raw_input("Which data file do you want to use? ")
    rectangle_list_1 = read_rectangles_from_text_file(frame_filename)

    perimeter = perimeter_of_union_of_rectangles(rectangle_list_1)
    print "The perimeter is: {}".format(perimeter)




if __name__ == "__main__":
    main()

