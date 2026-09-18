import os
def test_scripts_exist():
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "..", "scripts", "overview.py"))
