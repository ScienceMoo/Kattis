def is_digit?(s)
    code = s.ord
    48 <= code && code <= 57
end

S = gets.chomp
P = gets.chomp

n = S.length
acceptable = false

if P == S or S.swapcase == P or (is_digit?(S[0]) and S[1...n] == P) or (is_digit?(S[n-1]) and S[0...n-1] == P)
    acceptable = true
end

puts acceptable ? "Yes" : "No"