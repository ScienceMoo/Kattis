n = gets.chomp.to_i
m = gets.chomp.to_i

if (n - m).abs == 180
    puts 180
elsif n > m
    x = n - m
    y = (360 - n) + m
    puts x < y ? m - n : y
elsif m > n
    x = m - n
    y = (360 - m) + n
    puts x < y ? m - n : - y
else
    puts 0
end