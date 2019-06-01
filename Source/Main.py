import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

def read():
    # the dna sequences exists in a  dna.txt file
    with open("data.txt", "r") as reader:
        seq1 = reader.read()
        seq1 = seq1.split('\n')
        seq2 = seq1[1]
        seq1 = seq1[0]
        seq1 = seq1.replace(' ','')
        seq2 = seq2.replace(' ', '')
    return seq1,seq2

def dot_plot(seq1,seq2,window_size,threshold):
    length1 = len(seq1)
    length2 = len(seq2)
    array = np.zeros([length1+2, length2+2], dtype=np.uint8)
    for x in range(length1 +2 ):
        for y in range(length2 +2):
            array[x][y] = 255

    window1= seq1[:window_size]
    window2= seq2[:window_size]
    print(window1, '', window2)
    for j in range(length2 - window_size+1) :
        window2 = seq2[j:window_size + j]
        match= 0;
        for i in range(length1 - window_size +1):
            print(window1, window2, '\n')
            match = 0
            window_letters1 = list(window1)
            window_letters2 = list(window2)
            print(window_letters1,window_letters2)
            index = 0
            for letter1 in window_letters1:
                    if letter1 == window_letters2[index]:
                        match += 1
                        #print('match?')
                    index+=1
            if match >= threshold:
                array[i+2][j+2] = 0
                print('match')
            window1 = seq1[i:window_size + i]
    return array


window_size = 3
threshold = 3
seq1,seq2 = read()
print(seq1, ' ' , seq2)
array = dot_plot(seq1,seq2,window_size,threshold)
img = Image.fromarray(array)
img.save('sample_in.png')
