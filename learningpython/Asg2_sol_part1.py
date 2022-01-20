# use this approach instead
# simply append your google drive path to the system path 
# and then import it the "normal way"
import sys
sys.path.append("/content/drive/MyDrive/Colab Notebooks/")

from learningpython.Perceptron import Perceptron
from learningpython.Perceptron import perceptron_unit_test
print("Part 1 solution")
perceptron_unit_test()

print("Part 2 solution")
p1 = Perceptron([-2, -2], 3)
p2 = Perceptron([-2, -2], 3)
p3 = Perceptron([-2, -2], 3)
p4 = Perceptron([-2, -2], 3)
p5 = Perceptron([-2, -2], 3)
allinputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
for input in allinputs:
  p1out = p1.evaluate(input)
  p2out = p2.evaluate([input[0], p1out])
  p3out = p3.evaluate([p1out, input[1]])
  carry = p4.evaluate([p1out, p1out])
  sum = p5.evaluate([p2out, p3out])
  print(f"{input[0]}+{input[1]}={carry}{sum}")