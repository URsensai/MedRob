clear; clc; close all;
load('test_resp.mat'); 
vars = whos;
fprintf('Variables in test_resp.mat:\n');
for i = 1:length(vars)
    fprintf('  %s (size: %s)\n', vars(i).name, mat2str(vars(i).size));
end

if ~exist('y', 'var')
    signal_name = vars(1).name;
    y = eval(signal_name);
    fprintf('\nUsing variable: %s\n', signal_name);
end

y = y(:);

mu_values = [0.0001, 0.0002, 0.001];
M_values = [2, 4, 8];
rms_results = zeros(length(M_values), length(mu_values));

fprintf('\n========== LMS RESULTS ==========\n');
fprintf('   M   |    mu    |     RMS    \n');
fprintf('--------------------------------\n');

for i = 1:length(M_values)
    current_M = M_values(i);
    for j = 1:length(mu_values)
        current_mu = mu_values(j);

        [pred, err] = LMS_algorithm(y, current_mu, current_M);

        valid_err = err(current_M + 1 : end);
        rms_val = sqrt(mean(valid_err.^2));

        rms_results(i, j) = rms_val;
        fprintf('   %d   |  %.4f   |   %.6f\n', current_M, current_mu, rms_val);
    end
end
fprintf('--------------------------------\n');

[min_rms, idx] = min(rms_results(:));
[best_M_idx, best_mu_idx] = ind2sub(size(rms_results), idx);
fprintf('BEST: M=%d, mu=%.4f, RMS=%.6f\n', M_values(best_M_idx), mu_values(best_mu_idx), min_rms);
fprintf('================================\n\n');

figure('Name', 'LMS Predictions - All Combinations', 'Position', [100, 100, 1400, 900]);
plot_idx = 1;
for i = 1:length(M_values)
    for j = 1:length(mu_values)
        [pred, ~] = LMS_algorithm(y, mu_values(j), M_values(i));

        subplot(length(M_values), length(mu_values), plot_idx);
        plot(y, 'b-', 'LineWidth', 1); hold on;
        plot(pred, 'r--', 'LineWidth', 1);

        xlim([M_values(i) + 1, min(length(y), M_values(i) + 500)]); 

        xlabel('Sample Number');
        ylabel('Position');
        title(sprintf('M=%d, \\mu=%.4f, RMS=%.4f', M_values(i), mu_values(j), rms_results(i, j)));
        legend('Original', 'Predicted', 'Location', 'best');
        grid on;

        plot_idx = plot_idx + 1;
    end
end
sgtitle('Exercise 2b: LMS Prediction on Respiratory Data');