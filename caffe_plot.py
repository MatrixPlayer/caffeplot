# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 16:48:32 2016

@author: WuJianping
"""

import re
import matplotlib.pyplot as plt

def parser_log(logfile):
    regex_iteration = re.compile('Iteration (\d+)')
    regex_train_output_accuarcy = re.compile('Train net output #0: (\S+) = ([\.\deE+-]+)')
    regex_train_output_loss = re.compile('Train net output #1: (\S+) = ([\.\deE+-]+)')
    regex_test_output_accuarcy = re.compile('Test net output #0: (\S+) = ([\.\deE+-]+)')
    regex_test_output_loss = re.compile('Test net output #1: (\S+) = ([\.\deE+-]+)')
    regex_learning_rate = re.compile('lr = ([-+]?[0-9]*\.?[0-9]+([eE]?[-+]?[0-9]+)?)')
    
    iteration = -1;
    
    learning_rate = [[], []]
    train_accuracy = [[], []]
    train_loss = [[], []]
    test_accuracy = [[], []]
    test_loss = [[], []]

    
    with open(logfile, "r") as fp:
        for line in fp:
#            print line
            iteration_match = regex_iteration.search(line)
            if iteration_match:
                iteration = int(iteration_match.group(1))
            if -1 == iteration:
                continue;
#            print iteration
            
            learning_rate_match = regex_learning_rate.search(line)
            if learning_rate_match:
                lr = float(learning_rate_match.group(1))
#                print lr
                learning_rate[0].append(iteration)
                learning_rate[1].append(lr)
                
            train_accuracy_match = regex_train_output_accuarcy.search(line)
            if train_accuracy_match:
                trainacc = float(train_accuracy_match.group(2))
                train_accuracy[0].append(iteration)
                train_accuracy[1].append(trainacc)
                
            train_loss_match = regex_train_output_loss.search(line)
            if train_loss_match:
                trainloss = float(train_loss_match.group(2))
                train_loss[0].append(iteration)
                train_loss[1].append(trainloss)
                
            test_accuracy_match = regex_test_output_accuarcy.search(line)
            if test_accuracy_match:
                testacc = float(test_accuracy_match.group(2))
                test_accuracy[0].append(iteration)
                test_accuracy[1].append(testacc)
                
            test_loss_match = regex_test_output_loss.search(line)
            if test_loss_match:
                testloss = float(test_loss_match.group(2))
                test_loss[0].append(iteration)
                test_loss[1].append(testloss)
            
        
    return learning_rate, train_accuracy, train_loss, test_accuracy, test_loss


def caffe_plot(logfile):
    learning_rate, train_accuracy, train_loss, test_accuracy, test_loss = parser_log(logfile)

    plt.xlabel("iter")
    plt.ylabel("loss")
    plt.plot(test_loss[0], test_loss[1], 'b-', label='test_loss')
    plt.plot(train_loss[0], train_loss[1], 'r-', label='train_loss')
    plt.legend()
    plt.show()
    plt.savefig(r'D:\save.png')
   

if __name__ == '__main__':
	logfile = r"E:\DATA\FaceData\deepID-implement\log\INFO2016-07-04T19-59-13.txt"
	caffe_plot(logfile)
 
 
 
 
 
 
 
 