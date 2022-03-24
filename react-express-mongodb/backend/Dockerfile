FROM node:lts-buster-slim

# Create app directory
WORKDIR /usr/src/app

RUN npm install -g nodemon
RUN npm install -g react-scripts


COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json
RUN npm install

COPY . /usr/src/app

EXPOSE 3000

CMD [ "npm", "run", "dev" ]
