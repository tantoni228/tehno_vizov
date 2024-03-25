def check_path(points_list):
    total_path = 0
    if len(points_list) > 1:
        for i in range(len(points_list) - 1):
            projection_x = abs(points_list[i + 1][0] - points_list[i][0])
            projection_y = abs(points_list[i + 1][1] - points_list[i][1])
            total_path += (projection_x ** 2 + projection_y ** 2) ** 0.5
    return round(total_path, 2)


if __name__ == "__main__":
    # Test 1
    test1 = [(1.0, 2.0), (2.0, 3.0)]
    print(f"Test 1: {check_path(test1)}")
    # Test 2
    test2 = [(2.0, 3.0), (4.0, 5.0)]
    print(f"Test 2: {check_path(test2)}")
    # Test 3
    test3 = [(1.0, 2.0), (2.0, 3.0), (4.0, 5.0)]
    print(f"Test 3: {check_path(test3)}")
