function [predictions, errors] = LMS_algorithm(y, mu, M)
y = y(:);
n_total = length(y);

predictions = zeros(n_total, 1);
errors = zeros(n_total, 1);

w = zeros(M, 1); 
w(end) = 1.0; 

predictions(1) = y(1);
errors(1) = 0;

for n = M : (n_total - 1)

    u = y(n - M + 1 : n);

    predictions(n + 1) = w' * u;

    errors(n) = y(n) - predictions(n);

    if n > M
        u_past = y(n - M : n - 1);
        w = w + mu * errors(n) * u_past;
    end
end

errors(n_total) = y(n_total) - predictions(n_total);
end