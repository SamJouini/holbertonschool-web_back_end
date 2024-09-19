const process = require('process');

process.stdout.write('Welcome to Holberton School, what is your name?\n');

let inputBuffer = '';

process.stdin.on('data', (chunk) => {
    inputBuffer += chunk;
    if (inputBuffer.includes('\n')) {
        const name = inputBuffer.trim();
        process.stdout.write(`Your name is: ${name}\n`);
        process.stdin.pause();
        console.log('This important software is now closing');
        process.exit(0);
    }
});

process.stdin.on('end', () => {
    console.log('This important software is now closing');
    process.exit(0);
});
