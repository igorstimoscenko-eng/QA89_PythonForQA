#1
def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
        return
    print(lst[::-1])


print_list_reverse([1, 2, 3, 4, 5])  # [5, 4, 3, 2, 1]
print_list_reverse([])               # Wrong list
print_list_reverse(None)             # Wrong list
print_list_reverse("abc")            # Wrong list
print_list_reverse((1, 2, 3))        # Wrong list

#2
def is_valid_point(point):
    if point is None or point == ():
        return None
    if not isinstance(point, tuple) or len(point) != 2:
        return False
    return all(
        isinstance(coord, (int, float)) and not isinstance(coord, bool)
        for coord in point
    )


print(is_valid_point((3, 5)))      # True
print(is_valid_point((3.5, -2)))   # True
print(is_valid_point((3, "5")))    # False
print(is_valid_point([3, 5]))      # False
print(is_valid_point((1, 2, 3)))   # False
print(is_valid_point((True, 5)))   # False
print(is_valid_point(()))          # None
print(is_valid_point(None))        # None

#3
def is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def print_sublist_reverse(lst, start, finish):
    if (
        not isinstance(lst, list)
        or not lst
        or not is_int(start)
        or not is_int(finish)
        or not (0 <= start <= finish < len(lst))
    ):
        print("Wrong args")
        return
    print(lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:])


print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)  # [10, 40, 30, 20, 50, 60]
print_sublist_reverse([1, 2, 3], "0", 2)               # Wrong args
print_sublist_reverse([1, 2, 3], 2, 1)                 # Wrong args
print_sublist_reverse([1, 2, 3], 0, 3)                 # Wrong args
print_sublist_reverse(None, 0, 1)                      # Wrong args