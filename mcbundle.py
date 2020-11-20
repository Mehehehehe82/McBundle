def text_to_item(text):
	return f"""{"{"}id:"minecraft:{text}",Count:1{"}"}"""
#end
def array_to_bundle_data(array, prefix="give @p bundle"):
	full_array = []
	for i in array:
		full_array.append(text_to_item(i))
	full_text = ",".join(full_array)
	return f"""{prefix}{"{"}Items:[{full_text}]{"}"}"""
#end