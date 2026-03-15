
# FIX: Copilot agent added the 4 functions from app.py for better structure
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

# FIX: Copilot added this new function to return the diffuclty


def get_attempt_limit(difficulty: str):
    """Return the number of attempts allowed for a given difficulty."""
    limits = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    return limits.get(difficulty, 8)


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Directed Copilot to what the issue was and it fixed the go lower and go higher hints


def check_guess(guess, secret):
    # Normalize the secret value to an int when possible so comparisons stay numeric.
    try:
        secret_value = int(secret)
    except Exception:
        secret_value = secret

    if guess == secret_value:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret_value:
            # Guess is higher than secret, so tell player to go lower.
            return "Too High", "📉 Go LOWER!"
        else:
            # Guess is lower than secret, so tell player to go higher.
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # Fallback to string comparisons if we still can't compare as numbers.
        g = str(guess)
        s = str(secret)
        if g == s:
            return "Win", "🎉 Correct!"

        try:
            if int(g) > int(s):
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"
        except Exception:
            if g > s:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

# FIX: Copilot added a new function to reset the game when the new game button is clicked


def reset_game_state(difficulty: str):
    """Reset the game state for a new game with the given difficulty."""
    import random
    low, high = get_range_for_difficulty(difficulty)
    return {
        'secret': random.randint(low, high),
        'attempts': 0,
        'score': 0,
        'status': 'playing',
        'history': []
    }
