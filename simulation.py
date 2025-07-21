import random

NUM_OF_EXP=100
ROWS=50
class Person: #
    def __init__(self, row, sit, time):
        self.row = row
        self.sit = sit
        self.time = time

def enter_time(self,plane_use):
    blocks=0
    if self.sit==1:
        if plane_use[self.row][2]==1:
            blocks+=1
        if plane_use[self.row][3] == 1:
            blocks+=1
    if self.sit==6:
        if plane_use[self.row][5]==1:
            blocks+=1
        if plane_use[self.row][4] == 1:
            blocks+=1
    if self.sit==2:
        if plane_use[self.row][3]==1:
            blocks+=1
    if self.sit==5:
        if plane_use[self.row][4]==1:
            blocks+=1
    self.time+=random.expovariate(2)
    if blocks!=0:
        self.time += random.expovariate(1 / (0.5 + 0.25 * blocks))


def sit_down(line,plane_use,current_time):
    clear_line=line.copy()
    line.clear()
    for i in range (len(clear_line)):
        if (clear_line[i].time>current_time):
            clear_line[i].time-=current_time
            line.append(clear_line[i])
        else:
            plane_use[clear_line[i].row][clear_line[i].sit]=1
            clear_line[i].time=0

def shffle_1(array):
    flat_list = [item for sublist in array for item in sublist]
    random.shuffle(flat_list)
    return flat_list
def shffle_2(array):
    for row in array:
        random.shuffle(row)
    flat_list = [item for sublist in array for item in sublist]
    return flat_list

def shffle_3(array):
    for row in array:
        random.shuffle(row)
    flat_list = [item for sublist in array for item in sublist]
    reverse_list=flat_list[::-1]
    return reverse_list
def shffle_4(array):
    new_array= [[None for c in range(ROWS)] for r in range(6)]
    for i in range(6):
        for j in range(ROWS):
            new_array[i][j]=array[j][i]
    new_array2=shffle_2(new_array)
    return new_array2
if __name__ == "__main__":
    basic_array = [
        [Person ( row=r, sit=c, time=0) for c in range(6)]
        for r in range(ROWS)
    ]
    all_time=0

    line_array=[]
    print("choose one option:\n option 1: rondom\n option 2 start to end \n option 3  end to start \n option 4 by the sit")
    x=int(input())
    if x==1:
        shaffle=shffle_1
    if x == 2:
        shaffle = shffle_2
    if x == 3:
        shaffle = shffle_3
    if x == 4:
        shaffle = shffle_4
    if x<1 or x>4 :
        shaffle=shffle_1
    for i in range(NUM_OF_EXP):
        plane_use = [[0 for c in range(6)] for r in range(ROWS)]
        order_array=shaffle(basic_array)
        k=0
        time =0
        current_time=0
        while True :
            if k==6*ROWS:
                while len(line_array)!=0:
                    current_time=line_array[-1].time
                    sit_down(line_array, plane_use, current_time)
                    time+=current_time
                break
            if len(line_array)==0 or order_array[k].row<line_array[-1].row:
                enter_time(order_array[k],plane_use)
                #print(1)
                #print(order_array[k].time)
                line_array.append(order_array[k])
                current_time=order_array[k].time
                k+=1

                continue
            else:
                time+=current_time
                sit_down(line_array,plane_use, current_time)
                if len(line_array)==0:
                    current_time=0
                else:
                    current_time=line_array[-1].time

        all_time+=time
    print(all_time/NUM_OF_EXP)
