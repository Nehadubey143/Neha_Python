# break and continue :-

# break : -
# => if the given condition is true in that case we exit from loop immediatly.

from typing import Final


for i in range(6):
                    print(i) # 0,1,2,3,4,5


# ---------------------------------------------

for i in range(6):
                    if i == 3:
                                        break
                    print(i)


# i = 0 

# 0 == 3 => False   # 0
# 1 == 3 => False   # 1
# 2 == 3 => False   # 2
# 3 == 3 => False   # Break

# ---------------------------------------------

# ## Continue :- 
# => if the given condition is true , in that case only we skip the current elemnt and move to the next element. 

for i in range(6):
                    if i == 3:
                                        continue
                    print(i)

# i = 0 
# condition => i == 3
# 0 == 3 => False  # 0 
# 1 == 3 => False  # 1
# 2 == 3 => False  # 2 
# 3 == 3 => TRUE  # Continue => ( we skip the current element )

# 4,5
# Final Output => 0,1,2,4,5