import hashlib
import collections

def hash_str(string): 
    return hashlib.md5(string.encode()).hexdigest()

def hash(value):
  if (isinstance(value, dict)):
    return { key: hash_str(val) for key, val in value.items() }

  if (isinstance(value, str)):
    return hash_str(value)

  try:
    return list(map(hash_str, value))
  except TypeError:
    return hash_str(value)

print(hash('masha'))
print(hash(['masha', 'makes', 'money']))
print(hash({ 'name': 'masha' }))