from django.shortcuts import redirect
def login_requerido(vista):
    def interna(request,*args,**kwargs):
        if not request.session.get('acceso',False):
            return redirect('')
        return vista(request,*args,**kwargs)
    return interna
