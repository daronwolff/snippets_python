from datetime import datetime

def check_consecutivos(fechas_verificar):	
	dates = []
	for dt in fechas_verificar:
		dates.append(datetime.strptime(dt, "%Y-%m-%d"))

	date_ints = []
	for dt in dates:
		date_ints.append(dt.toordinal())
	date_ints = set(date_ints)
	if(len(date_ints)):
		if max(date_ints) - min(date_ints) == len(date_ints) - 1:
			print "Es consecutivo"
			return True
		else:
			print "No es consecutivo"
			return False
	else:
		print "No hay suficientes elementos especificados"
		return False


fechas_verificar = ['2012-01-27','2012-01-22','2012-01-30']
resultado = check_consecutivos(fechas_verificar)
print resultado
