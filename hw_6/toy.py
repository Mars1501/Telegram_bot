import field as f
import game as g

sign_empty = '.'
sign_x = 'x'
sign_o = 'o'
my_field = []

f.init_field(my_field, sign_empty)
f.print_field(my_field)
g.run_game(my_field, sign_empty, sign_x, sign_o)