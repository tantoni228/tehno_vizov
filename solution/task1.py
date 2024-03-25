def check_crossroad(robot, point1, point2, point3, point4):
    try:
        ox = min(point1[0], point2[0], point3[0]) < robot[0] < max(point1[0], point2[0], point3[0])
        oy = min(point2[1], point3[1], point4[1]) < robot[1] < max(point2[1], point3[1], point4[1])
        return ox and oy
    except TypeError:
        return "Error"


if __name__ == "__main__":
    # Test1
    print(f"Test 1: {check_crossroad((9, 3), (26, 13), (14, 13), (26, 23), (14, 23))}")
    # Test2
    print(f"Test 2: {check_crossroad((5, 8), (0, 3), (12, 3), (12, 16), (0, 16))}")
    # Test3
    error_test = "Hello, World!!!"
    print(f"Test 3: {check_crossroad(error_test, (0, 3), (12, 3), (12, 16), (0, 16))}")
    # Test4
    print(f"Test 4: {check_crossroad((9, 3), (26, 13), (26, 23), (14, 23), (14, 13))}")
    # Test5
    print(f"Test 5: {check_crossroad((17, 18), (4, 20), (41, 16), (4, 16), (41, 20))}")
