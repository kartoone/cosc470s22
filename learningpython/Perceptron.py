class Perceptron:
  def __init__(self, w, b):
    self.weights = w      # be sure that w is a "new" list for each Perceptron when you instantiate!
    self.bias = b         # be sure that b isn't somehow an object that can be shared, it should be a raw number or reference to variable that is itself a raw number (not some sort of number object)
  
  # i should have same length as our list of weights
  # returns a 0 if the weighted sum of inputs plus bias <= 0
  # returns a 1 if the weighted sum of inputs plus bias > 0
  def evaluate(self, inputs):
    if len(inputs) != len(self.weights):
      raise Exception(f"incorrect number of inputs, expecting {len(self.weights)}, but received {len(inputs)}." )
    sum = 0
    for index, i in enumerate(inputs):
      sum = sum + i*self.weights[index]
    return 0 if sum+self.bias <= 0 else 1

def perceptron_unit_test():
    p1 = Perceptron([-2,-2],3)
    inputcombos = [[0, 0], [0, 1], [1, 0], [1, 1]]
    for input in inputcombos:
      print(f"{input[0]} nand {input[1]} = {p1.evaluate(input)}")