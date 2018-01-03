#https://www.hackerrank.com/challenges/2d-array/problem
import sys,os
import math
table=[]
print 'set the table size'
N =6

table=[[2 , 4 , 5 , 6 ,727, 453],
[2 , 4 , 5 , 6 ,77, 43],
[29 , 448 , 275 , 36 ,717, 6543],
[25 , 14 , 59 , 61 ,7327, 435],
[23 , 141 , 95 , 161 ,7217, 643],
[21 , 42 , 556 , 62 ,757, 423],
[12 , 445 , 53 , 16 ,717, 143]]

def is_valid_HG(tb,col_index):
        VALID_COLUMN_LENGTH=3
        VALID_ROW_LENGTH=3
        is_valid= True
        row_length = len(tb) #index that i am
        #validate columns size
        is_valid&= row_length>=VALID_ROW_LENGTH
        if is_valid:
            column_length = len(tb[col_index:])
            is_valid&= column_length>=VALID_COLUMN_LENGTH
        return is_valid

def iterate_table(table):
    length =  len(table)
    j=i = 0
    while i< length:
        row = table[i]
        while j< len(row):
            if is_valid_HG(table[i],j):
                print 'row', row

            j+=1
        i+=1
        j=0
iterate_table(table)