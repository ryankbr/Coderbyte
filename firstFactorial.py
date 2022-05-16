def FirstFactorial(num):

  # code goes here
  # factorial of 1 or 0 returns 1
  if num < 2:
    return 1
  
  #factorial is num * firstfactorial(num-1)
  num *= FirstFactorial(num - 1)

  return num

# keep this function call here 
print(FirstFactorial(input()))
