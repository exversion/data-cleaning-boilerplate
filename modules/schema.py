#############################
#
# Functions to Alter the Schema
#
#############################

def filter_obj(fn, obj):
	edit = dict()
	for n in fn:
		try:
			edit[n] = obj[n]
		except:
			edit[n] = ''
	return edit
	
def rename_col(old_name, new_name, obj):
	obj[new_name] = obj[old_name]
	obj.pop(old_name, None)
	return obj
	
def remove_col(col_name, obj):
	obj.pop(col_name, None)