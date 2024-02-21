const request = require('request');

// API URL
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    // Iterate over the todos
    for (const todo of todos) {
      // If the task is completed, increment the count for the user
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    }

    // Print users with completed tasks
    for (const userId in completedTasksByUser) {
      console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks.`);
    }
  } else {
    console.log('An error occurred while fetching the data.');
  }
});
