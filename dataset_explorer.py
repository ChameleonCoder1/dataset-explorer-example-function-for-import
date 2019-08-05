
def describe_vars(data,n_values=9):
	"""
	For each variable, print the name, 
	number of values, and type. If variable has
	less than n_values number of values,
	print the values and their counts.
	Data is a pandas dataframe.
	"""
	vars_with_less_than_n_values=[]
	for var in list(data.columns):
		varcount=data[var].nunique()
		datatype=data[var].dtype
		print("The var " + var + " has:"+ " {} values".format(varcount))
		print("      of dtype: " + " {}".format(datatype))
		if varcount<n_values:
			print("....of which are: ")
			varnames=data[var].value_counts()
			print("{}".format(varnames))
			#save var names with less than 9 unique values
			vars_with_less_than_n_values.append(var)
		print()
	print(vars_with_less_than_n_values)


def frequency_encoding(data,variable):
    """
    Transform a categorical variable into a nominal
    variable based on frequency counts (raw frequencies,
    without respect to target frequencies). The variable
    can then be treated as numerical. With this function,
    run:
    for variable in tqdm(frequency_encoded_variables):
        freq_enc_dict = frequency_encoding(variable)
        data[variable] = data[variable].map(lambda x: freq_enc_dict.get(x, np.nan))
    """
    t = data[variable].value_counts().reset_index()
    t = t.reset_index()
    t.loc[t[variable] == 1, 'level_0'] = np.nan
    t.set_index('index', inplace=True)
    max_label = t['level_0'].max() + 1
    t.fillna(max_label, inplace=True)
    return t.to_dict()['level_0']


