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
    elif isinstance(value, tuple):
        return list(value)
    return value

  result = {k: simplify(v) for k, v in changed_record.items() if k not in blacklist}
  return result

# Trigger formula code
current_snapshot = jsonify_rec(RECORD(rec, dates_as_iso=True))
logs_json = current_snapshot.get('change_log') or "[]"
logs = json.loads(logs_json)
previous_snapshot = logs[0]["snapshot"] if logs else {}

changed_fields = [
  field for field in current_snapshot
  if current_snapshot.get(field) != previous_snapshot.get(field)
]

log = {
  "timestamp": NOW().isoformat(),
  "changed": changed_fields,
  "snapshot": current_snapshot
}
logs.insert(0, log)  # Prepend the new log entry
return json.dumps(logs)