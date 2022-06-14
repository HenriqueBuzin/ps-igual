FROM node:18-alpine

WORKDIR /ps_equal_react

ENV PATH /ps_equal_react/node_modules/.bin:$PATH

COPY package.json /ps_equal_react/package.json

RUN npm install
RUN npm install react-scripts@5.0.1 -g

CMD ["npm", "start"]
