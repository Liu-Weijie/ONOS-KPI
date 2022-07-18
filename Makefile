image:
	docker build -t fb-kpimon-xapp:v0.2 -f Dockerfile ../
	docker tag fb-kpimon-xapp:v0.2 norijun/fb-kpimon-xapp:v0.3
	docker push norijun/fb-kpimon-xapp:v0.3

