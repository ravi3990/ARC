#!/usr/bin/python

''' 
This is assignment 3, group submission by : 
    Student Name : Ravi Mishra Student ID: 21249928
    Student Name : Prasad Deshpande Student ID: 21249530 
    
    Link to Github Repository : https://github.com/ravi3990/ARC.git
    
    

'''


import os, sys
import json
import numpy as np
import re
import math

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

'''
solve_d4a91cb9: 

Difficulty Level according to us : Easy to Medium

Logic :

The basic logic for solving this problem through the naked eye and to a layman 
person would be get the coordinates of the two colours ie sky blue and red.The 
values for these in our list is 2 and 8.And then connect the 2 points throug 
it's row and column by two lines of yellows till it intersects.

We used the numpy where function to find the coordinates of these points.The main 
problem in solving this issue was to find out in what direction the line has to be plotted.
For this we used the if else to determine if blue has higher column value or red.
Based on that we update the corresponding values in the given row and column to 4.

Basic python and numpy used.Was able to solve all inputs and outputs in the json 
file successfully.

    
'''

def solve_d4a91cb9(x):
    #Changing to Numpy array in case the input is a list
    b=np.array(x)
   #Getting the position of 8 and 2 in the array    
    eight_pos=np.where(b==8)[0][0],np.where(b==8)[1][0]
    two_pos=np.where(b==2)[0][0],np.where(b==2)[1][0]
    #Changing the column values to 4 
    if eight_pos[0]<two_pos[0]:
        for i in range (eight_pos[0]+1,two_pos[0]+1):
            b[i][eight_pos[1]]=4
    elif eight_pos[0]>two_pos[0]:
        for i in range (two_pos[0],eight_pos[0]):
            b[i][eight_pos[1]]=4
    
    #Changing the row  values to 4
    if eight_pos[1]<two_pos[1]:
        for i in range (eight_pos[1]+1,two_pos[1]):
            b[two_pos[0]][i]=4
    elif eight_pos[1]>two_pos[1]:
        for i in range (two_pos[1]+1,eight_pos[1]+1):
            b[two_pos[0]][i]=4
    return b

'''
solve_f5b8619d: 

Difficulty Level according to us : Easy

Logic :

On a first look it looked a little difficult to us.However we could quickly understand 
that it is a mirror effect after some basic changes to the inital array.
In the initial array we have to identify the columns where the value is non zero.
We have to change the value of all the rows for that column without touching the original 
values to 8.Once it is completed we have to mirror the array along the horizontal 
axis once and then the vertical axis once.This can be done interchangeably as well.

Basic python and numpy has been used.

All the test inputs and outputs were successfully validated and passed.
    
'''


def solve_f5b8619d(x):
    new_arr=np.array(x)
    #Getting the columns where the value is non zero and changing rest of the column values to 8
    for mn in np.where(new_arr!=0)[1]:
        for i in range(new_arr.shape[1]):
            if new_arr[i][mn]==0:
                new_arr[i][mn]=8
     #Mirroring the array horizontally and vertically           
    new_arr=np.concatenate((new_arr,new_arr),axis=0)
    new_arr=np.concatenate((new_arr,new_arr),axis=1)
    return new_arr

'''
solve_0a938d79: 
    
Difficulty Level according to us : Easy 

We found Task 0a938d79 simple to understand and implement. Looking at task demonstration 
we can see alternate coloured line pattern repeats until end of array. If number of rows are 
more than the columns then line patterns are repeated until last row. If the number of 
columns are more than the rows then the line patterns are repeated until end of last column. 
Count for intermediate black rows are dependent on number of columns/rows between given 
two colour cells. 

Solver function checked shape of array, colours of non-black locations and loop through
the rows/columns until max number of rows/columns reached. Coloured locations/cells are
used as reference to paint the location to create the line in X or Y axis and new array
return after transformation. 

All training and test grids solved correctly. 
    
'''

