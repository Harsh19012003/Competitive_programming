# def get_query_param_values(url, param_names):
#     url_parts = url.split("?")
#     if len(url_parts) != 2:
#         return {}
# 
#     base_url, query_string = url_parts
# 
#     params = query_string.split("&")
#     
#     param_dict = {}
#     
#     for param in params:
#         key_value = param.split("=")
#         if len(key_value) == 2:
#             key, value = key_value
#             param_dict[key] = value
#     
#     filtered_params = {param_name: param_dict.get(param_name) for param_name in param_names}
#     
#     return filtered_params
# 
# url = "http://www.deltax.com/career?"
# 
# param_names = ["name", "city"]
# 
# param_values = get_query_param_values(url, param_names)
# 
# for param_name, param_value in param_values.items():
#     print(f"{param_name}: {param_value}")
# 
# 
# 
# 



url = input()
N = int(input())
url_parts = url.split('?')

if len(url_parts) == 2:
    query_string = url_parts[1]
    query_params = query_string.split('&')
    params_dict = {}
    
    for param in query_params:
        key_value = param.split('=')
        if len(key_value) == 2:
            key, value = key_value
            params_dict[key] = value
    
    for _ in range(N):
        key = input()
        value = params_dict.get(key, "-1")
        print(value)
else:
    for _ in range(N):
        print("-1")