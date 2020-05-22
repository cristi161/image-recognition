import requests
def translate(text):
    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"
    querystring = {"source":"en","target":"ro","input": text}
    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "1353cfae90mshea2870cfcff4cacp179496jsn0f4a0afd5a2c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

print(translate("Hello"))