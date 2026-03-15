from logic_utils import check_guess, get_attempt_limit, reset_game_state


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

# Additional tests targeting the high/low bug fix


def test_guess_too_high_message_correct():
    # Specifically test that high guess gives "Go LOWER!" hint
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_message_correct():
    # Specifically test that low guess gives "Go HIGHER!" hint
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_too_high_with_string_secret():
    # Test fallback when secret is a string (as in the buggy app logic)
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_with_string_secret():
    # Test fallback when secret is a string
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# Tests for new game reset and attempt limits


def test_attempt_limit_normal():
    # Normal difficulty should allow 8 attempts
    assert get_attempt_limit("Normal") == 8


def test_attempt_limit_easy():
    assert get_attempt_limit("Easy") == 6


def test_attempt_limit_hard():
    assert get_attempt_limit("Hard") == 5


def test_reset_game_state_normal():
    # Test that resetting for Normal difficulty initializes state correctly
    state = reset_game_state("Normal")
    assert state['attempts'] == 0
    assert state['score'] == 0
    assert state['status'] == 'playing'
    assert state['history'] == []
    # Secret should be between 1 and 100
    assert 1 <= state['secret'] <= 100


def test_reset_game_state_easy():
    state = reset_game_state("Easy")
    assert 1 <= state['secret'] <= 20


def test_reset_game_state_hard():
    state = reset_game_state("Hard")
    assert 1 <= state['secret'] <= 50
