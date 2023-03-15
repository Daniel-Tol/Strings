# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1 

# 1
scorer_name_0 = "Ruud Gullit"
scorer_name_1 = "Marco van Basten"
print(scorer_name_0)
print(scorer_name_1)

# 2
goal_0 = 32
goal_1 = 54
print(goal_0)
print(goal_1)

# 3
scorers = scorer_name_0 + " " + str(goal_0) + ", " + scorer_name_1 + " " + str(goal_1)
print(scorers)

# 4
report = scorer_name_0 + " scored in the " + str(goal_0) + "nd minute" + "\n" + scorer_name_1 + " scored in the " + str(goal_1) + "th minute"
print(report)

# Part 2

# 1
player = "Hans van Breukelen"
print(player)

# 2
find_last_name = player.find("van Breukelen")
first_name = player[:find_last_name - 1]
print(first_name)

# 3
last_name = player[find_last_name:]
last_name_len = len(last_name)
print(last_name_len)

# 4
name_short = first_name[:1] + ". " + last_name
print(name_short)

# 5
first_name_len = len(first_name)
chant_space = (first_name + "! ") * first_name_len
chant = chant_space[:-1]
print(chant)

# 6 
good_chant = chant[-1:] != " "
print(good_chant)