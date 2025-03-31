# python.text2doc.com


        
```bash
# Clean up any previous build artifacts
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m pip install --upgrade pip build
python -m build

# Publish to PyPI (if needed)
python -m pip install --upgrade twine
python -m twine upload dist/*

```