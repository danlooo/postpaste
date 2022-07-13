FROM node:18.5.0-slim
WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY ./ ./
RUN npm run build

# USER node
EXPOSE 3000
CMD npm run dev