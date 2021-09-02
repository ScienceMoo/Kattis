words = gets.chomp.split(" ")
dict = {}

repeats = false
for i in 0...words.length
    word = words[i]
    if dict[word] == nil 
        dict[word] = word 
    else 
        repeats = true 
        break
    end
end

puts repeats ? "no" : "yes"