import numpy as np
a = np.matrix('0.49 -0.128 0.09 0.15 0.15; -0.03 0.32 0 -0.61 0.02; 0.01 -0.09 0.58 0.011 0.035; 0.03 0 -0.073 0.58 0; 0.02 -0.03 0.145 -0.012 0.42') 
print(a) 

b = np.matrix('1.564; -1.733; 1.393; 1.744; -2.046') 
print(b) 

a_det = np.linalg.det(a) 
print(a_det) 

x_m = np.matrix(a) 
x_m[:, 0] = b 
print(x_m) 

y_m = np.matrix(a) 
y_m[:, 1] = b 
print(y_m) 

z_m = np.matrix(a) 
z_m[:, 2] = b 
print(z_m) 

q_m = np.matrix(a) 
q_m[:, 3] = b 
print(q_m) 

c_m = np.matrix(a) 
c_m[:, 4] = b 
print(c_m)

x = np.linalg.det(x_m) / a_det 
y = np.linalg.det(y_m) / a_det 
z = np.linalg.det(z_m) / a_det 
q = np.linalg.det(q_m) / a_det 
c = np.linalg.det(c_m) / a_det

print("xl=",x) 
print("x2=",y) 
print("x3=",z) 
print("x4=",q) 
print("x5=",c)
