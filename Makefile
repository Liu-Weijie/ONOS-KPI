image:
	docker build -t fb-kpimon-xapp:v0.1 -f Dockerfile ../
	docker tag fb-kpimon-xapp:v0.1 norijun/fb-kpimon-xapp:v0.2
	docker push norijun/fb-kpimon-xapp:v0.2

