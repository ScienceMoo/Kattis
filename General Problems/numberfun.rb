N = gets.chomp.to_i

N.times {
    possible = false
    nums = gets.chomp.split(" ").map {|x| x.to_i}
    if nums[0] * nums[1] == nums[2]
        possible = true
    elsif nums[0] + nums[1] == nums[2]
        possible = true
    elsif (nums[0] - nums[1]).abs == nums[2]
        possible = true
    elsif nums[0] / nums[1] == nums[2] and nums[0] % nums[1] == 0
        possible = true
    elsif nums[1] / nums[0] == nums[2] and nums[1] % nums[0] == 0
        possible = true
    end
    puts possible ? "Possible" : "Impossible" 
}