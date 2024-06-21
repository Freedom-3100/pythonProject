import Stack_List_Queue


def vawe(arr, From, to):
    Front = Stack_List_Queue.Queue
    x_From, y_From = From
    arr[y_From][x_From] = 2
    Front.push(From)
    From = (x_From , y_From , x_From , y_From)
    head = (From[0] , From[1])
    ind = 0
    while len(Front) != 0 or head != to:
        x = -1
        y = -1
        for i in range(3):
            for j in range(3):
                From[0] += x
                From[1] += y
                if x != 0 and y != 0:
                    for k in range(4):
                        for h in range(2):
                            if arr[From[1] + k][From[0] + h] == 1 or arr[From[1] + k][From[0] + h] == 2:
                                return
                        if k == 3 and h == 1 and arr[From[1] + k][From[0] + h] == 0:
                            arr[From[1]][From[0]] = 2
                            Front.push((From[0], From[1], From[0] - x, From[1] - y))
                x += 1
            y += 1
        ind += 1
        head = (Front[ind][0] , Front[ind][1])

    if len(Front) == 0:
        return False

    if head == to:
        return Front
def

def comeback(Front,From,to):
    current = to
    if current == (Front[0][0] , Front[0][1]):
        return to
