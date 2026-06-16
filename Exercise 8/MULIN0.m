function p_hat = MULIN0(P)
    n = length(P);
    p_hat = zeros(1, n);

    p_hat(1) = P(1);
    p_hat(2) = P(2);
    for i = 2 : n - 1
        p_hat(i + 1) = 2 * P(i) - P(i-1);
    end
end
