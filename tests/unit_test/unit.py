#!/usr/bin/env python
import unittest
import numpy as np

def Tx(x):
    Tx = np.array([ [1,0,0,x],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    return Tx
def Ty(y):
    Ty = np.array([ [1,0,0,0],
                    [0,1,0,y],
                    [0,0,1,0],
                    [0,0,0,1]])
    return Ty

def Tz(z):
    Tz = np.array([ [1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,z],
                    [0,0,0,1]])
    return Tz
def Rz(q):
    Rz = np.array([ [np.cos(q),-np.sin(q), 0, 0],
                    [np.sin(q), np.cos(q), 0, 0],
                    [    0    ,    0     , 1, 0],
                    [    0    ,    0     , 0, 1]])
    return Rz
def FK(q2):
	a = np.array([[0],[0], [0], [1]])
	P = Tz(0.9).dot(Tx(1.0).dot(Ty(-1.0).dot(Rz(q2).dot(Rz(90*3.142/180).dot(Ty(0.65).dot(Tz(-0.46).dot(a)))))))
	return P[:3]
class Test(unittest.TestCase):
	def test_FK(self):
		b = np.array([[0.38925516],[-1.22246514], [0.44]])
		self.assertEqual(np.sum((FK(20*3.142/180)- b) < 0.001), 3)
if __name__ == '__main__':
	unittest.main()
    