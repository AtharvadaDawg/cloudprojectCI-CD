import os
import sys

def test_hello_world():
    hw_dir = os.path.join(os.path.dirname(__file__), "hello_world")
    sys.path.insert(0, hw_dir)
    import main as hw_main
    client = hw_main.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, World!" in resp.data
    print("[PASS] hello_world test: Status 200, Content verified.")
    sys.path.pop(0)
    del sys.modules["main"]

def test_simple_web_app():
    sw_dir = os.path.join(os.path.dirname(__file__), "simple_web_app")
    sys.path.insert(0, sw_dir)
    import main as sw_main
    client = sw_main.app.test_client()
    
    # 1. Test GET /
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Google App Engine Web Suite" in resp.data
    print("[PASS] simple_web_app GET /: Status 200")
    
    # 2. Test POST /grade-calculator
    resp_grade = client.post("/grade-calculator", data={
        "student_name": "Atharva",
        "roll_number": "CC-08",
        "subject1": "85",
        "subject2": "90",
        "subject3": "88",
        "subject4": "92"
    })
    assert resp_grade.status_code == 200
    assert b"Atharva" in resp_grade.data
    assert b"355.0 / 400" in resp_grade.data
    assert b"88.75%" in resp_grade.data
    print("[PASS] simple_web_app POST /grade-calculator: Status 200, Grade calculated correctly")
    
    # 3. Test POST /text-analyzer
    resp_text = client.post("/text-analyzer", data={
        "user_text": "Cloud Computing on Google App Engine"
    })
    assert resp_text.status_code == 200
    assert b"Total Words:" in resp_text.data
    assert b"enignE ppA elgooG no gnitupmoC duolC" in resp_text.data
    print("[PASS] simple_web_app POST /text-analyzer: Status 200, String analyzed & reversed")

if __name__ == "__main__":
    print("Testing applications...")
    test_hello_world()
    test_simple_web_app()
    print("ALL TESTS PASSED SUCCESSFULLY!")
