import uuid, datetime
print("Simulating A2A Message...")
msg = {
  "message_id": str(uuid.uuid4()),
  "timestamp": datetime.datetime.utcnow().isoformat(),
  "sender_id": "agent://demo1",
  "receiver_id": "agent://demo2"
}
print("Message:", msg)