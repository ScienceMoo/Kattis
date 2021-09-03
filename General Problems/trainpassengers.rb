line1 = gets.chomp.split(" ").map(&:to_i)
C = line1[0]
n = line1[1]

current = 0
possible = false

for i in 0...n
    line = gets.chomp.split(" ").map(&:to_i)
    left = line[0]
    enter = line[1]
    waiting = line[2]

    current += enter
    current -= left

    if current < 0
        break
    elsif i == n-1 and (enter > 0 or waiting > 0 or current > 0)
        break
    elsif i == n-1
        possible = true
        break
    end
    
    if current < C and waiting > 0
        break
    elsif current < 0 or current > C
        break
    end
end

puts possible ? "possible" : "impossible"