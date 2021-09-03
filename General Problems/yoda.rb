n = gets.chomp.chars.map(&:to_i).reverse
m = gets.chomp.chars.map(&:to_i).reverse

i = 0
new_n = []
new_m = []
while i < n.length or i < m.length do
    if i >= n.length
        new_m.push(m[i])
    elsif i >= m.length
        new_n.push(n[i])
    elsif n[i] > m[i]
        new_n.push(n[i])
    elsif n[i] < m[i]
        new_m.push(m[i])
    else
        new_n.push(n[i])
        new_m.push(m[i])
    end
    i += 1;
end

puts new_n.length > 0 ? new_n.reverse.join.to_i : "YODA"
puts new_m.length > 0 ? new_m.reverse.join.to_i : "YODA"
