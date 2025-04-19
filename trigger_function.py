# ====================8<-----------------------------------
blacklist = ["change_log", "updated_at", "created_at"]
# ----------------------------->8==========================

import json

def jsonify_rec(changed_record):
  def simplify(value):
    if ISREF(value):
      return value.id
    elif ISREFLIST(value):
      return ["L"] + [v.id for v in value]
    return value

  result = {k: simplify(v) for k, v in changed_record.items() if k not in blacklist}
  return result

def are_equal(value1, value2):
  # Check if both values are lists
  if isinstance(value1, list) and isinstance(value2, list):
    if len(value1) != len(value2):
      return False
    # Compare each element in the lists
    for item1, item2 in zip(value1, value2):
      if item1 != item2:
        raise ValueError(f"List items differ: {item1} != {item2}")
        return False
    return True
  return value1 == value2  # Fallback to direct comparison for non-list values

# Trigger formula code
logs_json = PEEK(rec.change_log) or "[]"
logs = json.loads(logs_json)

current_snapshot = jsonify_rec(PEEK(RECORD(rec, dates_as_iso=True)))
previous_snapshot = logs[0]["snapshot"] if logs else {}

changed_fields = [
  field for field in current_snapshot
  if not are_equal(current_snapshot.get(field), previous_snapshot.get(field))
]

log = {
  "timestamp": NOW().isoformat(),
  "changed": changed_fields,
  "snapshot": current_snapshot
}
logs.insert(0, log)  # Prepend the new log entry
return json.dumps(logs)