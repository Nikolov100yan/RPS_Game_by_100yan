from rps_game import determine_result


def test_determine_result():
    assert determine_result("r" , "s") == "win"
    assert determine_result("r", "p") == "loss"
    assert determine_result("r", "r") == "tie"

    assert determine_result("p", "r") == "win"
    assert determine_result("s", "p") == "win"

    print("All tests passed!")