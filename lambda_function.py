import json
import base64
import datetime 

records = []

def lambda_handler(event, context):
  for record in event["records"]:
    json_data = json.loads(base64.b64decode(record["data"]))

    enriched_data = json_data
    enriched_data["processedAt"] = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

    json_string = json.dumps(enriched_data).encode("ascii")
    b64_encoded_data = base64.b64encode(json_string).decode("ascii")

    rec = {'recordId': record["recordId"], 'result': 'Ok', 'data': b64_encoded_data}
    records.append(rec)
  return {'records': records}
