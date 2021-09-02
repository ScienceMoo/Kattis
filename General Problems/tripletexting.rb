text = gets.chomp

N = text.length

word_length = N / 3
dict = {}

words = text.chars.each_slice(word_length).map(&:join)

result = ""
words.each do |word|
    if dict[word] == nil
        dict[word] = word
    else
        result = word  
    end
end

puts result