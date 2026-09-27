# Experiment 6
# 0/1 Knapsack Problem
# Using Bottom-Up and Top-Down Dynamic Programming

# Bottom-Up Approach
def knapsack_bottom_up(values, weights, capacity):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                # Include or exclude the item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                # Item cannot be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Top-Down Approach using Memoization
def knapsack_top_down(values, weights, capacity):
    n = len(values)

    # Create memoization table
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(n, capacity):

        # Base condition
        if n == 0 or capacity == 0:
            return 0

        # Return already calculated result
        if memo[n][capacity] != -1:
            return memo[n][capacity]

        # If item weight is greater than capacity
        if weights[n - 1] > capacity:
            memo[n][capacity] = solve(n - 1, capacity)

        else:
            # Include the item
            include = values[n - 1] + solve(
                n - 1, capacity - weights[n - 1]
            )

            # Exclude the item
            exclude = solve(n - 1, capacity)

            memo[n][capacity] = max(include, exclude)

        return memo[n][capacity]

    return solve(n, capacity)


# Main Program
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("0/1 Knapsack Problem")
print("--------------------")

print("Values :", values)
print("Weights:", weights)
print("Capacity:", capacity)

bottom_up_result = knapsack_bottom_up(values, weights, capacity)
top_down_result = knapsack_top_down(values, weights, capacity)

print("\nBottom-Up Result:", bottom_up_result)
print("Top-Down Result :", top_down_result)
