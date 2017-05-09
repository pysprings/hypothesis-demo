import runlength

from hypothesis import given, example, strategies as st

@given(st.text())
@example('')
def test_decode_inverts_encode(s):
    assert runlength.decode(runlength.encode(s)) == s
