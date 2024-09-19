const fs = require('fs');

function countStudents(path) {
  try {
    // Read the database file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the data into lines and remove empty lines
    const lines = data.split('\n').filter(line => line.trim() !== '');

    // Remove the header line
    const students = lines.slice(1);

    // Log the total number of students
    console.log(`Number of students: ${students.length}`);

    // Object to store students by field
    const fieldCounts = {};

    // Process each student
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fieldCounts[field]) {
        fieldCounts[field] = { count: 0, list: [] };
      }
      fieldCounts[field].count++;
      fieldCounts[field].list.push(firstName);
    });

    // Log the number of students in each field
    for (const [field, data] of Object.entries(fieldCounts)) {
      console.log(`Number of students in ${field}: ${data.count}. List: ${data.list.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;