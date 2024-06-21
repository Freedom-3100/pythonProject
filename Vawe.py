

def wave(arr, From, to,wight,hight):
    arr_new = arr
    Front = [From]
    From_x , From_y = From
    arr_new[From_y][From_x] = 2
    ind = 1
    head = (Front[0][0],Front[0][1])
    mass_y = [From_y-1,From_y,From_y+1]
    mass_x = [From_x-1,From_x,From_x+1]
    while len(Front) != 0 or head != to:
        for i in range(3):
            From_y_1 = mass_y[i]
            for j in range(3):
                From_x_1 = mass_x[j]
                if From_x_1 == 3 and From_y_1 == 3:
                    print('lox')
                if From_x_1 > wight-1 or From_y_1 > hight-1 or From_y_1 < 0 or From_x_1 < 0:
                    continue
                if i == 1 and j == 1:
                    continue
                else:
                    for k in range(4):
                        for h in range(2):
                            if   From_y_1 - k < 0 or From_x_1 + h > wight - 1  :
                                break
                            if arr[From_y_1 - k][From_x_1 + h] == 1:
                                break
                        if  From_y_1 - k < 0 or From_x_1 + h > wight - 1  :
                            break

                        if  arr[From_y_1 - k][From_x_1 + h] == 1:
                            break

                        if k == 3 and h == 1 and arr[From_y_1 - k][From_x_1 + h] == 0 and arr[From_y_1 ][From_x_1 ] == 0:
                            arr[From_y_1][From_x_1] = 2 + ind
                            Front.append((From_x_1 , From_y_1))


        ind += 1
        Front.pop(0)

        if len(Front) == 0:
            return False
        mass_y = [Front[0][1]-1,Front[0][1],Front[0][1]+1]
        mass_x = [Front[0][0]-1,Front[0][0],Front[0][0]+1]
        head = (Front[0])

        if head == to:
            return arr_new


def wave_search(arr, From, wight, hight):
    arr_new = arr
    Front = [From]
    From_x, From_y = From
    arr_new[From_y][From_x] = 2
    ind = 1
    head = Front[0]
    mass_y = [From_y - 1, From_y, From_y + 1]
    mass_x = [From_x - 1, From_x, From_x + 1]
    while len(Front) != 0:
        for i in range(3):
            From_y_1 = mass_y[i]
            for j in range(3):
                From_x_1 = mass_x[j]
                if From_x_1 > wight - 1 or From_y_1 > hight - 1 or From_y_1 < 0 or From_x_1 < 0:
                    continue
                if i == 1 and j == 1:

                    continue
                else:
                    for k in range(5):
                        for h in range(3):
                            if  From_y_1 - k < 0 or From_x_1 + h > wight - 1:
                                break
                            if arr[From_y_1 - k][From_x_1 + h] == 1:
                                break
                        if arr[From_y_1 - k][From_x_1 + h] == 1 or From_y_1 - k < 0 or From_x_1 + h > wight - 1:
                            break
                        if k == 4 and h == 2 and arr[From_y_1 - k][From_x_1 + h] == 0 and arr[From_y_1][From_x_1] == 0:
                            arr[From_y_1][From_x_1] = 2 + ind
                            Front.append((From_x_1, From_y_1))
                            arr[From_y_1][From_x_1] = 0
                            arr[From_y][From_x] = 0
        ind += 1

        cur = Front.pop(0)
        if cur[0] != From_x or cur[1] != From_y:
            return cur

        if len(Front) == 0:
            return False
        mass_y = [Front[0][1] - 1, Front[0][1], Front[0][1] + 1]
        mass_x = [Front[0][0] - 1, Front[0][0], Front[0][0] + 1]
        head = (Front[0])


def wave_return(arr_new, From , To,wight,hight):
    search = []
    if arr_new == False:
        return False
    else:
        To_x, To_y = To
        min_value = arr_new[To_y][To_x]
        mass_y = [To_y - 1, To_y, To_y + 1]
        mass_x = [To_x - 1, To_x, To_x + 1]
        min_x , min_y = To_x, To_y
        while To != From:
            for i in range(3):
                To_y_1 = mass_y[i]
                for j in range(3):
                    To_x_1 = mass_x[j]
                    if To_x_1 > wight-1 or To_y_1 > hight-1 or To_y_1 < 0 or To_x_1 < 0:
                        continue
                    if j == 1 and i == 1:
                        continue
                    if arr_new[To_y_1][To_x_1] <= min_value and arr_new[To_y_1][To_x_1] != 1  and  arr_new[To_y_1][To_x_1] != 0:
                        min_x , min_y = To_x_1,To_y_1
                        min_value = arr_new[To_y_1][To_x_1]


            if min_x != To_x and min_y != To_y:
                search.append((min_x,min_y))
            mass_y = [min_y - 1, min_y, min_y + 1]
            mass_x = [min_x - 1, min_x, min_x + 1]
            if len(search) !=0:
                To = search[-1]
    return search



