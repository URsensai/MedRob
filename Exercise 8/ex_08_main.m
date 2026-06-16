clear; clc; close all;

% Part (a)  Plot patient positions accoding to question
t = 0:0.05:2;
P = sin(t + 0.2014);

pred0 = MULIN0(P);
pred1 = MULIN1(P);
pred2 = MULIN2(P);

rmse2 = RMS(P, pred2);
rmse0 = RMS(P, pred0);
rmse1 = RMS(P, pred1);

% Display RMSE values for each prediction method
fprintf('RMSE for MULINO: %.8f\n', rmse0);
fprintf('RMSE for MULIN1: %.8f\n', rmse1);
fprintf('RMSE for MULIN2: %.8f\n', rmse2);