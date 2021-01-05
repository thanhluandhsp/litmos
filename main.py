from litmos import Litmos


API_KEY = '387b5351-2740-4fc1-a61d-2f6987dba41e'
LITMOS_APP_NAME = 'pva-uat'
LITMOS_SERVER_URL = 'https://api.litmos.com.au/v1.svc'  # https://support.litmos.com/hc/en-us/articles/227734667-Overview-Developer-API
litmos = Litmos(API_KEY, LITMOS_APP_NAME, LITMOS_SERVER_URL)


# --- User ---
# retrieve users
all_users = litmos.User.all()
#print(all_users);
#find user by Id
user = litmos.User.find('ZjJPv_tAjxU1')
print(user);