import point
import charg



__destination_point = point.Point(0,-1)
__negative_el_list = [charg.Charg(__destination_point,-1)]
# __positive_el_list = [charg.Charg(point.Point(-0.5,0),1)]
# negative_el_list  = [charg.Charg(point.Point(0.5,0),-1)]
__positive_el_list = []
__last_visited_point = {}


__charg_list = __negative_el_list + __positive_el_list

__x_range = 3
__y_range = 3
__squer_size = 0.2
__additional_constns_of_visited_points = 0.1


def update_last_visited_points(x,y):
    temp_point = point.Point(x,y)

    if temp_point in __last_visited_point.keys():
        __last_visited_point[temp_point] =  __last_visited_point[temp_point] 
    else:
         __last_visited_point[temp_point] = 1

def create_positive_shape():
    x = -0.7
    for i in range(15):
        y = 3*x*x*x*x
        __update_positive_list(x,y)
        x = x + 0.1


def __update_positive_list(x,y):
        temp = charg.Charg(point.Point(x,y),1)
        __positive_el_list.append(temp)
        __charg_list.append(temp)



def get_last_visited_list():
    return __last_visited_point

def get_destination_point():
    return __destination_point

def get_negative_el_list():
    return __negative_el_list

def get_positive_el_list():

    return __positive_el_list

def get_charg_list():
    return __charg_list

def get_x_renge():
    return __x_range

def get_y_renge():
    return __y_range


def get_squer_size():
    return __squer_size

def get_add_constans():
    return __additional_constns_of_visited_points