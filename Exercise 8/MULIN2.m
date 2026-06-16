function p_hat = MULIN2(P)    
    n = length(P);
    p_hat = zeros(1, n);

    p_hat(1) = P(1);
    p_hat(2) = P(2);
    p_hat(3) = P(3);
    p_hat(4) = P(4);

    for i = 4 : n - 1
        p_hat(i + 1) = 5 * P(i) - 8 * P(i - 1) + 5 * P(i - 2) - P(i - 3);
    end
end