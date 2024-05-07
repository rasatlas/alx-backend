# 0x03. Queuing System in JS
`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

## Resources
**Read or watch:**

- [Redis quick start](https://redis.io/docs/latest/integrate/)
- [Redis client interface](https://redis.io/docs/latest/develop/connect/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue) deprecated but still use in the industry

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## Requirements

- All of your code will be compiled/interpreted on `Ubuntu 18.04`, `Node 12.x`, and `Redis 5.0.7`
- All of your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension

## Required Files for the Project

**`package.json`**

```JSON
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }

```

**`.babelrc`**

```JSON
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

**and…**
Don’t forget to run `$ npm install` when you have the `package.json`

## Tasks

### 0. Install a redis instance
### 1. Node Redis Client
### 2. Node Redis client and basic operations
### 3. Node Redis client and async operations
### 4. Node Redis client and advanced operations
### 5. Node Redis client publisher and subscriber
### 6. Create the Job creator
### 7. Create the Job processor
### 8. Track progress and errors with Kue: Create the Job creator
### 9. Track progress and errors with Kue: Create the Job processor
### 10. Writing the job creation function
### 11. Writing the test for job creation
### 12. In stock?
### 13. Can I have a seat?
