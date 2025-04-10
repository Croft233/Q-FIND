clc 
clear all;
close all;
delete *.fig

file_SD = sprintf("1_times_FvsT_Resulty.txt");
file_SD_ID = fopen(file_SD,'r');
formatSpec = '%f %f %f %f %f %f %f %f';
data_SD = textscan(file_SD_ID,formatSpec);
mydata_SD =cell2mat(data_SD);
fclose(file_SD_ID);
 
Th1 = mydata_SD(1, 1:8);
Th2 = mydata_SD(2, 1:8);
F1 = mydata_SD(3, 1:8);
F2 = mydata_SD(4,1:8);
fth = [0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9];


figure(1)
plot(fth, Th1,'-o','Color','r','MarkerFaceColor','r', 'LineWidth', 2);
hold on;
plot(fth, Th2,'-s','Color','b','MarkerFaceColor','b', 'LineWidth', 2);
hold on;

set(gca,'XLim',[0.55 0.9]); 
set(gca,'XTick',[0.55:0.05:0.9]);
set (gca, 'FontSize', 15 ); 


set(gca,'YLim',[0 50]); 
set(gca,'YTick',[0:5:50]);
xlabel('Fidelity Threshold', 'FontSize', 20)
ylabel('Throughput (qubits/slot)', 'FontSize', 20)
% legend('E2E Q-Path','E2E Q-Leap','SD Q-Path','SD Q-Leap','Location','NE');
legend('Q-PATH','Q-LEAP','Location','SW', 'FontSize', 15);
grid on
pbaspect([4 3 1])

% figure(2)
% plot(fth, F1,'--o','Color','k','MarkerFaceColor','W');
% hold on;
% plot( fth,F2,'--s','Color','b','MarkerFaceColor','b');
% hold on;
% set(gca,'XLim',[0.55 0.9]); 
% set(gca,'XTick',[0.55:0.05:0.9]);
% 
% set(gca,'YLim',[0.6 1.00]); 
% set(gca,'YTick',[0.6:0.05:1.00]);
% xlabel('Fidelity Threshold', 'FontSize', 25)
% ylabel('Average Fidelity', 'FontSize', 25)
% legend('SD Q-Path','SD Q-Leap','Location','NE');
% grid on
% pbaspect([4 3 1])

% file_E2E = sprintf("E2EPath_vs_Fidelity.txt");
% file_SD = sprintf("Single_SDPair_vs_Fidelity.txt");
% file_E2E_ID = fopen(file_E2E,'r');
% file_SD_ID = fopen(file_SD,'r');
% formatSpec = '%f %f %f %f %f %f %f %f %f %f %f';
% data_E2E = textscan(file_E2E_ID,formatSpec);
% data_SD = textscan(file_SD_ID,formatSpec);
% mydata_E2E = cell2mat(data_E2E);
% mydata_SD =cell2mat(data_SD);
% fclose(file_E2E_ID);
% fclose(file_SD_ID);
% 
% fth_E2E = mydata_E2E(1:8,1);
% Throughput2_E2E = mydata_E2E(1:8, 7);
% Fidelity_E2E = mydata_E2E(1:8,3);
% Throughput_E2E = mydata_E2E(1:8,2);
% 
% fth_SD = mydata_SD(1:8,1);
% Throughput2_SD = mydata_SD(1:8, 7);
% Fidelity_SD = mydata_SD(1:8,3);
% Throughput_SD = mydata_SD(1:8,2);
% Fidelity2_SD = mydata_SD(1:8,8);
% 
% figure(1)
% plot(fth_E2E, Throughput_E2E,'-o','Color','k','MarkerFaceColor','k');
% hold on;
% plot(fth_E2E, Throughput2_E2E,'-s','Color','b','MarkerFaceColor','b');
% 
% set(gca,'XLim',[0.55 0.9]); 
% set(gca,'XTick',[0.55:0.05:0.9]);
% 
% set(gca,'YLim',[3.5 6.5]); 
% set(gca,'YTick',[3.5:0.5:6.5]);
% xlabel('Fidelity Threshold', 'FontSize', 15)
% ylabel('Throughput (qubits/slot)', 'FontSize', 15)
% legend('Q-Path','Q-Leap','Location','SW');
% grid on
% pbaspect([4 3 1])
% fig_n = sprintf('fig01.fig');
% fig_n1 = sprintf('fig01.png');
% fig_n2 = sprintf('fig01.eps');
% saveas(gcf,fig_n)
% saveas(gcf,fig_n1)
% saveas(gcf,fig_n2)
% 
% figure(2)
% % plot(fth_E2E, Throughput_E2E,'-o','Color','k','MarkerFaceColor','k');
% % hold on;
% % plot(fth_E2E, Throughput2_E2E,'-x','Color','b','MarkerFaceColor','b');
% % hold on;
% plot(fth_SD, Throughput_SD,'--o','Color','k','MarkerFaceColor','W');
% hold on;
% plot(fth_SD, Throughput2_SD,'--s','Color','b','MarkerFaceColor','b');
% hold on;
% 
% set(gca,'XLim',[0.55 0.9]); 
% set(gca,'XTick',[0.55:0.05:0.9]);
% 
% set(gca,'YLim',[0 50]); 
% set(gca,'YTick',[0:5:50]);
% xlabel('Fidelity Threshold', 'FontSize', 15)
% ylabel('Throughput (qubits/slot)', 'FontSize', 15)
% % legend('E2E Q-Path','E2E Q-Leap','SD Q-Path','SD Q-Leap','Location','NE');
% legend('SD Q-Path','SD Q-Leap','Location','SW');
% grid on
% pbaspect([4 3 1])
% fig_n = sprintf('fig02.fig')
% fig_n1 = sprintf('fig02.png')
% fig_n2 = sprintf('fig02.eps')
% saveas(gcf,fig_n)
% saveas(gcf,fig_n1)
% saveas(gcf,fig_n2)
% 
% figure(3)
% plot(fth_SD, Fidelity_SD,'--o','Color','k','MarkerFaceColor','W');
% hold on;
% plot( fth_SD,Fidelity2_SD,'--s','Color','b','MarkerFaceColor','b');
% hold on;
% set(gca,'XLim',[0.55 0.9]); 
% set(gca,'XTick',[0.55:0.05:0.9]);
% 
% set(gca,'YLim',[0.6 1.00]); 
% set(gca,'YTick',[0.6:0.05:1.00]);
% xlabel('Fidelity Threshold', 'FontSize', 15)
% ylabel('Average Fidelity', 'FontSize', 15)
% legend('SD Q-Path','SD Q-Leap','Location','NE');
% grid on
% pbaspect([4 3 1])