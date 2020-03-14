const webPush = require('web-push');

const pushSubscription = {"endpoint":"https://fcm.googleapis.com/fcm/send/fcEMEcaine8:APA91bGZLostOD8hXAg8NEn-jy3_fsuoRRMRLJ-RG0AgN97U_Bc88LPq9aRzufYWUhc9FvdDYoSk8Txc7V89-p_gla-1-n1bsfVx_f5De4kZzQ7dpCA1SFW7wFmExVK3xlKeouHEe7SM","expirationTime":null,"keys":{"p256dh":"BJKPK-j2qu-CP7AQkq5LL2Z3ZzWmSkqwmS3u7vwKfmam7315H75s02Rc6PGyQpTYkmumOC_YC6kYDMeclF-GlfY","auth":"jKX2bVkLAhf9hWmIhUB6uQ"}};

const vapidPublicKey = 'BHMjgLGN8nZiCSksH_wyULGMYCPr5rPdNU7wqr1Ttn8ZdodbnIZHPlF4L3jctp0FLV-WD4ux9-vUyE12qHtqRmI';
const vapidPrivateKey = 'htq0Ypw5K5Oqe3Vo9kXawCJ1d_2vDw4-bRMJj-brbKU';

const payload = 'Here is a payload!';

const options = {
  // gcmAPIKey: 'YOUR_SERVER_KEY',
  TTL: 60,
  vapidDetails: {
    subject: 'mailto:YOUR_EMAIL_ADDRESS',
    publicKey: vapidPublicKey,
    privateKey: vapidPrivateKey
  }
};

webPush.sendNotification(
  pushSubscription,
  payload,
  options
);
