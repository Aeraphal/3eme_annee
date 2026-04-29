function [T,s] = signalTP2(A,v_0,phi_0,D,Fe)
    T =  0:1/Fe:D;
    s =  A*sin(2*pi*v_0*T+phi_0*pi/180);
end