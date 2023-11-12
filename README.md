template-generator
====

## install
```bash
git clone https://github.com/vane/template-generator
cd template-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## help
```bash
python template-generator.py -h
```

## templates
- templates/go-bazel - generate bazel go template  
run example - generates github.com/foo/bar module in tmp/bar directory
```bash
ORG_NAME=foo MODULE_NAME=bar python template-generator.py
```