def solve_0a938d79(x):
    '''empty list to collect coloured cells'''
    non_zero = []
    
    ''' copy input array'''
    new_arr=np.array(x)
    
    ''' get number of rows are colums with shape'''
    num_rows, num_cols = new_arr.shape 
    
    '''find the non-zero coordinates '''
    non_zero = np.nonzero(new_arr)
    
    '''find the colour at non-zero coordinates '''
    colour_1 = new_arr[non_zero[0][0], non_zero[1][0]]
    colour_2 = new_arr[non_zero[0][1], non_zero[1][1]]

    '''if number of columns are greater than rows then patterns need to be 
    formed in x-axis else in y-axis'''
        
    if(num_cols > num_rows):
        black_mid_segments = abs(non_zero[1][1] - non_zero[1][0]) 
        while((non_zero[1][0] or non_zero[1][1]) < num_cols):
            '''fill the colour at non-zero column''' 
            for i in range(num_rows):
                if(non_zero[1][0] < num_cols):
                    new_arr[i,non_zero[1][0]] = colour_1
                if(non_zero[1][1] < num_cols):
                    new_arr[i,non_zero[1][1]] = colour_2     
            '''increment coloumn index based number of empty col. in pattern'''
            non_zero[1][0] += (black_mid_segments*2)
            non_zero[1][1] += (black_mid_segments*2)
    else:
        black_mid_segments = abs(non_zero[0][0] - non_zero[0][1]) 
        while((non_zero[0][0] or non_zero[0][1]) < num_rows):
            '''fill the colour at non-zero rows''' 
            for i in range(num_cols):
                if(non_zero[0][0] < num_rows):
                    new_arr[non_zero[0][0], i] = colour_1
                if(non_zero[0][1] < num_rows):
                    new_arr[non_zero[0][1], i] = colour_2     
            '''increment row index based number of empty col. in pattern'''
            non_zero[0][0] += (black_mid_segments*2)
            non_zero[0][1] += (black_mid_segments*2)
    
    ''' return the modified array''' 
    return new_arr

'''
solve_1a07d186(x)

Difficulty Level according to us : Medium to difficult 

We found Task 1a07d186 medium to be difficult. On the first look, task seems easy 
i.e. just moving the coloured cells adjacent to respective lines. But it is also important to 
identify line as object, move coloured cells in right direction and to remove other 
coloured cells which doesn’t have coloured line present. The same logic then needs to be 
defined for vertical and horizontal lines (single/multiple).

We decided to implement the solver function with basic logic and with less use of 
library APIs. Numpy is used only where necessary, so the code looks big. It identified 
colour in array and marked the coordinates. Then identified the line object with traversing 
in X/Y axis from edge to edge to confirm the line position. Once all these information 
is available, then look for nearest line coordinate for coloured cell and paint next 
location in same row/column. The original colour location is then overwritten with black. 
In case of cells with colours other than line colour, the location is overwritten with black.  

All training and test grids solved correctly. 

'''

def solve_1a07d186(x):
    
    ''' copy input array'''
    new_arr=np.array(x)
    
    ''' get number of rows are colums with shape'''
    num_rows, num_cols = new_arr.shape 
    
    '''find the non-zero coordinates '''
    non_zero = np.nonzero(new_arr)

    ''' index for checking all coordinates around the colour'''
    Dy = [0, -1, 0, 1]
    Dx = [1, 0, -1, 0]
    
    ''' empty lists to log if Hlines or Vlines found in image'''
    H_line = []
    V_line = []
    
   
    ''' loop to check colour around all identified colour co-ordinates '''
    for x, y  in zip(non_zero[0],non_zero[1]):
        colour = new_arr[x][y]
        
        for dy, dx in zip(Dy, Dx):
            ''' if same colour found then move either x or y axis to find if it is a line'''
            x_, y_ = x+dx, y+dy
            
            ''' loop through number of cols or rows to find lines and log into list '''
            if(x_ < num_rows and y_ < num_cols):
                if(colour == new_arr[x_][y_]):
                    if(abs(x_ - x)):
                        #vertical line 
                        for k in range(num_rows):
                            if(colour == new_arr[k][y]):
                                V_line.append(y) 
                                v_line_flag = True
                
                    if (abs(y_-y)):
                        #horizontal line 
                        for k in range(num_cols):
                            if(colour == new_arr[x][k]):
                                H_line.append(x)
                                v_line_flag = False
    
    ''' consider only unique items to give exact number of lines and their one 
    coordinates location. Other location can be assumed zero as it is a line'''  
    H_line = np.unique(H_line)
    V_line = np.unique(V_line)
    
    ''' loop through all coloured cellls to either associate with line or if 
    not then make it zero'''
    for x, y  in zip(non_zero[0],non_zero[1]):
        if(v_line_flag == True):
            ''' if y is not in Vline then proceed '''
            if(y not in V_line):
                colour_flag = False    
                colour = new_arr[x][y]
                
                for i in V_line:
                    if(colour == new_arr[0, i]):
                        if(i < y):
                            new_arr[x,i+1] = colour
                        else:
                            new_arr[x,i-1] = colour
                        
                        new_arr[x][y] = 0
                        colour_flag = True
                ''' if colour cell is not associated with line colour then 
                make it zero '''        
                if(colour_flag == False ): 
                    new_arr[x][y] = 0
            
            
        if(v_line_flag == False):
            '''if x is not in Hline then proceed '''
            if(x not in H_line):
                colour_flag = False    
                colour = new_arr[x][y]
    
                for i in H_line:
                    if(colour == new_arr[i, 0]):
                        if(i < x):
                            new_arr[i+1, y] = colour
                        else:
                            new_arr[i-1, y] = colour
                        
                        new_arr[x][y] = 0
                        colour_flag = True    
                ''' if colour cell is not associated with line colour then 
                make it zero '''        
                if(colour_flag == False ): 
                    new_arr[x][y] = 0
                        
               
                    
    ''' return the modified array''' 
    return new_arr

