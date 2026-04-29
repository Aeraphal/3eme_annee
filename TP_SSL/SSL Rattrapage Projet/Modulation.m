function [x_m, tps, X_m, freq] = Modulation(F_m, a_m, nu_0, B, M, T)

% [x_m, tps, X_m, freq] = Modulation(F_m, a_m, nu_0, B, M, T)

% Input: 
% - F_m : La fréquence de la porteuse
% - a_m : l'amplitude du signal à transmettre
% - nu_0 : La fréquence du signal modulant
% - B : La borne supérieure de la bande passante du canal
% - M : Nombre de signaux à transmettre simultanément
% - T : La durée du signal à transmettre, t appartient à [0,T[
% Outputs:
% - x_m : Le signal échantillonné
% - tps : Le vecteur de temps
% - X_m : La transformée de Fourier
% - freq : Le vecteur de fréquence correspondant

tps = 0:2/B:T-2/B;
k = 2000;
x_m = cos(2*pi*F_m*tps + k*a_m/nu_0.*sin(2*pi*nu_0*tps));
v_m_exp = instfreq(x_m, tps);

v_m_th = F_m+k*a_m.*cos(2*pi*nu_0*tps);

[X_m, freq] = TransFourier(tps, x_m);

figure(1);
subplot(221);
plot(tps,x_m);
title('Signal x_m');
xlabel('Temps'); ylabel('Amplitude');

subplot(222);
plot(tps,v_m_exp,'r'); hold on; plot(t,v_m_th,'k');
title('Fréquence instantannée expérimentale et théorique');
xlabel('Temps'); ylabel('Amplitude');

subplot(223);
plot(freq,real(X_m));
title('Signal des réels de la Transformée de Fourier X_m de x_m')
xlabel('Fréquence'); ylabel('Amplitude');

subplot(224);
plot(freq, phase(X_m));
title('Signal Zoomer sur la bande passante utile de la Transformée de Fourier X_m')
xlim(F_m-B/(4*M),F_m+B/(4*M)); 
xlabel('Fréquence'); ylabel('Amplitude');











