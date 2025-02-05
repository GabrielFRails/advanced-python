from functools import wraps

def log_info(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		#decorator stuff
		print(f"{func.__name__}() {args} {kwargs}")
		
		# execute the decorating function
		return func(*args, **kwargs)
	return wrapper

@log_info
def get_datafeed(ticker):
	return True

@log_info
def publish_ticker(ticker):
	return True

get_datafeed("WDO23F")
publish_ticker("WDO24Z")

