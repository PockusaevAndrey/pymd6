# Simple library to calculate MD6 checksum

### Example
```python
from MD6 import MD6

if __name__ == '__main__':
    md6 = MD6()
    md6_hash = md6("Hello World!!")
    print(str(md6_hash)) # show hex
    print(md6_hash.raw()) # show raw utf-8 string
```
