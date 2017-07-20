class Matrix():
    
    def __init__(self,start_pic_str,end_pic_str):
        self.end_pic = []
        self.curr_pic = []

        self.row_cnt = 0
        self.col_cnt = 0
        for line in end_pic_str.split("\n"):
            self.row_cnt += 1
            if (len(line) > self.col_cnt):
                self.col_cnt = len(line)


        for line in start_pic_str.split("\n"):
            self.curr_pic.append([char for char in line])
        for line in end_pic_str.split("\n"):
            self.end_pic.append([char for char in line])

    def update(self):
        i = 0
        for line in self.curr_pic:
            j = 0
            for char in line:
                if ((len(self.end_pic[i]) > j) and (self.end_pic[i][j] != self.curr_pic[i][j])):
                    self.curr_pic[i][j] = self.end_pic[i][j]
                    return True
                j += 1
            i += 1
        return False

    def print(self):
        for line in self.curr_pic:
            for char in line:
                print(char,end='')
            print("")




# Testing only. Create new matrix and print repeatedly. Each update changes one character
#  until picture becomes equal to ending picrure
if (__name__ == "__main__"):
    # Starting picture
    start = """
-----   
|   |   
|               
|            
|              
|               
|               
|              
|              
--------"""

    # Ending picture
    end = """
-----
|   |
|   O 
| /-+-\ 
|   |  
|   | 
|  | |
|  | | 
|
--------"""

    myMatrix = Matrix(start,end)
    while myMatrix.update():
        myMatrix.print()
