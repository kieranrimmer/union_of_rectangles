
from union_of_rectangles import Rectangle, perimeter_of_union_of_rectangles, measure_of_union_of_rectangles, contour_of_union_of_rectangles 

def read_rectangles_from_text_file(filename):
    with open(filename, 'r') as f:
       rectangle_list = [ Rectangle(int(x[0]), int(x[2]), int(x[1]), int(x[3])) for x in [ line.strip('\n').split(' ') for line in f.readlines()] ] 
    return rectangle_list

def main():

    frame_1_filename = 'frames_1.txt' 
    rectangle_list_1 = read_rectangles_from_text_file(frame_1_filename)

    p_1 = perimeter_of_union_of_rectangles(rectangle_list_1)
    print "Perimeter of union for file '{}': {}".format(frame_1_filename, p_1)


    frame_2_filename = 'frames_2.txt' 

    rectangle_list_2 = read_rectangles_from_text_file(frame_2_filename)

    p_2 = perimeter_of_union_of_rectangles(rectangle_list_2)
    print "Perimeter of union for file '{}': {}".format(frame_2_filename, p_2)




if __name__ == "__main__":
    main()

