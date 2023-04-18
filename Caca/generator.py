import random
import string

"https://www.spotify.com/us/redeem/?_ga=2.156295675.1149674389.1680169861-1451346293.1677844914&_gac=1.159332552.1677844979.Cj0KCQiA0oagBhDHARIsAI-BbgeM0jpbkX7fT3J_arWQFBbDEBuTBlS-4RqqUQ-74GKLgA0NxZzlj10aAkYqEALw_wcB"
finnish = 10
n_fin = 0

while finnish != n_fin:

    with open("gc_gen.txt", "w") as gen_file:
        for i in range(10):
            gen_file.write(random.choice(string.ascii_letters + string.digits))

    n_fin += 1