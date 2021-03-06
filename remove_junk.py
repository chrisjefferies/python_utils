# A basic cleanup utility for large text files. 
#
# In testing, it filters at about 10,000 lines/second 
# For non-multipbyte character files with 0 to 1024 bytes per line. 
try:
	# Look for configurable import file (provided with filter_str variable defined)
	from config.log_filter import *
	print 'imported: ', filter_str
except:
	filter_str = []

def remove_junk(src, dst, match_remove):
	with open(src) as f:
		lines = f.read().splitlines()
		for n in range(0, len(lines) - 1):
			if n % 1000 == 0:
				print '.'
			match = False
			for i in range(0, len(filter_str)):
				if lines[n].find(filter_str[i]) > -1:
					match = True
			if not match:
				g = open(dst, 'a')
				g.write(lines[n] + '\n')
				g.close()

# Secondarily, config Filter Strings here. 
# filter_str.append('a filter string.')

remove_junk('error_logs/error.log', 'error_logs/log-0.txt', filter_str)