def check_collision(data):
    out = []
    for i, value in enumerate(data):
        for j, value2 in enumerate(data):
            if i != j:
                a1, b1, c1 = value[0], value[1], value[2]
                a2, b2, c2 = value2[0], value2[1], value2[2]
                try:
                    x = (c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1)
                    if not (x >= -70 and x <= 70):
                        continue
                except ZeroDivisionError:
                    continue
                try:
                    y = - (a1 * x + c1) / b1
                    if not (y >= -70 and y <= 70):
                        continue
                except ZeroDivisionError:
                    continue
                out.append((i, j))
    return out


if __name__ == "__main__":
    # Test 1
    data1 = [[-1, -4, 0], [-7, -5, 5], [1, 4, 2], [-5, 2, 2]]
    print(f"Test 1: {check_collision(data1)}")

