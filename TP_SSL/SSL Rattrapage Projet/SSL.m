close all; clear variables;

B = 48000;
M = 4;
nu_0 = 500;
a_m = 1;
T = 5;
F_m = [3000, 9000, 15000, 21000]; %On divise par deux afin de respecter le critère de Shannon

%Question 7 

mu_max = B/(2*nu_0*M)-1;

k_max = mu_max*nu_0;


%Question 10

melange = 0;

for i=1:M
    [x_m, tps, X_m, freq] = Modulation(F_m(i), 1, nu_0, B, M, T);
    melange = melange + x_m;
end

[Fin,f] = TransFourier(melange,t);
figure(5);
plot(freq,melange);
title('Transformée de Fourier du mélange des signaux x_m');
xlabel('Fréquence'); ylabel('Amplitude');

