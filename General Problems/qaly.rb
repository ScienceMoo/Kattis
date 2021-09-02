N = gets.chomp.to_i

sum = 0

N.times {
    nums = gets.chomp.split(" ").map {|x| x.to_f}
    sum += nums[0] * nums[1]
}

puts sum