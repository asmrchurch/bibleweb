start:
	npm start
kill:
	sh ./scripts/kill.sh 
run:
	npm run build
	sudo node server.js 
b:
	npm run build
deploy:
	sudo systemctl stop cron
	git pull origin HEAD
	npm run build
	sh ./scripts/kill.sh 
	sudo node server.js &
	sleep 10
	sudo systemctl start cron
open:
	open https://keitaroemotion.github.io/bibleasmr/
setup:
	npm install react-router-dom
	npm i react-xml-viewer
	npm install express
	npm install react-markdown remark-gfm
	npm install react-helmet
	npm install react-share
