# SUM OF MULTIPLES

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    else:
        return sum(i for i in range(n,m,n))
print(sum_mul(2,9))

# GRASSHOPPER COMBINED STRINGS
def combine_names(fname,sname):
    fullname = (fname,sname)
    return " ".join(fullname)

print(combine_names("adriano","suprine"))

# GRASSHOPER -IF/ELSE SYNTAX DEBUG

# BDD input health - output boolean value
# pseudocode 
# start
#   take in the parameter 
#   check in the conditional statement
#   return boolean value
# stop

def check_alive(health):
    if health <= 0 :
        return False
    else:
        return True
print(check_alive(-80))    
