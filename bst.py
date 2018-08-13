# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:32:04 2018

@author: shampa shahriyar
"""

def insert(data,root):
    tempNode={}
    tempNode['val']=data
    tempNode['left']={}
    tempNode['right']={}
    current={}
    parent={}
    ##if tree is empty
    if any(root.values())==False:
        root = tempNode
        return root
    else:
        current = root
        parent = {}
        while True:
            parent = current
            #go to left of the tree
            if data < parent['val']:
                current = current['left']              
                ##insert to the left
                if any(current.values())==False:
                    parent['left'] = tempNode
                    return root

            else:  ##go to right of the tree
                current = current['right']
                ##insert to the right
                if any(current.values())==False:
                    parent['right'] = tempNode
                    return root
def search(data,root):
    current=root
    while(current['val']!=data):
        if any(current.values()):
            print(current['val'])
            if current['val']>=data:
                current=current['left']
            else:
                current=current['right']
            if any(current.values())==False:
                print("not found")
                return 
    print("found")

def test():
  root={}
  root=insert(6,root)
  root=insert(3,root)
  root=insert(12,root)
  root=insert(7,root)
  root=insert(15,root)
  search(5,root)
  search(12,root)
  search(7,root)
