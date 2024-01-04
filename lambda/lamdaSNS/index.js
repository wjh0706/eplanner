const AWS = require('aws-sdk');
const ses = new AWS.SES();

exports.handler = async (event) => {
  const message = JSON.parse(event.Records[0].Sns.Message);

  // Perform action based on the event
  const { eventType, userId, userEmail } = message;
  
  const adminEmail = 'wujianghao0706@gmail.com'; 
  const subject = `Resource Change - ${eventType}`;
  const content = `User ${userId} has triggered a resource change. User email: ${userEmail}`;

  await sendEmail(adminEmail, subject, content);

  return {
    statusCode: 200,
    body: JSON.stringify('Action performed successfully'),
  };
};

async function sendEmail(to, subject, content) {
  const params = {
    Destination: {
      ToAddresses: [to],
    },
    Message: {
      Body: {
        Text: {
          Data: content,
        },
      },
      Subject: {
        Data: subject,
      },
    },
    Source: 'wujianghao0706@gmail.com', // Replace with your verified SES sender email
  };

  return ses.sendEmail(params).promise();
};