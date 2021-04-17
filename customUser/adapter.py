from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        data = form.cleaned_data
        user.AadhaarNumber = data.get('AadhaarNumber', '')
        # user.Otp = data.get('Otp', '')
        # user.Otp2 = data.get('Otp2', '')
        user.save()
        return user