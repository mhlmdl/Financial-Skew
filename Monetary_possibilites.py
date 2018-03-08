'''
Created on Feb 20, 2018

@author: mhlmdl
'''
from math import sqrt
def expectation(m1,p,m2):
    EX=m1*p+m2*(1-p)
    print "Expectation of set with",m1,"and",m2, "is", EX
    
#def var(m1, p, m2):
 #   X=m1*p+m2*(1-p)
  #  var=(m1-EX)**2+(m2-EX)**2
   # print "Variance of set with",m1,"and",m2, "is",var

def possible(ev,p,var):
    ev=float(ev)
    p=float(p)
    var=float(var)
    m2pos=((2*ev-4*ev*p**2)+sqrt(((2*ev-4*ev*p**2)**2)-4*(1-p**2)*(ev**2-(ev**2)*p-var*p)))/(2*(1-p**2))
    m2neg=((2*ev-4*ev*p**2)-sqrt(((2*ev-4*ev*p**2)**2)-4*(1-p**2)*(ev**2-(ev**2)*p-var*p)))/(2*(1-p**2))
    m1pos=(ev-(1-p)*m2pos)/p
    m1neg=(ev-(1-p)*m2neg)/p
    print "Set 1 is:", m1pos,"with p1=",p,"," , m2pos,"with p2=",(1-p)
    print "Set 2 is:", m1neg,"with p1=",p,"," , m2neg,"with p2=",(1-p)
    expectation(m1pos, p, m2pos)
    expectation(m1neg, p, m2neg)
  #  var(m1pos, p, m2pos)
   # var(m1neg, p, m2neg)
    
possible(5, 0.25, 9)
possible(0.5,.95, 9)
