from sympy.combinatorics.permutations import Permutation
from sympy.combinatorics import PermutationGroup

# Given permutations
alpha_beta = Permutation([1, 3, 2, 0])
beta_alpha = Permutation([3, 0, 1, 2])

# Since alpha_beta and beta_alpha are known, we can find alpha and beta
# We know that alpha_beta = alpha * beta and beta_alpha = beta * alpha
# Also, we know that alpha(2) = 1 (considering the position starts from 1 in mathematical notation)

# To find alpha, we first find the inverse of beta (beta_inv) from beta_alpha
# Since beta_alpha = beta * alpha, then beta_inv = alpha * beta_alpha_inv
beta_alpha_inv = beta_alpha**-1
# We have alpha(2) = 1, which means alpha = (*, 1, *, *) where * are the unknowns

# We will iterate over all possible permutations of S4
# and find the one that satisfies both alpha_beta and alpha(2) = 1
s4 = PermutationGroup([Permutation([1, 0, 2, 3]), Permutation([0, 2, 1, 3]),
                       Permutation([0, 1, 3, 2])])

# Define a function to check if a given permutation alpha satisfies the conditions
def check_alpha(alpha, alpha_beta, beta_alpha_inv):
    beta = alpha_beta * alpha**-1
    beta_inv = alpha * beta_alpha_inv
    return beta == beta_inv

# Find alpha and beta
for alpha in s4.generate_schreier_sims():
    # Check if alpha(2) = 1
    if alpha(1) == 0:
        # Check if alpha satisfies the conditions
        if check_alpha(alpha, alpha_beta, beta_alpha_inv):
            # If it does, then we have found our alpha and can calculate beta
            beta = alpha_beta * alpha**-1
            break

# Display alpha and beta in cycle notation
alpha_cycle = alpha.cyclic_form if alpha else None
beta_cycle = beta.cyclic_form if beta else None

alpha_cycle, beta_cycle