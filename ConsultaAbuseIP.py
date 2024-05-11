#Programer: Juan Martinez
# Version 0.2
#
import io
import requests

archivoip = open("ips.txt",'r')
archivoip = archivoip.read().split('\n')


url = "https://api.abuseipdb.com/api/v2/check"
api_key = ""

#listado_ip = ['124.235.251.192', '177.36.187.95','122.176.52.13']

    
print('ip,', 'totalreport,','isp,','domain,','country,','LastReport AIP','AbuseIP')

#for cada_ip in listado_ip:
for cada_ip in archivoip:
    informacion = {
        "ipAddress": cada_ip,
        "maxAgeInDays": "90"
    }
    api = {
        "Key": api_key,
        "Accept": "application/json"
    }

    response = requests.get(url,headers=api, params=informacion)
    respuesta = response.json()
 #   print(respuesta)
    ip = respuesta['data']['ipAddress']
    reportes = respuesta['data']['totalReports']
    reporte2 = respuesta['data']['isp']
    reporte3 = respuesta['data']['domain']
    reporte4 = respuesta['data']['countryCode']
    reporte5 = respuesta['data']['lastReportedAt']
    abuseipd = "X"


    print(ip,",",reportes,",",reporte2,",",reporte3,",",reporte4,",",reporte5,",","abuseip")
