#from test import add
#https://www.youtube.com/watch?v=GxCXiSkm6no
#IMPORT YOUR IMPORT MODULES PROPERLY
from module import *
from module.equationResolver import *

# ctrl+F -> find
# ctrl+R -> replace
# ctrl+Q -> show documentation
'''
def add(a, b):
    return a + b + a + b


print("adding:", add(1, 2))



#initial_string = "(2+1)-4.3*7-2.5+4*(2+1)*(sin30+tan12+(ctg0+cos39)*(1-2)-sqr2)-3%2"
initial_string = "(2+1)-4.3*7-2.5+4*(2+1)*(sin30+tan12+(ctg0+cos39)*(1-2)-3!)-3^2"
a = find_parenthesis(initial_string)
print("find parenthesis: ", a)
#error = find_parenthesis("4.3*7-2.5+4)*(2+1)*(sin30+tan12+(ctg0+cos39)-sqr2)-3%2")

print("min_distance(a)=", get_min_distance_index_list(a))

#test string with no parenthesis:
no_par_string = "4.3*7-2.5+4"
b = find_parenthesis(no_par_string)
print("find parenthesis (empty): ", b)
if len(b[0]) == len(b[1]) == 0:
    pass  #compute
else:
    print("min_distance(a)=", get_min_distance_index_list(a))
    #do cut_and_compute

#list with indexes to cut
index_lst = get_min_distance_index_list(a)

#print("cut_and_compute", cut_and_compute(initial_string, index_lst))



while '(' in initial_string or ')' in initial_string:
    parenthesis_indexes_all = find_parenthesis(initial_string)
    #print("parenthesis_indexes_all",parenthesis_indexes_all)
    closest_parenthesis_indexes = get_min_distance_index_list(parenthesis_indexes_all)
    #print("closest_parenthesis_indexes",closest_parenthesis_indexes)
    initial_string = cut_and_compute(initial_string, closest_parenthesis_indexes)
    #print("initial_string",initial_string)
print(initial_string)

#compute_trigon("sin45+cos30+45+tan190+ctg15")

#compute_factorial("3!++7+8*2-2!+1-2!+3!")
print("\n---multiply---")
#conduct_multiplication("2+33+5*4*2+4/-2+5*6")
conduct_multiplication("5*6+7*5-4*2/2*8")

conduct_multiplication("30.0+35.0/5*2-8.0/2*8")

a = conduct_addition(conduct_multiplication(conduct_exponentiation("30.0+-35.0/+-5*2-8.0/2*8*2^10")))
print(a)

'''
print("===========FINAL TESTING===============")
initial_string_final = "(2+1)-4.3*7-2.5+4*(2+1)*(sin30+tan12+(ctg10+cos39)*(1-2)-3!)-3^2"

#a = compute_equation(initial_string_final)
#print(a)

#b = compute_equation("-5+10^2!*sin23+30.0+5*6")
#print(b)

c = compute_equation("(2+1)-4.3*7-2.5+4*(2+1)*(sin30+tan12+(ctg10+cos39)*(1-2)-3!)-3^2")
print(c)

#d = compute_equation("0.49999999999999994+0.2125565616700221+-6.44842778107468-6")
#print(d)

#e = compute_equation("3.0-4.3*7-2.5+4*3.0*-11.7-3^2")
#print(e)

f = compute_equation("abc")
print(f)
