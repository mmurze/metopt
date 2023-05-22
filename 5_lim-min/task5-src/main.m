 [x1 ,x2] = meshgrid(-1.1:0.01:1.1);
z = x1.^2+x2.^2+4*sqrt(1+2*x1.^2+3*x2.^2);
contour(x1, x2, z)
hold on
%1
z = x1.^2 + x2.^2 - 1;
contour(x1,x2,z,[0,0])
hold on
%2
z = x1.^2 + x2.^2 - 0.5;
contour(x1,x2,z,[0,0])
hold on
%3
z = x1.^2 - 1;
contour(x1,x2,z,[0,0])
hold on
%answer
plot(-0.12834186, -0.08560516,'r*')
%colorbar
shading interp