
def triangle(base: int, height: int) -> float:
    print(0.5*base*height)

def test_triangle(capsys):
    # given
    base = 6
    height = 7
    # when
    field = triangle(base, height)
    out, err = capsys.readouterr()
    #then
    assert out == '21.0\n'