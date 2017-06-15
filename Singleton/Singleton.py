import unittest

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ObjectSingleton():
	__metaclass__ = Singleton

class TestSingleton(unittest.TestCase):
	def test_singleton(self):
		singleton_one = ObjectSingleton()
		singleton_two = ObjectSingleton()
		self.assertEqual(id(singleton_one), id(singleton_two))

if __name__ == '__main__':
    unittest.main() 