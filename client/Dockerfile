FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm install sass-loader node-sass --save-dev

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]