'''
def solve_00d62c1b(x)

Difficulty Level according to us : Medium to difficult 

We found task 00d62c1b medium to be difficult. The challenge was in finding the enclosed 
shape to fill the space with yellow colour. The logic which is applied here is same 
as previous task 1a07d186, instead of lines, here is to identify the space enclosed 
with green colour. 

Same logic of x, y location +/-1 for checking all coordinates around the coloured 
cell used. Code optimized with the use of list as queue and multiple conditions in loops. 
‘Searched’ array created with padding of rows and columns. Based on search the true/False 
marked and resultant used for filling yellow colour. 
The in-line comments give more details of logic. 

All training and test grids solved correctly.

'''

def solve_00d62c1b(x):
    
    ''' copy input array'''
    new_arr=np.array(x)
    
    ''' get number of rows are colums with shape'''
    num_rows, num_cols = new_arr.shape 
 
    green = 3 
    yellow = 4
    
    ''' index for checking all coordinates around the colour'''
    Dy = [0, -1, 0, 1]
    Dx = [1, 0, -1, 0]
    
    '''
    https://numpy.org/doc/stable/reference/generated/numpy.pad.html
    
    ((1,1),(1,1)) -Number of values padded to the edges of each axis. ((before_1, after_1)
    pads with 'Constant' value of zero [False]                                                               
    
    '''
    
    arr_padded = np.pad(new_arr, ((1,1),(1,1)), "constant", constant_values=0)
    
    ''' 
    input array padded on x and y axis at the edge i.e. num_col and num_rows 
    increased by 2 and created searched array with default False in each element''' 
    search_empty_sq = np.zeros(arr_padded.shape, dtype=bool)
    search_empty_sq[0, 0] = True
    
    queue = [(0, 0)]
    while queue:
        ''' take each element/cell from matrix'''
        j, i = queue.pop()
        
        ''' loop for near by coordinates in x, y axis '''
        for dy, dx in zip(Dy, Dx):
            y_, x_ = j+dy, i+dx
            
            if not 0 <= y_ < num_rows+2 or not 0 <= x_ < num_cols+2:
                ''' skip the next logic for edge elements/cells'''
                continue
            ''' in case of identical elements change value at searched to True 
                else maintain the value at False. False indicates yellow colour 
                to add 
            '''
            if not search_empty_sq[y_][x_] and arr_padded[y_][x_]==0:
                '''add to queue for next operation '''
                queue.append((y_, x_))
                search_empty_sq[y_, x_] = True
    
    '''remove the padding'''
    res = search_empty_sq[1:-1, 1:-1]
    
    ''' check the green and keep it as it is'''
    res |= new_arr==green
    
    ''' invert the searched results and fill true with yellow '''
    new_arr[~res] = yellow 
   
    ''' return the modified array''' 
    return new_arr

'''
def solve_d0f5fe59(x)

Difficulty level according to us : Medium

Logic:
The idea behind solving this problem was to get the number of islands within a 
particular array.This was done through a depth first search.Once a particulat 
island is visited it is not counted twice.For this we created an internal functions 
called dfs.


After iterating through the entire array we found the number of islands.We then 
created a numpy zero array with the same dimensions as the number of islands.
We then update the diagonal of the array with the value 8.

We were able to succsfully validate and test all the inputs with their given outputs 
as in the json file.


'''

