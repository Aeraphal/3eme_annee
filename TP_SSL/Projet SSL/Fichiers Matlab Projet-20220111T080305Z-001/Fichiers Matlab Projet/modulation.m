function [signalModule, t] = modulation(Fp)
    Fe = 96000 ; % Fréquence d'échantillonage
    Fc = 2800 ; % Fréquence de coupure du filtre passe-bas
    T = 5 ; % Durée de l'enregistrement
    Vp = 0.1; % Amplitude de la porteuse
    
    [voix, signalRecorded, t] = RecordModulation(Fe,T); % Enregistrement de la voix grâce à une fonction RecordModulation
    
    signalModulant = PasseBas(signalRecorded, Fe, Fc); % Filtrage du signal enregistré par un filtre passe-bas avec Fc = 3 kHz
    
    porteuse = Vp*cos(2*pi*Fp*t); % signal de la porteuse
    signalModule = (signalModulant.*porteuse)./max(abs(signalModulant)); % création du signal modulé
    
    [tfSignalRecorded,nu1] = TransFourier(signalRecorded,t);
    [tfSignalModulant,nu] = TransFourier(signalModulant,t);
    [tfSignalPorteuse,nu2] = TransFourier(porteuse,t);
    [tfSignalModule,nu3] = TransFourier(signalModule,t);
    
   % set(gca, 'XTickLabel', get(gca, 'XTick'));
    subplot(2,2,1);
    plot (t,signalRecorded); xlabel('temps(t)');
    title('Signal enregistré s_r(t)');
    
    subplot(2,2,3);
    plot (t,signalModulant); xlabel('temps(t)');
    title('Signal modulant filtré s_rf(t)');
    
%     subplot(2,4,3); 
%     plot (t, porteuse);
%     title('Signal de la porteuse s_p(t)'); xlabel('temps(t)'); xlim([2.970, 2.971]);
%     
%     subplot(2,4,4);
%     plot(t, signalModule);xlabel('temps(t)');
%     title('Signal modulé s_m(t)');
%     
%     subplot(2,4,5);
%     plot (nu1, real(tfSignalRecorded)); xlabel('fréquence(f)'); xlim([-8000, 8000]);ylim([0,inf]);
%     title('Transformée de Fourier du signal enregistré S_r(f)');
%     
%     subplot(2,4,6);
%     plot (nu, real(tfSignalModulant)); xlabel('fréquence(f)'); xlim([-8000, 8000]);ylim([0,inf]);
%     title('Transformée de Fourier du signal enregistré S_rf(f)');
    
    subplot(2,2,2);
    plot (nu2, abs(tfSignalPorteuse)); xlabel('fréquence(f)');  xlim([-10000, 10000]);ylim([0,inf]);
    title('Transformée de Fourier de la porteuse S_p(f)');
    
    subplot(2,2,4);
    plot (nu3, abs(tfSignalModule)); xlabel('fréquence(f)');ylim([0,inf]);
    title('Transformée de Fourier du signal modulé S_m(f)');
    
    while 1 == 1 
        soundsc(signalModule, Fe);  
        pause(T);
    end