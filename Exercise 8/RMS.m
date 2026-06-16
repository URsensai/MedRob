function rms_val = RMS(original, predicted)
    diff = original - predicted;
    rms_val = sqrt(mean(diff.^2));
end
