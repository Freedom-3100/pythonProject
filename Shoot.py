import math

def trajectory(angle, x_cord,y_cord, wight, hight, power):
    x_cord_0 = x_cord
    y_cord_0 = y_cord
    arr = []
    while x_cord > 0 and x_cord < wight and y_cord > 0 and y_cord < hight:
        if angle != 90 and angle !=-90 and angle != 270:
            y_cord = (x_cord-x_cord_0) * math.tan(math.radians(angle)) + 10 * (x_cord - x_cord_0) ** 2 / 2 / (power ** 2) / (math.cos(math.radians(angle)) ** 2) + y_cord_0
        elif angle == -90:

            y_cord += 5
        else:
            y_cord -= 5

        y_cord = int(y_cord)
        if angle > -90 and angle < 90:
            if y_cord >= hight:
                cur = x_cord, hight
                arr.append(cur)
                return arr
            elif y_cord <= 0:
                cur = x_cord, 0
                arr.append(cur)
                return arr
            else:
                cur = x_cord, y_cord
                arr.append(cur)
            x_cord += 1

        elif angle > 90 and angle < 270:
            if y_cord >= hight:
                cur = x_cord, hight
                arr.append(cur)
                return arr
            elif y_cord <= 0:
                cur = x_cord, 0
                arr.append(cur)
                return arr
            else:
                cur = x_cord, y_cord
                arr.append(cur)
            x_cord -= 1


    return arr






