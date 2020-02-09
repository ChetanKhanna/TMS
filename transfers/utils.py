def get_context_data(user, designation=None):
    context = {}
    try:
        context['error'] = False
        context['message'] = 'success'
        context['data'] = {
            'username' : 'user.username',
            'designation': designation,
            'campus': user.userprofile.campus,
            'email': user.email,
        }
    except:
        context['error'] = True
        context['message'] = 'failure'
        context['data'] = []

    return (context)
