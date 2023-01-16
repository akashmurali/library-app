from rest_framework_simplejwt.tokens import RefreshToken

def create_token(user):
	
	refresh = RefreshToken.for_user(user)	

	return {
		'refresh_token': str(refresh),
		'access_token': str(refresh.access_token),		
	}