def solve_d0f5fe59(x):
    row=len(x)
    col=len(x[0])
    count=0
   #Creating a function for Depth first search for finding the islands
    def dfs(a,row,col,m,n):
        if a[m][n]==0:
            return
        a[m][n]=0
        
        if m!=0:
            dfs(a,row,col,m-1,n)
    
        if m!=row-1:
            dfs(a,row,col,m+1,n)
    
        if n!=0:
            dfs(a,row,col,m,n-1)    
        if n!=col-1:
            dfs(a,row,col,m,n+1) 
            #Iterating to count the number of islands   
    for i in range(row):
        for j in range(col):
            if x[i][j]==8:
                dfs(x,row,col,i,j)
                count+=1
     #Creating a zero numpy array with the same dimensions as the number of islands           
    b=np.zeros((count, count), int)
    #Filling the diagonal with the value 8
    np.fill_diagonal(b,8)    

    return b

'''
def solve_4093f84a(x)


Difficulty Level  according to us : Medium to Difficult

Logic : 
4093f84a.json looked to be simple on the testing interface initially.Logically 
we needed to find the rectangle with 5's and then determine whether it was a horizontal 
one or a vertical one.After that close to the the rectangle  we had to fill the 5 in 
the respective rows or columns.

We tried to have a simple approach of finding the bigger island with the rectangle first.
After that we made all the other positions as zero.We noted the positions of the other 
values.And then added them to the rectangle in their respective rows and columns.

The given code use basic python and numpy functions.
While testing this it passed for the test demonstration 1.However there was a 
slight difference in demosntraions 2 and 3 as there were multiple non 5 values in the 
same row or column.This made it to not completely satisfy the outputs for 2 and 3 and test input grid.

The idea to solve this would be to get the positions ond the number of such colours 
in a particular row or column.Once we get the number we can add to the same side of 
the rectangle the cells and this would result in the success of the function


'''


def solve_4093f84a(x):
    x=np.array(x)
    #Getting positions where the value is non zero
    mn=np.where(x!=0)
    #Getting positions where the value is five
    yz=np.where(x==5)
    emp_lst=[]
    #Adding to an empty list the positions of the non 5 and non zero values
    for i in range(len(mn[0])):
        if x[mn[0][i]][mn[1][i]]!=5:
            emp_lst.append([mn[0][i],mn[1][i]])
    #Making all the non island positions 0 before actioning
    for m in emp_lst:
        x[m[0],m[1]]=0
    #Action to alter the value to 5 for the respective postions near to the island    
    if np.amin(yz[1])==0:
        for m in emp_lst:
            if m[0]<np.amin(yz[0]):
                x[np.amin(yz[0])-1][m[1]]=5
            else :
                x[np.amax(yz[0])+1][m[1]]=5
    else :
        for m in emp_lst:
            if m[1]<np.amin(yz[1]):
                x[m[0]][np.amin(yz[1])-1]=5
            else :
                x[m[0]][np.amax(yz[1])+1]=5
    return x


'''
def solve_5ad4f10b(x)

Difficulty Level according to us : Difficult

Logic:

For solving 5ad4f10b.json we tried to look at various ways for coming up.It seemed 
a little difficult.The main challenge was to find the area for the section which was 
to be contracted and then the values updated with the other colour outliers.

Following is the approach we followed for this section :

1.Identify the n*n squares(start with 3) in the given array,their coordinates as 
well and store their values in separate lists.
2.Get the max and min values of the rows and column numbers for the areas containing squares.
3.Create a new array with only the rows and columns which  was obtained from Step 2
4.Clear any other colour values than 0 and the squares and convert it to 0.
5.Get the other colour value from the original array and create a new array with the specific positions.

We have used basic numpy and math library to get this output.

The one limitation to this part of the code is that it is currently useful for 
3*3 squares only(Training Input and output 2 currently. We can use a similar version of 
the same code by altering the for loops a little to make it working for 4*4 squares as well.
Due to timing limitations we have not tried it. However we believe the logic would be near 
about the same and would work for other training and test grids as well with slight modifications.
'''

