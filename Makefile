start:
	npm start
pm2:
	sudo pm2 start server.js --name react-app
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
	# sh ./scripts/kill.sh
	# sudo node server.js &
	sudo pm2 reload server.js --name react-app
	sudo systemctl start cron &
open:
	open https://keitaroemotion.github.io/bibleasmr/
setup:
	npm install react-router-dom
	npm i react-xml-viewer
	npm install express
	npm install react-markdown remark-gfm
	npm install react-helmet
	npm install react-share
	npm install dotenv
	npm install -g pm2
