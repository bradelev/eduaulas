from eduaulas import settings    

def template_base(request):
    return {'template_base':'base.html', 'left_menu':'left.html'}
