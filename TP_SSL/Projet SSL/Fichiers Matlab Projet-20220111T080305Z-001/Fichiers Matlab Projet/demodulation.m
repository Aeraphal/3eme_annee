function [sFinal, t] = demodulation(sInput, t, Fp)

    Fe = 96000; % Fréquence d'échantillonnage
    Fc = 3000; % Fréquence de coupure du filtre passe-bas
    Vp = 0.1; % Amplitude de la porteuse
    
    sp = Vp*cos(2*pi*Fp*t); % Creation de la porteuse
    
    sm = sInput.*sp; % Multiplication entre la porteuse et le signal modulé
    [S1, f1] = TransFourier(sm, t);
    sFinal = PasseBas(sm, Fe, Fc);
    [S2, f2] = TransFourier(sFinal, t);
    
    subplot(2,2,1);
    plot(t,sm); xlabel('temps(t)');
    title('Signal réceptionné multiplié par la porteuse');
    
    subplot(2,2,2);
    plot(f1, real(S1)); ylim([0,inf]); xlim([-2*10^4,2*10^4]);
    xlabel('fréquence(f)');
    title('Signal réceptionné multiplié par la porteuse dans le domaine fréquentiel');
    
    subplot(2,2,3);
    plot(t, sFinal);
    xlabel('temps(t)');
    title('Signal final démodulé reconstruit s(t)');
    
    subplot(2,2,4);
    plot(f2, real(S2)); ylim([0,inf]);xlim([-2*10^4,2*10^4]);
    xlabel('fréquence(f)');
    title('Signal démodulé dans le domaine fréquentiel');
    
    


