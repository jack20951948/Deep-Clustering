'''
Class DataGenerator:
    Read in the .pkl data sets generated using datagenerator.py
    and present the batch data for the model
'''
import numpy as np
import librosa
import pickle
from numpy.lib import stride_tricks
import ipdb
import os
import matplotlib as mpl
mpl.use('agg')
from matplotlib import pyplot as plt
import pickle
from GlobalConstont import *


class DataGenerator(object):
    def __init__(self, pkl_list, batch_size):
        '''pkl_list: .pkl files contaiing the data set'''
        self.ind = 0  # index of current reading position
        self.batch_size = batch_size
        self.samples = []
        self.epoch = 0
        # read in all the .pkl files
        for pkl in pkl_list:
            self.samples.extend(pickle.load(open(pkl, 'rb')))
        self.tot_samp = len(self.samples)
        print(self.tot_samp, "samples")
        np.random.shuffle(self.samples)

    def gen_batch(self):
        # generate a batch of data
        n_begin = self.ind
        n_end = self.ind + self.batch_size
        # ipdb.set_trace()
        if n_end >= self.tot_samp:
            # rewire the index
            self.ind = 0
            n_begin = self.ind
            n_end = self.ind + self.batch_size
            self.epoch += 1
            np.random.shuffle(self.samples)
        self.ind += self.batch_size
        return self.samples[n_begin:n_end]

#if __name__ == '__main__':
#    print("begin datagenerator2.py!")
#    pkl_dir = r'C:\Users\changjac\Google Drive\HP Intern\EE\deep-clustering-master\pkl_folder'
#    gen = DataGenerator(pkl_dir, 64)
#    gen.gen_batch()