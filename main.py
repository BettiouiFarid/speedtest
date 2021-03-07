import speedtest

s = speedtest.speedtest()
print("My download speed is :",s.download()/pow(10,6),"Mbps")
print("My upload speed is :",s.upload()/pow(10,6),"Mbps")

best_server = s.get_best_server()

for key , value in best_server.items() :
    print("Best server : \n"+ key,' : ', value)

closest_server = s.get_closest_servers()
for key , value in closest_server[1].items() :
    print("closest Servers : \n"+ key, " : ", value)
    
