numbers = gets.chomp.split(" ").map {|x| x.to_i}.sort
puts numbers[0].to_s + " " + numbers[1].to_s
