# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:24:48 2017

@author: shoham
"""

class Worker : 
    
    def __init__ (self,name , id , salary ) : 
        self._name = name 
        self._id = id
        self._salary = salry
    
    def printWorker(self):
        print(self._name)
        print(self._id)
        print(self._salary)
        
        
        
class Manager (Worker) : 
    ##_list=[]
    #count=0
    
    def __init__ (self,name , id , salary ) : 
        Worker.__init__(name , id , salary)
        self._list = []
        
    def addWorker(self, wor):
        self._list.append(wor)
        
    def printManager(self):
        for obj in self._list:
             obj.printWorker();


w=Worker('ddd','232134',2312 ) 
 
 
    
    
    
    
    
               
               
               