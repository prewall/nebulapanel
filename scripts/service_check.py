import sys, os

ELASTICSEARCH = os.popen('systemctl status elasticsearch | head -3 | grep running | cut -c 20-26').read(7)
LOGSTASH = os.popen('systemctl status logstash | head -3 | grep running | cut -c 20-26').read(7)
KIBANA = os.popen('systemctl status kibana | head -3 | grep running | cut -c 20-26').read(7)
SURICATA = os.popen('systemctl status suricata | head -3 | grep running | cut -c 20-26').read(7)
#ESS = open('es.tmp', 'r').read()
#print(ELASTICSEARCH)


def esServiceStatus():
	if ELASTICSEARCH == "running" :
		#print('Elasticsearch service is running')
		ES = "running"
		#print(ES)
		lsServiceStatus(ES)
	else:
		#print('Elasticsearch service is stopped')
		#print('I am starting elasticsearch service for you')
		#os.system('systemctl start elasticsearch > /tmp/srv.tmp')
		ES = "stopped"
		#print(ES)
		lsServiceStatus(ES)

def lsServiceStatus(ES):
        if LOGSTASH == 'running' :
                #print('Logstash service is running')
		LS = "running"
                kbServiceStatus(ES, LS)
        else:
                #print('Logstash service is stopped')
                #print('I am starting logstash service for you')
		LS = "stopped"
                #os.system('systemctl start logstash > /tmp/srv.tmp')
		kbServiceStatusES(ES, LS)

def kbServiceStatus(ES, LS):
        if KIBANA == 'running' :
                #print('Kibana service is running')
		KB = "running"
                srServiceStatus(ES, LS, KB)
        else:
                #print('Kibana service is stopped')
                #print('I am starting Kibana service for you')
		LS = "stopped"
                #os.system('systemctl start kibana > /tmp/srv.tmp')
                srServiceStatus(ES, LS, KB)

def srServiceStatus(ES, LS, KB):
        if SURICATA == 'running' :
                #print('Suricata service is running')
		SR = "running"
		printAll(ES, LS, KB, SR)
                
        else:
               # print('Suricata service is stopped')
               # print('I am starting Suricata service for you')
		SR = "stopped"
                #os.system('systemctl start suricata > /tmp/srv.tmp')
                printAll(ES, LS, KB, SR)

def printAll(ES, LS, KB, SR):
	print(ES)
	print(LS)
	print(KB)
	print(SR)
	exit(0)	

esServiceStatus()
