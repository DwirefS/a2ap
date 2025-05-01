from agent_core.protocol import Envelope

def test_envelope():
    e = Envelope(message_id='1', timestamp='2025-05-01T00:00:00Z', sender_id='a', receiver_id='b', auth_token='t', signature='s')
    assert e.receiver_id == 'b'