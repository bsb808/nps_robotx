
R = 1.0

H = linspace(0,3*R)
A =[]
for h in H:
    A.append(R**2*arccos((R-h)/R)-(R-h)*sqrt(2*R*h-h**2))

figure(3)
clf()
plot(H,A)
