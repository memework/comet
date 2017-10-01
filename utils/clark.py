#RIP CLARK KENT
import ruamel.yaml as yaml
def load(path):
	with open(path, 'r') as f:
		x = yaml.safe_load(f)
	return x
def save(pointer, path):
	with open(path, 'w') as f:
	    yaml.dump(pointer, f)