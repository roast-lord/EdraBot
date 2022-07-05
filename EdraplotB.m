function [] = EdraplotB(directory, nomes, titulo)
    pkg load io
    titulo = csv2cell('data/tB.csv');
    nomes = csv2cell('data/nB.csv');
    directory = csv2cell('data/dB.csv');
    [motores, baterias] = size(directory);
    all_data = [];
    dados = 10;

    for k = 1:motores

        for i = 1:baterias
            data = csvread(['csv/' directory{k, i} '.csv']);

            all_data = [all_data data];
            data = [];
        end

        espacamento = all_data(2, 1) - all_data(1, 1);

        %XY - tempo de voo x peso total (curvas de bateria)
        figure(1)
        cores = cellstr(['-mo'; '-k*'; '-xg'; '-sb'; '-+c'; '-rd'; '-yp'; '-mv']);
        j = 1;

        for i = 1:dados:(baterias * dados)

            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 1);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel(" Tempo de voo (min)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)
            x_axis = 0;
            y_axis = 0;
            hold on

        end

        legend(nomes, 'fontsize', 26);
        print(['graficos/' titulo{1, k} ' TVxPT-B.png'], '-dpng')
        figure(2)
        j = 1;
        %XY - Peso empuxo x Peso total ( Curvas de bateria)
        for i = 1:dados:(baterias * dados)
            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 2);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel("Peso-Empuxo", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)

            hold on
            x_axis = 0;
            y_axis = 0;
        end

        legend(nomes, 'fontsize', 26)
        print(['graficos/' titulo{1, k} ' PExPT-B.png'], '-dpng')

        %XY - Peso pras outrs areas x Peso total (curvas de motor)
        figure(3)
        j = 1;

        for i = 1:dados:(baterias * dados)
            x_axis = all_data(:, i);
            y_axis = x_axis - all_data(:, i + 4);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel("Peso para outras areas (g)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)

            hold on
            x_axis = 0;
            y_axis = 0;
        end

        legend(nomes, 'fontsize', 26)
        print(['graficos/' titulo{1, k} ' PPOAxPT-B.png'], '-dpng')
        %Velocidade Max
        figure(4)
        j = 1;

        for i = 1:dados:(baterias * dados)
            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 5);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel("Velocidade MAX (km/h)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)

            hold on
            x_axis = 0;
            y_axis = 0;
        end

        legend(nomes, 'fontsize', 26)
        print(['graficos/' titulo{1, k} ' VelxPT-B.png'], '-dpng')
        %VOO VARIADO
        figure(5)
        j = 1;

        for i = 1:dados:(baterias * dados)

            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 6);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel(" Tempo de voo Variado (min)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)
            x_axis = 0;
            y_axis = 0;
            hold on

        end

        legend(nomes, 'fontsize', 26);
        print(['graficos/' titulo{1, k} ' TVVxPT-B.png'], '-dpng')
        %Corrente X Peso Total
        figure(6)
        j = 1;

        for i = 1:dados:(baterias * dados)

            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 7);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel(" Corrente (A)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)
            x_axis = 0;
            y_axis = 0;
            hold on

        end

        legend(nomes, 'fontsize', 26);
        print(['graficos/' titulo{1, k} ' CxPT-B.png'], '-dpng')
        % Tensão X Peso total
        figure(7)
        j = 1;

        for i = 1:dados:(baterias * dados)

            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 8);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel(" Tensao (V)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)
            x_axis = 0;
            y_axis = 0;
            hold on

        end

        legend(nomes, 'fontsize', 26);
        print(['graficos/' titulo{1, k} ' TxPT-B.png'], '-dpng')
        % RPM X Peso Total
        figure(8)
        j = 1;

        for i = 1:dados:(baterias * dados)

            x_axis = all_data(:, i);
            y_axis = all_data(:, i + 9);
            plot(x_axis, y_axis, cores{j, 1});
            grid on
            j++;
            xlabel("Peso Total (g)", 'fontsize', 20);
            ylabel(" Rotacoes (RPM)", 'fontsize', 20);
            set(gcf, 'Position', get(0, 'ScreenSize'))
            set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
            title(titulo{1, k}, 'fontsize', 26)
            x_axis = 0;
            y_axis = 0;
            hold on

        end

        legend(nomes, 'fontsize', 26);
        print(['graficos/' titulo{1, k} ' RPMxPT-B.png'], '-dpng')

        all_data = [];

        close all
    end

    fprintf('Graficos salvos! Voce pode fechar esta janela agora.\n');
end
