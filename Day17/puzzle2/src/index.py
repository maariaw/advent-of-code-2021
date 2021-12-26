from inputreader import InputReader

def main():
    # Target dimensions
    min_x = 139
    max_x = 187
    min_y = -148
    max_y = -89

    combinations = []
    for init_x in range(max_x + 1):
        for init_y in range(min_y, 0 - min_y):
            y_place = init_y
            y_velocity = init_y - 1
            x_place = init_x
            x_velocity = init_x - 1
            while x_place < min_x or y_place > max_y:
                x_place += x_velocity
                if x_velocity > 0:
                    x_velocity -= 1
                else:
                    if x_place < min_x:
                        break
                y_place += y_velocity
                y_velocity -= 1
            if x_place > max_x or y_place < min_y:
                continue
            if x_place >= min_x and y_place <= max_y:
                # print("Adding ", init_x, ", ", init_y)
                combinations.append((init_x, init_y))
    
    print(f"""
    There are {len(combinations)} successful initial velocity values
    """)

if __name__ == "__main__":
    main()
