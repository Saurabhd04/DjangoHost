from rest_framework import serializers
# from .models import Register
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
# from allauth.account.utils import setup_user_email

# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only= True)
    

class CustomRegisterSerializer(RegisterSerializer):
    AadhaarNumber = serializers.CharField(max_length=12)
    # Otp = serializers.BooleanField()
    # Otp2 = serializers.BooleanField()
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['AadhaarNumber'] = self.validated_data.get('AadhaarNumber', '')
        # data_dict['Otp'] = self.validated_data.get('Otp', '')
        # data_dict['Otp2'] = self.validated_data.get('Otp2', '')
        return data_dict



#     class Meta:
#         model = Register
#         # fields = ['UserName','EmailId', 'Password', 'password2']
#         fields = '__all__'
#         # extra_kwargs = {
#         #     'Password' : {'write_only' : True, 'read_only' : True}
#         # }

#     def save(self):

#         email = self.validated_data['email']
#         # username = self.validated_data['username']
#         if Register.objects.filter(email = email).exists():
#             raise serializers.ValidationError({'email' : 'Email already exists'})
#         # elif Register.objects.filter(username = username).exists():
#         #     raise serializers.ValidationError({'username' : 'Username already exists'})

#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password' : 'Password must match.'})
        

#         register = Register(
#             username = self.validated_data['username'],
#             email = self.validated_data['email'],
#             password = self.validated_data['password']
#         )    
#         register.save()
#         return register