def solve_5ad4f10b(x):
    a=np.array(x)
    row,colmn=a.shape[0],a.shape[1]
    
     #Code to get the 3*3 squares inside the array

    emp_lst1=[]
    range_lst1=[]
    #comp=0
    for i in range(row):
        for j in range(colmn):
            emp_lst=[]
            range_lst=[]
            comp=0
            if i-1>0 and j-1>0 and i+1<row and j+1<colmn:
                for m in range(i-1,i+2):
                    for n in range(j-1,j+2):
                        emp_lst.append(a[m][n])
                        range_lst.append ((m,n))
                       
            if len(emp_lst)>0 and emp_lst[0]!=0:
                comp=1
                #print (emp_lst )
                for mn in emp_lst:
                    if emp_lst[0]!=mn:
                        comp+=1 
            #print(comp)
            if comp==1 and len(emp_lst)>0:
                #print(emp_lst)
                #print(range_lst)
                emp_lst1.append(emp_lst)
                range_lst1.append(range_lst)
                
    #Getting the minimum and maximum section of the array to be cut            
    
    min_row=range_lst1[0][0][0]

    for m in range_lst1:
        for n in m:
            if n[0]<min_row:
                min_row=n[0]
 
    min_col=range_lst1[0][0][1]

    for m in range_lst1:
        for n in m:
            if n[1]<min_col:
                min_col=n[1]
    max_row=range_lst1[0][0][0]

    for m in range_lst1:
        for n in m:
            if n[0]>max_row:
                max_row=n[0]
                
    max_col=range_lst1[0][0][1]

    for m in range_lst1:
        for n in m:
            if n[1]>max_col:
                max_col=n[1]
                
    new_arr=a[min_row:max_row+1,min_col:max_col+1]
    #Clear the array for any oher number which are outliers
    new_row,new_col=new_arr.shape[0],new_arr.shape[1]
    
    for i in range(new_row):
        for j in range(new_col):
            if new_arr[i][j]!=emp_lst1[0][0]:
                new_arr[i][j]=0

    new_mod_arr=np.zeros((int(math.sqrt(new_row)),int(math.sqrt(new_col))))
    row_alt,col_alt=new_mod_arr.shape[0],new_mod_arr.shape[1]
    
    #Getting the colour value which has to be updated
    non_zero_val_loc=np.where(a!=0)
    
    for m in non_zero_val_loc[0]:
        for n in non_zero_val_loc[1]:
            if a[m][n]!=emp_lst1[0][0]:
                val_to_update=a[m][n]
    
    #Updating the new modified array with the intended values
    for i in range(0,new_row,3):
        for j in range(0,new_col,3):
            if new_arr[i][j]!=0:
                new_i=int(i/3)
                new_j=int(j/3)
            #print (new_i,new_j)
                new_mod_arr[new_i,new_j]=val_to_update
    return new_mod_arr

''' 

A short summary/reflection, commenting on the Python features and libraries you used in the solve * 

In first semester of MSc. while learning and working on assignments we could see maturity 
of available ML packages which can trained on different kind of tasks e.g., NLP task for 
suggestion mining or regression tasks for prediction of home prices etc. but while working 
with ARC, we realized that we’re still very far away from building a human like intelligence. 
All the tasks (.JSON files) when looked in browser, one can identify the patterns in seconds 
just looking at few samples, but it is not easy for ML/programming to generalize this type 
of intelligence. We didn’t find much help on generalised pattern recognition available, 
and ARC is an upcoming new topic in field of AI. We both found it is super interesting 
and addictive i.e., we initially though to just complete 3-4 patterns and submit the assignment 
but end up coding 8-9 patterns!

We did not use any ML package or specific libraries but used Numpy and pure python to 
translate our understanding of patterns into code. We found that, in future there can 
be few common functions/libraries be made to recognize the patterns e.g., find specific 
shape objects or enclosed spaces, highlight repetitive patterns, symmetry etc. or correlate 
the colours in base image to transformed image. These functions in addition to math 
libraries can be then basis for creating hypothesise in terms of hyper parameters or 
support functions. We still have limited understanding of this topic and acknowledge 
that writing the code to solve all sorts of problems i.e., generalisation is not easy 
task. 


Commonalities between the problems :

->Pattern Recognition is very important.
->Many problems include finding the position of enclosed areas and islands.
->In many problems we had dimensionality reshaping as well as revaluation of the array.
->Most of the problems can be solved via if else loops or basic libraray functions.
  However as mentioned before  there is no one off solution to all problems


Github has been thoroughly used by us for core sharing and working as a team of 2.
Readme file has been altered as well for reflecting the ARC understanding.

As mentioned by François Chollet in his paper 'The Measure of Intelligence' the 
solutions can be generalised only to a limited extent because of some of the limitations 
which we could see while solving our given problems.The major limitations were a 
generalisation of the problem and limited set of inputs and outputs for training 
on the same problem. We could only test what was given to use.We are however aware 
that there will be many variations in the given formations.

No doubt there are still many leaps to be taken by Arificial Intelligence!


'''


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()


