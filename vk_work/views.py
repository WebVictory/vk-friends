from django.shortcuts import render, redirect

import vk_api

def index(request):
    vk_token = request.session.get('vk_token', 0)
    if vk_token != 0:
        vk_session = vk_api.VkApi(token = request.session['vk_token'] )
        vk = vk_session.get_api()
        account = vk.users.get()
        full_name = account[0]['first_name'] + " " + account[0]['last_name']
        friends = vk.friends.get(count=9, fields = ['nickname', 'photo_200',], order = 'random', )
        context = {'response': response, 'account': account, 'friends': friends, 'full_name': full_name}

        return render(request, 'oauth_result.html', context)

    return render(request, 'index.html')

def response(request):

    code = request.GET.get("code", "")
    redirect_url = 'http://viteka.pythonanywhere.com/response/'
    app = 000000
    secret = ''

    vk_session = vk_api.VkApi(app_id=app, client_secret=secret)
    vk_session.code_auth(code, redirect_url)

    request.session['vk_token'] = vk_session.token['access_token']

    return redirect("/")