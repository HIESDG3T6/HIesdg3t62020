var uri = "https://sandbox-authservice.priaid.ch/login";
var secret_key = "mysecretkey";
var computedHash = CryptoJS.HmacMD5(uri, secret_key);
var computedHashString = computedHash.toString(CryptoJS.enc.Base64);     
console.log('head');
async function getToken() {
    console.log('tail');
    // var serviceURL = "https://sandbox-authservice.priaid.ch/login" + "/" + isbnNumber;
    try {
        let response = await fetch('https://sandbox-authservice.priaid.ch/login', {
            method: 'POST',
            headers: {
                'Host': 'authservice.priaid.ch',
                'Bearer huifen.ong.2018@smu.edu.sg': computedHashString
            },
        });
        const data = await response.json();
        const token = data.Token();
        // console.log(response);
    }
catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        showError
        ('There is a problem retrieving books data, please try again later.<br />'+error);
        
    }
}