clear; clc; close all;

t = 0:0.05:20;
P = sin(t + 0.2014);

pred0 = MULIN0(P);
pred1 = MULIN1(P);
pred2 = MULIN2(P);

rmse0 = RMS(P, pred0);
rmse1 = RMS(P, pred1);
rmse2 = RMS(P, pred2);

figure;

subplot(3, 1, 1);
plot(t, P, 'k-', t, pred0, 'r:', 'LineWidth', 1.5);
title(sprintf('MULIN0 Prediction (RMSE: %.5f)', rmse0));
ylabel('Position');
legend('Ground Truth', 'MULIN0');
grid on;

subplot(3, 1, 2);
plot(t, P, 'k-', t, pred1, 'g--', 'LineWidth', 1.5);
title(sprintf('MULIN1 Prediction (RMSE: %.5f)', rmse1));
ylabel('Position');
legend('Ground Truth', 'MULIN1');
grid on;

subplot(3, 1, 3);
plot(t, P, 'k-', t, pred2, 'b-.', 'LineWidth', 1.5);
title(sprintf('MULIN2 Prediction (RMSE: %.5f)', rmse2));
xlabel('Time (t)');
ylabel('Position');
legend('Ground Truth', 'MULIN2');
grid on;

fprintf('RMSE for MULIN0: %.8f\n', rmse0);
fprintf('RMSE for MULIN1: %.8f\n', rmse1);
fprintf('RMSE for MULIN2: %.8f\n', rmse2);