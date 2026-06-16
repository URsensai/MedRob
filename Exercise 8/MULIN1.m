function p_hat = MULIN1(P)
    n = length(P);
    p_hat = zeros(1, n);
    
    % Warm-up assignments for the first 3 elements
    p_hat(1) = P(1);
    p_hat(2) = P(2);
    p_hat(3) = P(3);
    
    % Shift start index to 3 so p_hat(4) is computed
    for i = 3 : n - 1
        p_hat(i + 1) = 3 * P(i) - 3 * P(i-1) + P(i-2);
    end
end
