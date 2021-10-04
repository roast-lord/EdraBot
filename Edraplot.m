function [] = Edraplot()
    pkg load io
    directory =  csv2cell('data/d.csv');
    nomes = csv2cell('data/n.csv');
    [l,motores] = size(directory);
    all_data = [];
    titulo = csv2cell('data/t.csv');

    for i = 1:motores
        data = csvread( ['csv/' directory{1,i} '.csv'] );
        

        all_data = [all_data data];
        data = [];
    end
    espacamento = all_data(2,1) - all_data(1,1);

    %XY - tempo de voo x peso total (curvas de motor)
    figure(1)
    cores = cellstr(['-mo';'-k*';'-xg';'-sb';'-+c';'-rd']);
    j = 1;
    for i = 1:6:(motores*6)
        
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+1);
        plot(x_axis,y_axis,cores{j,1});
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel(" Tempo de voo (min)", 'fontsize', 20);
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        title(titulo{1,1}, 'fontsize', 26)
        hold on
        x_axis = 0;
        y_axis = 0;
    end
    legend(nomes,'fontsize',26)
    print(['graficos/' titulo{1,1} ' TVxPT-M.png'],'-dpng')


    i=0;

    %XY - Peso pras outrs areas x Peso total (curvas de motor)
    j=1;
    figure(2)
    for i = 1:6:(motores*6)
        x_axis = all_data(:,i);
        y_axis = x_axis - all_data(:,i+4);
        plot(x_axis,y_axis,cores{j,1});
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel("Peso para outras areas (g)", 'fontsize', 20);
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        title(titulo{1,1}, 'fontsize', 26)
        
        
        hold on
        x_axis = 0;
        y_axis = 0;
    end
    legend(nomes,'fontsize',26)
    print(['graficos/' titulo{1,1} ' PPOAxPT-M.png'],'-dpng')
    j=1;
    figure(3)
    %XY - Empuxo especifico x Peso total ( Curvas de motor )
    for i = 1:6:(motores*6)
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+3);
        plot(x_axis,y_axis,cores{j,1})
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel("Empuxo Especifico (g/W)", 'fontsize', 20);
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        title(titulo{1,1}, 'fontsize', 26)
        
        hold on
        x_axis = 0;
        y_axis = 0;
    end

    legend(nomes,'fontsize',26)
    print(['graficos/' titulo{1,1} ' EExPT-M.png'],'-dpng')

    j=1;
    figure(4)

    %XY - Peso empuxo x Peso total ( Curvas de motor )
    for i = 1:6:(motores*6)
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+2);
        plot(x_axis,y_axis,cores{j,1});
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel("Peso-Empuxo", 'fontsize', 20);
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        title(titulo{1,1}, 'fontsize', 26)
        
        hold on
        x_axis = 0;
        y_axis = 0;
    end

    legend(nomes,'fontsize',26)
    print(['graficos/' titulo{1,1} ' PExPT-M.png'],'-dpng')

    j=1;
    figure(5)
    %XY - velocidade_max X Peso total

    for i = 1:6:(motores*6)
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+5);
        plot(x_axis,y_axis,cores{j,1});
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel("Velocidade MAX (km/h)", 'fontsize', 20);
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        title(titulo{1,1}, 'fontsize', 26)
        
        hold on
        x_axis = 0;
        y_axis = 0;
    end

    legend(nomes,'fontsize',26)
    print(['graficos/' titulo{1,1} ' velxPT-M.png'],'-dpng')

    
    %YY - Tempo de voo, Peso empuxo X Peso total 
    b=1;
    for i = 1:6:(motores*6)
        figure(5+i)
        
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+1);
        y2_axis = all_data(:,i+2);

        ax = plotyy(x_axis,y_axis,x_axis,y2_axis);
        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel(ax(1)," Tempo de voo (min)",'fontsize',20)
        ylabel(ax(2)," Peso-Empuxo",'fontsize',20)
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        set(ax(1),"YTick",y_axis)
        set(ax(2),"YTick",y2_axis)
        title(nomes{1,b}, 'fontsize', 26)
        print(['graficos/' titulo{1,1} ' TV,PExPT-YY ' nomes{1,b} '.png'],'-dpng')
        x_axis = 0;
        y_axis = 0;
        b++;
    end

    

    %YY - Peso empuxo, Empuxo específico X Peso total
    b=1;
    for i = 1:6:(motores*6)
        figure(7+i)
        
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+2);
        y2_axis = all_data(:,i+3);

        ax = plotyy(x_axis,y_axis,x_axis,y2_axis);

        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel(ax(1),"Peso-Empuxo",'fontsize',20)
        ylabel(ax(2),"Empuxo Especifico (g/W)",'fontsize',20)
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        set(ax(1),"YTick",y_axis)
        set(ax(2),"YTick",y2_axis)
        title(nomes{1,b}, 'fontsize', 26)
        print(['graficos/' titulo{1,1} ' PE,EExPT-YY ' nomes{1,b} '.png'],'-dpng')

        x_axis = 0;
        y_axis = 0;

        b++;
    end

    %%YY - Tempo de voo, Empuxo Especifico x Peso Total
    b=1;
    for i = 1:6:(motores*6)
        figure(9+i)
        
        x_axis = all_data(:,i);
        y_axis = all_data(:,i+1);
        y2_axis = all_data(:,i+3);

        ax = plotyy(x_axis,y_axis,x_axis,y2_axis);

        grid on
        j++;
        xlabel("Peso Total (g)", 'fontsize', 20);
        ylabel(ax(1),"Tempo de voo (min)",'fontsize',20)
        ylabel(ax(2),"Empuxo Especifico (g/W)",'fontsize',20)
        set(gcf, 'Position', get(0, 'ScreenSize'))
        set(gca, "XTick", x_axis(1):espacamento:x_axis(end));
        set(ax(1),"YTick",y_axis)
        set(ax(2),"YTick",y2_axis)
        title(nomes{1,b}, 'fontsize', 26)
        print(['graficos/' titulo{1,1} ' TV,EExPT-YY ' nomes{1,b} '.png'],'-dpng')
        x_axis = 0;
        y_axis = 0;
        b++;

    end

close all
end