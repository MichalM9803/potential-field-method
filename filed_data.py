import point
import charg



__destination_point = point.Point(0,-1)
__negative_el_list = [charg.Charg(__destination_point,-1)]
# __positive_el_list = [charg.Charg(point.Point(-0.5,0),1)]
# negative_el_list  = [charg.Charg(point.Point(0.5,0),-1)]
__positive_el_list = []


__charg_list = __negative_el_list + __positive_el_list

__x_range = 2
__y_range = 2
__squer_size = 0.2


def get_destination_point():
    return __destination_point

def get_negative_el_list():
    return __negative_el_list

def get_positive_el_list():
    x = -0.7
    for i in range(15):
        y = 3*x*x*x*x
        temp = charg.Charg(point.Point(x,y),1)
        __positive_el_list.append(temp)
        __charg_list.append(temp)
        x = x + 0.1
    return __positive_el_list

def get_charg_list():
    return __charg_list

def get_x_renge():
    return __x_range

def get_y_renge():
    return __y_range


def get_squer_size():
    return __squer_size

