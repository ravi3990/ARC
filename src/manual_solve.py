#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
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

