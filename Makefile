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
	git pull; make kill; make run &
open:
	open https://keitaroemotion.github.io/bibleasmr/
setup:
	npm install react-router-dom
	npm i react-xml-viewer
	npm install express
	npm install react-markdown remark-gfm
	npm install react-helmet
