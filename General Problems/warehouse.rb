T = gets.chomp.to_i

for i in 0...T
    N = gets.chomp.to_i
    warehouse = Hash.new(0)
    N.times do
        line = gets.chomp.split(" ")
        warehouse[line[0]] += line[1].to_i
    end
    puts warehouse.length
    warehouse = warehouse.sort_by {|k, v| [-v, k]}
    warehouse.each { |k, v| puts "#{k} #{v}"}
end

