line = gets.chomp.split(" ").map(&:to_f)

X = line[0]
Y = line[1]

if X == 0 
    if Y == 1
        puts "ALL GOOD"
    else
        puts 0
    end
elsif Y == 1
    puts "IMPOSSIBLE"
else
    puts X / (1-Y)
end
