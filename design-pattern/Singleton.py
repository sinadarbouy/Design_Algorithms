class ConfigurationManager:
  _instance = None
  
  def __new__(cls,*args,**kwargs):
    if not cls._instance:
      cls._instance = super(ConfigurationManager,cls).__new__(cls, *args, **kwargs)
    return cls._instance
  
  def __init__(self):
    if not hasattr(self, 'initialized'):
        self.load_configuration()
        self.initialized = True

  def load_configuration(self):
      self.config = {
          "database_url": "mysql://user:password@localhost/dbname",
          "logging_level": "DEBUG"
      }
  
  def get(self, key):
      return self.config.get(key)
    
# Usage
config1 = ConfigurationManager()
config2 = ConfigurationManager()

print(config1.get("database_url"))  # Output: mysql://user:password@localhost/dbname
print(config2.get("logging_level"))  # Output: DEBUG
print(config1 is config2)  # Output: True
