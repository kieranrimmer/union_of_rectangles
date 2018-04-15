
from union_of_rectangles import Rectangle, perimeter_of_union_of_rectangles, measure_of_union_of_rectangles, contour_of_union_of_rectangles 

def read_rectangles_from_text_file(filename):
    with open(filename, 'r') as f:
       rectangle_list = [ Rectangle(int(x[0]), int(x[2]), int(x[1]), int(x[3])) for x in [ line.strip('\n').split(' ') for line in f.readlines()] ] 
    return rectangle_list

def main():

    # rectangle_list = [Rectangle(1, 3, 1, 3), Rectangle(2, 4, 2, 4), Rectangle(5, 7, 5, 7)] # 20
    # rectangle_list = [Rectangle(1, 3, 1, 3)]
    # rectangle_list = [Rectangle(0, 10, 0, 10), Rectangle(1, 3, 1, 3), Rectangle(2, 4, 2, 4), Rectangle(3, 5, 3, 5)]
    # rectangle_list = [Rectangle(1, 3, 1, 3), Rectangle(5, 7, 5, 7)]
    # rectangle_list = [Rectangle(1, 3, 1, 3), Rectangle(2, 4, 2, 4), Rectangle(3, 5, 3, 5)]
    # rectangle_list = [Rectangle(1, 3, 1, 3), Rectangle(2, 4, 2, 4)]

    rectangle_list = [Rectangle(1, 3, 1, 3), Rectangle(2, 4, 2, 4), Rectangle(1, 5, 2, 4)]

    p = perimeter_of_union_of_rectangles(rectangle_list)
    print "Perimeter of union:", p

    m = measure_of_union_of_rectangles(rectangle_list)
    print "Measure of union:", m


    frame_1_filename = 'frames_1.txt' 
    rectangle_list_1 = read_rectangles_from_text_file(frame_1_filename)

    p_1 = perimeter_of_union_of_rectangles(rectangle_list_1)
    print "Perimeter of union for file '{}': {}".format(frame_1_filename, p_1)

    m_1 = measure_of_union_of_rectangles(rectangle_list_1)
    print "Measure of union:", m_1

    frame_2_filename = 'frames_2.txt' 

    rectangle_list_2 = read_rectangles_from_text_file(frame_2_filename)

    p_2 = perimeter_of_union_of_rectangles(rectangle_list_2)
    print "Perimeter of union for file '{}': {}".format(frame_2_filename, p_2)

    m_2 = measure_of_union_of_rectangles(rectangle_list_2)
    print "Measure of union:", m_2

    # vertical_edges, horizontal_edgs = contour_of_union_of_rectangles(rectangle_list)
    # print "Vertical Edges in Contour:", vertical_edges
    # print "Horizontal Edges in Contour:",  horizontal_edgs


if __name__ == "__main__":
    main()

