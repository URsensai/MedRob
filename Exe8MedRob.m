t = 0:0.05:29.95;
P = sin(t + 0.2014);

R = zeros(1,length(P));

R(1) = P(1);

for i = 2:length(P)
    R(i) = P(i - 1);
end

def 
plot(t, P, t, R)