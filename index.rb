#Given an array of numbers, your function should return an array of arrays, 
#where each subarray contains all the duplicates of a particular number. 
#Subarrays should be in the same order as the first occurence of the number they contain:
#group([3, 2, 6, 2, 1, 3])
#>>> [[3, 3], [2, 2], [6], [1]]
#Assume the input is always going to be an array of numbers. 
#If the input is an empty array, an empty array should be returned.

def group(arr)
    result = []
  
    arr.each do |num|
      found = false

      result.each do |subarray|
        if subarray[0] == num
          subarray << num
          found = true
          break
        end
      end
      result << [num] unless found
    end
  
    result
  end
  
  puts group([3, 2, 6, 2, 1, 3]).inspect
   