def scripts(tab):
    return ["js/"+script_name+".js" for script_name in tab]


def css(tab):
    return ["css/"+css_name+".css" for css_name in tab]


def front_context(request):
    scripts_tab = ['test', 'links']
    styles_tab = ['menu', 'style']
    return {"scripts_wanted": scripts(scripts_tab), "styles": css(styles_tab), }
