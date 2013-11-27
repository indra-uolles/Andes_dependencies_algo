Andes_dependencies_algo
=======================

A model-tracing ITS is a system where students can enter full solutions of multi-step problems like it is shown here (this is a screenshot of Andes Physics Tutor, probably the most advanced model-tracing ITS):

![screenshot of Andes Physics Tutor](http://volga.asmon.ru/images/andes.gif)

Users of model-tracing ITS can check their solution steps for correctness, receive hints, receive grades for their solutions - all of that is done automatically.

This repository contains Andes Physics Tutor algorithm of dependency checking. I realized it as it was described in [1] to examine its properties. 

1 - [J.A.Shapiro. An Algebra Subsystem for Diagnosing Students' Input in a Physics Tutoring System](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=A4CDE3B32ABCB3250B3DF96A0612AF75?doi=10.1.1.87.9408&rep=rep1&type=pdf)

This repository requires SymPy v.0.7.2 (it won't work with SymPy 0.7.3 cause it has a different realization of matrices)
Works with Python 2.7 and numpy 1.6.1
