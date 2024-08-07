me - Maria and Ben are playing a game."""


def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds to play.
        nums (list): List of integers representing the upper limit
            of the set for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
        None: If the winner cannot be determined.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    for n in nums:
        prime_count = sum(is_prime[: n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None
