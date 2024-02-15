# example-kserve-custom-model

This is an example Kserve Custom Predictor.

## Usage

```bash
docker build -t local/kserve-custom-model:example .
docker run -ePORT=8080 -p8080:8080  local/kserve-custom-model:example
```

To test the endpoint:

```bash
curl -X POST http://localhost:8080/v2/models/model/infer -H 'Content-Type: application/json' -d @./input.json
```
